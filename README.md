# Script Auto Input Produk Prabayar H2H Serpul.co.id

Script ini adalah alat otomatisasi untuk menginput data produk prabayar h2h serpul menggunakan Python dan Selenium.

## Persyaratan Sistem
- Python 3.7 atau lebih baru
- Google Chrome browser
- Koneksi internet yang stabil
- File Excel dengan format yang sesuai

## Panduan Instalasi

### 1. Instalasi Python
1. Kunjungi https://www.python.org/downloads/
2. Unduh versi Python terbaru untuk sistem operasi Anda
3. Jalankan installer dan ikuti petunjuk instalasi
4. **PENTING**: Pastikan untuk mencentang opsi "Add Python to PATH" selama instalasi

Untuk memverifikasi instalasi, buka Command Prompt dan ketik:
python --version

### 2. Instalasi pip (Python package manager)
pip biasanya sudah terinstal bersama dengan Python. Untuk memverifikasi, buka Command Prompt dan ketik:
pip --version

Jika pip belum terinstal, ikuti langkah berikut:
1. Buka Command Prompt sebagai Administrator
2. Jalankan perintah berikut:
   python -m ensurepip --upgrade

Perintah ini akan menginstal atau memperbarui pip ke versi terbaru.

### 3. Instalasi Dependensi
Buka Command Prompt dan jalankan perintah berikut untuk menginstal semua library yang diperlukan:

pip install selenium webdriver-manager pandas colorama requests

Perintah ini akan menginstal:
- selenium: untuk otomatisasi browser
- webdriver-manager: untuk mengelola WebDriver Chrome
- pandas: untuk membaca dan memproses file Excel
- colorama: untuk output berwarna di console
- requests: untuk melakukan HTTP requests (digunakan untuk cek koneksi internet)

**Penting:** 
_Pastikan Google Chrome terinstal di komputer Anda. Jika belum, unduh dan instal dari https://www.google.com/chrome/_

### 4. Persiapan File Excel
1. Buat file Excel dengan nama "prabayar h2h.xlsx"
2. File harus memiliki kolom berikut (perhatikan penulisan yang tepat):
   - KATEGORY |OPERATOR |PRODUK ID |PRODUK |DETAIL |ZONA |MARKUP

Jadi Kolom pada excel diisi Judul kolom seperti diatas

3. Simpan file Excel di folder Downloads komputer Anda 

### 5. Mengunduh Script
1. Unduh file `prabayarh2h.py`
2. Simpan di lokasi yang mudah diakses (misalnya: Desktop atau Documents)

### 6. Konfigurasi Script
1. Buka file prabayarh2h.py menggunakan text editor (Notepad++ atau Visual Studio Code)
2. Cari dan ubah kredensial login:
email_input.send_keys("email_anda@example.com")  # Ganti dengan email login dashbord
password_input.send_keys("password_anda")        # Ganti dengan password login

## Cara Menjalankan Script

1. Buka Command Prompt
2. Navigasi ke folder tempat script disimpan:
cd path/to/script
Contoh: cd C:\Users\YourName\Desktop atau mislanya

3. Jalankan script:
python prabayarh2h.py

4. Proses Otomatis:
   - Script akan membuka browser Chrome
   - Login otomatis akan dilakukan
   - Tunggu 15 detik untuk memasukkan OTP yang dikirim ke email yang kamu cantumkn pada secript
   - Setelah login berhasil, proses input data akan berjalan otomatis
   - Jangan tutup browser selama proses berjalan

## Catatan Keamanan

### Peringatan Keamanan Browser
Anda mungkin akan melihat peringatan keamanan karena situs menggunakan HTTP (bukan HTTPS). Ini normal dan Anda dapat:
1. Klik "Continue to site" atau "Lanjutkan ke situs"
2. Gunakan script ini hanya pada jaringan yang terpercaya

