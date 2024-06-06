import csv
import datetime
import os
from tkinter import *
from tkinter import font
from tkinter import ttk

import cv2
import numpy as np
from PIL import Image, ImageTk

# main app class
class rootApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.font = font.Font(family="Helvetica", size=28, weight="bold")

        self.geometry("1200x700")
        self.resizable(width=False, height=False)
        self.title("  Attendance System")
        self.iconbitmap(default="Files/icon.ico")

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for i in (HomePage, StudentsPage, AttendancePage, RecordATTPage, CreateDataPage):
            page_name = i.__name__
            frame = i(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("HomePage") 

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()  

# variables to be used
n=0
haar_file = 'Files/haarcascade_frontalface_default.xml'
datasets = 'Dataset'

# homepage class
class HomePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="White")

        logo = ImageTk.PhotoImage(Image.open("Files/icon.png"))
        logo_btn = Button(self, text="  Attendify", command=lambda : controller.show_frame("HomePage"), font=("Helvetica", 15, "bold"), bd=0, image=logo, bg="white", compound="left", activebackground="white")
        logo_btn.image = logo
        logo_btn.place(x=0,y=0)

        self.drawer = Frame(self, bg="#f2f0ed", bd=2)

        stu_img = ImageTk.PhotoImage(Image.open("Files/students.png").resize((70,70)))
        stu_btn = Button(self.drawer, bd=0, text="Students", image=stu_img, compound="top", bg="white", activebackground="white",command=lambda:controller.show_frame("StudentsPage"))
        stu_btn.image = stu_img
        stu_btn.grid(row=0,column=0)

        att_img = ImageTk.PhotoImage(Image.open("Files/attendance.png").resize((70,70)))
        att_btn = Button(self.drawer, bd=0, text="Attendance", image=att_img, compound="top", bg="white", activebackground="white", command=lambda:controller.show_frame("AttendancePage"))
        att_btn.image = att_img
        att_btn.grid(row=0,column=1)

        tr_img = ImageTk.PhotoImage(Image.open("Files/Face.png").resize((70,70)))
        tr_btn = Button(self.drawer, bd=0, text="Scan", image=tr_img, compound="top", bg="white", activebackground="white", command=lambda:controller.show_frame("RecordATTPage"))
        tr_btn.image = tr_img
        tr_btn.grid(row=1,column=0)

        cr_img = ImageTk.PhotoImage(Image.open("Files/create.png").resize((70,70)))
        cr_btn = Button(self.drawer, bd=0, text="Record", image=cr_img, compound="top", bg="white", activebackground="white", command=lambda:controller.show_frame("CreateDataPage"))
        cr_btn.image = cr_img
        cr_btn.grid(row=1,column=1)

        def control_drawer():
            global n
            if n==0:
                self.drawer.place(x=1030,y=40)
                self.drawer.tkraise()
                n+=1
            else:
                self.drawer.place_forget()
                n-=1

        features = Button(self, activebackground="white", bg="white", bd=0, text="⫶⫶⫶", compound="top", command=control_drawer, font=("Helvetica", 18, "bold"))
        features.place(x=1120, y=-5)

        def settime():
            dateandtime = datetime.datetime.now()
            date_time.config(text=str(dateandtime.strftime("%I:%M %p.%a,%b %d")))
            date_time.after(1000, settime)

        date_time = Label(self, bd=0, bg="white", fg="black", font=("courier", 15))
        settime()
        date_time.place(x=870, y=5)

        lbl2 = Label(self, text="Simulasi Penggunaan Face Recognition Untuk Absensi Kelas", justify="left", wraplength=580, font=("Helvetica", 26), fg="grey", bg="white")
        lbl2.place(x=80, y=260)
        
        record = Button(self, text="Klik Tab Menu Di Kanan Atas", command=lambda:controller.show_frame("RecordATTPage"), bd=0, font=("Helvetica", 26), fg="Black", bg="white")
        record.place(x=80, y= 350)

        show_img = ImageTk.PhotoImage(Image.open("Files/class.png").resize((300,280)))
        showcase = Label(self, bg="white", image = show_img)
        showcase.image = show_img
        showcase.place(x=830, y=210)

