# Sistem Absensi Menggunakan Face Recognition

Aplikasi ini adalah simulasi sistem absensi yang menggunakan teknologi pengenalan wajah. Dibangun menggunakan Python dengan GUI berbasis Tkinter.

## Persyaratan

Pastikan Anda telah menginstall Python (versi 3.6 atau yang lebih baru). Anda dapat mengunduhnya dari [situs resmi Python](https://www.python.org/downloads/).

### Instalasi

1. **Clone repositori ini**:
    ```sh
    git clone https://github.com/username/repository.git
    cd repository
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Jalankan aplikasi**:
    ```sh
    python main.py
    ```

## Penggunaan

### Halaman Utama

- Klik tab menu di kanan atas untuk membuka drawer yang berisi pilihan menu seperti **Students**, **Attendance**, **Scan**, dan **Record**.

### Halaman Students

- Daftar nama mahasiswa yang terdaftar dalam sistem.

### Halaman Create Data

- Masukkan nama mahasiswa baru dan klik tombol **Record** untuk merekam wajah menggunakan webcam. 

### Halaman Attendance

- Melihat catatan absensi mahasiswa.

### Halaman Record Attendance

- Klik **Start Attendance** untuk memulai proses absensi menggunakan pengenalan wajah. Klik **Stop Attendance** untuk menghentikan proses.
