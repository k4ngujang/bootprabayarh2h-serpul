# Script auto input produk prabayar H2H Serpul.co.id

Script ini adalah alat otomatisasi untuk menginput data produk prabayar h2h serpul menggunakan Python dan Selenium.

## Persyaratan Sistem

- Python 3.7 atau lebih baru
- Google Chrome browser

## Panduan Instalasi

### 1. Instalasi Python

1. Kunjungi https://www.python.org/downloads/
2. Unduh versi Python terbaru untuk sistem operasi Anda
3. Jalankan installer dan ikuti petunjuk instalasi
4. Pastikan untuk mencentang opsi "Add Python to PATH" selama instalasi

### 2. Instalasi pip (Python package manager)

pip biasanya sudah terinstal bersama dengan Python. Untuk memastikan, buka command prompt atau terminal dan ketik:

pip --version

Jika pip belum terinstal, ikuti panduan instalasi di https://pip.pypa.io/en/stable/installation/

### 3. Instalasi Dependensi

Buka command prompt atau terminal, navigasi ke direktori tempat Anda menyimpan script, lalu jalankan perintah berikut:

pip install selenium webdriver-manager pandas colorama requests

## Cara Penggunaan

1. Unduh atau clone repository ini ke komputer Anda
2. Pastikan file Excel "prabayar h2h.xlsx" berada di folder Downloads atau folder yang mudah dicari
3. Buka file `prabayarh2h.py` dan sesuaikan email dan password login jika diperlukan
4. Buka command prompt atau terminal, navigasi ke direktori tempat script disimpan
5. Jalankan script dengan perintah:

prabayarh2h.py

6. Script akan mulai berjalan. Ikuti instruksi yang muncul di layar
7. Saat diminta memasukkan OTP, masukkan OTP yang Anda terima melalui email
8. Script akan melanjutkan proses input data secara otomatis
9. Setelah selesai, tekan Enter untuk menutup browser

## Catatan Penting

- Pastikan koneksi internet Anda stabil selama script berjalan
- Jangan menutup browser Chrome yang dibuka oleh script
- Jika terjadi error, script akan mencoba melanjutkan ke data berikutnya
- Pastikan format data dalam file Excel sesuai dengan yang diharapkan oleh script

## Troubleshooting

Jika Anda mengalami masalah:

1. Pastikan semua dependensi terinstal dengan benar
2. Periksa apakah Chrome browser Anda up-to-date
3. Pastikan file Excel berada di lokasi yang benar dan formatnya sesuai
4. Jika masalah persists, buat issue baru di repository GitHub ini


## Penjelasan Kode

Script `prabayarh2h.py` terdiri dari beberapa bagian utama:

1. Import library yang diperlukan
2. Inisialisasi colorama untuk output berwarna
3. Definisi fungsi-fungsi utilitas (print berwarna, pengecekan koneksi internet, dll.)
4. Inisialisasi WebDriver untuk Chrome
5. Proses login ke situs Qiosalifapay
6. Membaca data dari file Excel
7. Loop untuk memproses setiap baris data dan menginputkannya ke situs
8. Penanganan error dan penutupan browser

## Kustomisasi

Anda dapat menyesuaikan beberapa parameter dalam script:

- Ubah path file Excel jika lokasi berbeda
- Sesuaikan selector CSS atau XPath jika struktur situs berubah
- Tambahkan field tambahan jika diperlukan

## Keamanan

- Script ini menyimpan kredensial login dalam bentuk plaintext. Pastikan untuk tidak membagikan script yang berisi informasi sensitif kepada siapapun
- Gunakan variabel lingkungan atau file konfigurasi terpisah untuk menyimpan kredensial jika diperlukan

## Pembaruan dan Pemeliharaan

- Periksa secara berkala apakah ada pembaruan pada library yang digunakan
- Uji script secara reguler untuk memastikan kompatibilitas dengan perubahan pada situs Qiosalifapay

## Dukungan

Jika Anda memerlukan bantuan lebih lanjut atau memiliki pertanyaan, silakan buat bisa hubungi telegram https://t.me/kangujang08

## Disclaimer

Script ini dibuat untuk tujuan otomatisasi dan efisiensi. Gunakan dengan bijak dan tidak untuk diperjual belikan namun anda bisa untuk membuka jasa input produk.