# students list page class
class StudentsPage(Frame):
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg= "white")

        logo = ImageTk.PhotoImage(Image.open("Files/icon.png"))
        logo_btn = Button(self, text="Attendance", command=lambda : controller.show_frame("HomePage"), font=("Helvetica", 15, "bold"), bd=0, image=logo, bg="white", compound="left", activebackground="white")
        logo_btn.image = logo
        logo_btn.place(x=0,y=0)

        title = Label(self, text= "Students List", bg  ="White", fg ="red", font=("Helvetica", 25, "italic"))
        title.place(relx=0.5,rely=0.1,anchor=CENTER)

        TableMargin1 = Frame(self, width=500)
        TableMargin1.place(relx=0.1, rely=0.2)
        scrollbary1 = Scrollbar(TableMargin1, orient=VERTICAL)

        table1 = ttk.Treeview(TableMargin1, columns=("Name"), height=400, selectmode="extended", yscrollcommand=scrollbary1.set)
        scrollbary1.config(command=table1.yview)
        scrollbary1.pack(side=RIGHT, fill=Y)

        table1.heading('Name', text="Name", anchor=W)
        table1.column('#0', stretch=NO, minwidth=0, width=0)
        table1.column('#1', stretch=NO, minwidth=0, width=200)
        table1.pack()

        def show_st():
            if os.path.isdir('Dataset'):
                for item in table1.get_children():
                    table1.delete(item)
                for i in os.listdir('Dataset'):
                    table1.insert("", 0, values=i)
                
            table1.after(100, show_st)
        
        show_st()

# students list page class
class CreateDataPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg= "white")

        logo = ImageTk.PhotoImage(Image.open("Files/icon.png"))
        logo_btn = Button(self, text="Attendance", command=lambda : controller.show_frame("HomePage"), font=("Helvetica", 15, "bold"), bd=0, image=logo, bg="white", compound="left", activebackground="white")
        logo_btn.image = logo
        logo_btn.place(x=0,y=0)
        
        def record():
            sub_data = name.get()
            datasets = "Dataset"
            path = os.path.join(datasets, sub_data)

            if os.path.isdir(path):
                count = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]) + 1
            else:
                os.mkdir(path)
                count = 1

            face_cascade = cv2.CascadeClassifier(haar_file)
            webcam = cv2.VideoCapture(0)
            name.set("")
            while count <= 100:
                (_, im) = webcam.read()
                gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 4)
                for (x, y, w, h) in faces:
                    cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    face = gray[y:y + h, x:x + w]
                    face_resize = cv2.resize(face, (130, 100))
                    cv2.imwrite('% s/% s.png' % (path, count), face_resize)
                    count += 1
                cv2.imshow('OpenCV', im)
                key = cv2.waitKey(10)
                if key == 27:
                    break
            webcam.release()
            cv2.destroyAllWindows()

        def go_back():
            controller.show_frame("StudentsPage")
        
        lbl = Label(self, text="Create Student Data", font=("Helvetica", 22), bg="white", fg="red")
        lbl.place(relx=0.5, rely=0.1, anchor=CENTER)

        Label(self, text="Name       ", font=("Helvetica", 20), bg="white").place(relx=0.35, rely=0.5, anchor=CENTER)

        name = StringVar()
        name.set("")
        Entry(self, textvariable=name, font=("Helvetica", 20), bg="white").place(relx=0.5, rely=0.5, anchor=CENTER)

        Button(self, text="Record", font=("Helvetica", 15), command=record, bg="white").place(relx=0.4, rely=0.6, anchor=CENTER)
        Button(self, text="Back", font=("Helvetica", 15), command=go_back, bg="white").place(relx=0.6, rely=0.6, anchor=CENTER)