### Praktik Keamanan
- Jangan bagikan kredensial login Anda kepada siapapun
- Gunakan script ini hanya dari lokasi yang aman
- Selalu logout setelah selesai menggunakan sistem

## Troubleshooting

### Masalah Umum dan Solusi

1. **Script tidak berjalan:**
   - Pastikan Python terinstal dengan benar
   - Pastikan semua dependensi terinstal
   - Coba buka Command Prompt sebagai Administrator

2. **File Excel tidak terbaca:**
   - Pastikan nama file tepat: "prabayar h2h.xlsx"
   - Pastikan format kolom sesuai
   - Periksa lokasi file di folder Downloads

3. **Browser tidak terbuka:**
   - Pastikan Chrome terinstal
   - Update Chrome ke versi terbaru
   - Coba install ulang webdriver-manager:
pip install --upgrade webdriver-manager

4. **Koneksi Terputus:**
   - Script akan otomatis menunggu sampai koneksi kembali
   - Pastikan koneksi internet stabil
   - Jangan tutup browser selama proses berjalan

## Pemeliharaan dan Update

- Periksa dan update dependensi secara berkala:
pip install --upgrade selenium webdriver-manager pandas colorama requests
- Backup file Excel Anda secara regular
- Pantau perubahan pada website target yang mungkin mempengaruhi script

## Format Data Excel

File Excel Anda harus memiliki nama "prabayar h2h.xlsx" dan berisi kolom-kolom berikut:

1. KATEGORY
2. OPERATOR
3. PRODUK ID
4. PRODUK
5. DETAIL
6. ZONA
7. MARKUP

Pastikan untuk menggunakan nama kolom yang tepat seperti di atas.

## Fitur Script

1. **Otomatisasi Penuh:**
   - Login otomatis
   - Input data otomatis
   - Penanganan OTP
   - Validasi data

2. **Penanganan Kesalahan:**
   - Deteksi koneksi terputus
   - Retry otomatis
   - Lanjut ke data berikutnya jika terjadi error

3. **Keamanan:**
   - Penanganan timeout
   - Validasi input
   - Penanganan session

4. **Monitoring:**
   - Status proses real-time
   - Pesan error yang jelas
   - Log aktivitas

## Tips Penggunaan

1. **Persiapan:**
   - Pastikan data Excel sudah benar dan lengkap
   - Backup data sebelum menjalankan script
   - Test dengan data sedikit terlebih dahulu

2. **Selama Proses:**
   - Jangan intervensi proses otomatis
   - Biarkan browser tetap terbuka
   - Monitor proses melalui console

3. **Penanganan Error:**
   - Catat error yang muncul
   - Periksa log untuk troubleshooting
   - Laporkan bug yang ditemukan

## Dukungan dan Bantuan

- Telegram: https://t.me/kangujang08

## Disclaimer

- Script ini dibuat untuk memudahkan input data produk h2h serpul
- Gunakan dengan bijak dan sesuai ketentuan yang berlaku
- Tidak untuk diperjualbelikan
- Anda dapat menggunakan script ini untuk jasa input produk

## Lisensi

MIT License - Silakan gunakan dan modifikasi sesuai kebutuhan dengan mencantumkan kredit kepada pembuat asli.

## Kontribusi

Jika Anda ingin berkontribusi pada pengembangan script ini:
1. Fork repository
2. Buat branch untuk fitur baru
3. Submit pull request
4. Diskusikan perubahan yang diusulkan

## Update Log

### Versi 1.0.0
- Rilis pertama
- Fitur dasar otomatisasi
- Penanganan error dasar

### Versi 1.1.0
- Penambahan penanganan koneksi terputus
- Perbaikan format input produk
- Peningkatan stabilitas

## Penutup

Script ini dikembangkan untuk membantu proses input data. Gunakan dengan bijak dan laporkan jika menemukan masalah atau bug. Terima kasih telah menggunakan script ini!
