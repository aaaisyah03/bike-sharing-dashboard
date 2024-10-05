# Dashboard Peminjaman Sepeda v1.0

## Deskripsi
Dashboard Peminjaman Sepeda adalah aplikasi web yang memberikan analisis peminjaman sepeda berdasarkan data peminjaman per jam dan per hari. Aplikasi ini menggunakan Streamlit untuk membuat antarmuka pengguna yang interaktif dan mudah digunakan. Dashboard ini bertujuan untuk memberikan wawasan tentang pola peminjaman sepeda sehingga dapat membantu pengelola dalam pengambilan keputusan.

## Fitur
- Menampilkan tabel peminjaman sepeda per jam.
- Menampilkan tabel peminjaman sepeda per hari dengan pemetaan nama hari.
- Visualisasi grafik peminjaman sepeda per jam dan per hari.
- Filter peminjaman berdasarkan tanggal.

## Teknologi yang Digunakan
- Python: Bahasa pemrograman untuk pengembangan aplikasi.
- Pandas: Untuk pengolahan dan analisis data.
- Streamlit: Untuk membangun antarmuka pengguna web.
- Matplotlib: Untuk visualisasi data dalam bentuk grafik.

## Persyaratan
Sebelum menjalankan aplikasi, pastikan Anda telah menginstal semua paket yang diperlukan. Anda dapat menggunakan `pip` untuk menginstal dependensi:


```bash
pip install pandas streamlit matplotlib

Cara Menjalankan Aplikasi
Pastikan dataset (hour.csv dan day.csv) tersedia di jalur berikut: C:/Users/aaais/.vscode/python/dashboard/Submission/data/

Jalankan aplikasi Streamlit dengan perintah berikut di terminal:

streamlit run dashboard.py

Buka browser Anda dan kunjungi http://localhost:8501 untuk melihat dashboard.