class AttendancePage(Frame):
    
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg= "white")

        logo = ImageTk.PhotoImage(Image.open("Files/icon.png"))
        logo_btn = Button(self, text="Attendance", command=lambda : controller.show_frame("HomePage"), font=("Helvetica", 15, "bold"), bd=0, image=logo, bg="white", compound="left", activebackground="white")
        logo_btn.image = logo
        logo_btn.place(x=0,y=0)

        title = Label(self, text= "Attendance", bg  ="White", fg ="red", font=("Helvetica", 25, "italic"))
        title.place(relx=0.5,rely=0.1,anchor=CENTER)

        TableMargin = Frame(self, width=500)
        TableMargin.place(relx=0.1, rely=0.2)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

        table = ttk.Treeview(TableMargin, columns=("Name", "Attendance", "Date", "Time"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=table.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=table.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        table.heading('Name', text="Name", anchor=W)
        table.heading('Attendance', text="Attendance", anchor=W)
        table.heading('Date', text="Date", anchor=W)
        table.heading('Time', text="Time", anchor=W)
        table.column('#0', stretch=NO, minwidth=0, width=0)
        table.column('#1', stretch=NO, minwidth=0, width=200)
        table.column('#2', stretch=NO, minwidth=0, width=200)
        table.column('#3', stretch=NO, minwidth=0, width=300)
        table.column('#4', stretch=NO, minwidth=0, width=300)
        table.pack()

        def show_att():
    
            if os.path.isfile("Files/Attendance.csv") == True:
                for item in table.get_children():
                    table.delete(item)

                with open('Files/Attendance.csv') as f:
                    reader = csv.DictReader(f, delimiter=',')
                    for row in reader:
                        name = row['Name']
                        att = row['Attendance']
                        date = row['Date']
                        time = row['Time']
                        table.insert("", 0, values=(name, att, date, time))
            table.after(100, show_att)
        
        show_att()

    
class RecordATTPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg="white")

        logo = ImageTk.PhotoImage(Image.open("Files/icon.png"))
        logo_btn = Button(self, text="Attendance", command=lambda: controller.show_frame("HomePage"),
                          font=("Helvetica", 15, "bold"), bd=0, image=logo, bg="white", compound="left",
                          activebackground="white")
        logo_btn.image = logo
        logo_btn.place(x=0, y=0)

        Button(self, text="Start Attendance", font=("Helvetica", 22), command=self.attendance, bg="white").place(relx=0.5, rely=0.3, anchor=CENTER)

        self.stop_button = Button(self, text="Stop Attendance", font=("Helvetica", 22), command=self.stop_attendance, bg="white")
        self.stop_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.running = False

    def markAttendance(self, name):
        current_time = datetime.datetime.now().strftime("%I:%M %p.%a,%b %d")
        date = datetime.datetime.now().strftime("%b %d")
        existing_attendance = set()

        if os.path.exists("Files/Attendance.csv"):
            with open("Files/Attendance.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 3:
                        existing_attendance.add((row[0], row[2]))

        if (name, date) not in existing_attendance:
            with open("Files/Attendance.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([name, "Present", date, current_time])

    def attendance(self):
        self.running = True
        dataset = 'Dataset'
        names = []
        images = []
        labels = []
        id = 0

        for subdir in os.listdir(dataset):
            if os.path.isdir(os.path.join(dataset, subdir)):
                for filename in os.listdir(os.path.join(dataset, subdir)):
                    path = os.path.join(dataset, subdir, filename)
                    images.append(cv2.imread(path, 0))
                    labels.append(id)
                names.append(subdir)
                id += 1

        if len(images) == 0 or len(labels) == 0:
            print("No training data found.")
            return

        images, labels = [np.array(lis) for lis in [images, labels]]

        # Create the LBPH face recognizer
        model = cv2.face.LBPHFaceRecognizer_create()
        model.train(images, labels)

        face_cascade = cv2.CascadeClassifier(haar_file)
        webcam = cv2.VideoCapture(0)

        while self.running:
            _, im = webcam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
                face = gray[y:y + h, x:x + w]
                prediction = model.predict(face)
                if prediction[1] < 100:
                    cv2.putText(im, '% s - %.0f' % (names[prediction[0]], prediction[1]),
                                (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                    self.markAttendance(names[prediction[0]])
                else:
                    cv2.putText(im, 'not recognized', (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            cv2.imshow('OpenCV', im)
            key = cv2.waitKey(10)
            if key == 27:
                break
            self.update_idletasks()  # Allow tkinter to process events
            self.update()  # Allow tkinter to process events

        webcam.release()
        cv2.destroyAllWindows()

    def stop_attendance(self):
        self.running = False


if __name__ == "__main__":
    app = rootApp()
    app.mainloop()