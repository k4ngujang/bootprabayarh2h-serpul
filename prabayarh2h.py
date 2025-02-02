from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import colorama
from colorama import Fore, Style
import os
import sys
import pandas as pd
from selenium.webdriver.common.keys import Keys
import requests

# Inisialisasi colorama untuk warna teks di terminal
colorama.init()

# Variabel untuk mengecek status koneksi internet
connection_was_lost = False

# Fungsi untuk mencetak teks dengan warna hijau
def print_green(text):
    """
    Fungsi ini digunakan untuk mencetak teks dengan warna hijau di terminal
    dan memastikan teks langsung ditampilkan tanpa buffer
    """
    print(Fore.GREEN + text + Style.RESET_ALL)
    sys.stdout.flush()

# Fungsi untuk mencetak teks dengan warna merah
def print_red(text):
    """
    Fungsi ini digunakan untuk mencetak teks dengan warna merah di terminal
    dan memastikan teks langsung ditampilkan tanpa buffer
    """
    print(Fore.RED + text + Style.RESET_ALL)
    sys.stdout.flush()

# Fungsi untuk menekan output yang tidak diinginkan
def suppress_output(func):
    """
    Fungsi ini digunakan untuk menyembunyikan output yang tidak diinginkan
    saat menginisialisasi webdriver
    """
    def wrapper(*args, **kwargs):
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        try:
            return func(*args, **kwargs)
        finally:
            sys.stdout = original_stdout
            sys.stderr = original_stderr
    return wrapper

# Fungsi untuk membersihkan input field
def clear_input(element):
    """
    Fungsi ini digunakan untuk membersihkan isi dari input field
    dengan cara memilih semua teks (Ctrl+A) dan menghapusnya
    """
    element.send_keys(Keys.CONTROL + "a")  # Pilih semua teks
    element.send_keys(Keys.DELETE)         # Hapus teks yang dipilih

# Fungsi untuk menginisialisasi driver Chrome
@suppress_output
def initialize_driver():
    """
    Fungsi ini digunakan untuk menginisialisasi Chrome WebDriver
    dengan menyembunyikan log yang tidak penting
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Fungsi untuk memilih opsi dalam dropdown
def wait_and_select_option(driver, select_element, value):
    """
    Fungsi ini digunakan untuk memilih opsi dalam dropdown dengan menunggu
    sampai opsi tersedia dan mencoba metode alternatif jika cara normal gagal
    """
    try:
        # Tunggu sampai opsi tersedia
        WebDriverWait(driver, 10).until(
            lambda d: len([opt for opt in select_element.options if opt.get_attribute('value') == str(value)]) > 0
        )
        select_element.select_by_value(str(value))
        return True
    except Exception as e:
        print_green(f"Gagal memilih option dengan value {value}. Mencoba metode alternatif...")
        try:
            # Coba metode JavaScript jika cara normal gagal
            driver.execute_script(
                f"arguments[0].value = '{value}'; arguments[0].dispatchEvent(new Event('change'))",
                select_element.wrapped_element
            )
            return True
        except:
            print_green(f"Tidak dapat memilih option dengan value {value}")
            return False

# Fungsi untuk mengecek koneksi internet
def check_internet_connection():
    """
    Fungsi ini digunakan untuk mengecek apakah ada koneksi internet
    dengan mencoba mengakses google.com
    """
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Fungsi untuk menunggu koneksi internet
def wait_for_internet_connection():
    """
    Fungsi ini digunakan untuk menunggu sampai koneksi internet tersedia kembali
    dan menampilkan pesan status koneksi
    """
    global connection_was_lost
    while not check_internet_connection():
        connection_was_lost = True
        print_red("Koneksi internet terputus. Proses dijeda.")
        time.sleep(5)
    if connection_was_lost:
        print_green("Koneksi terhubung kembali. Proses akan dilanjutkan...")
        connection_was_lost = False

# Program Utama
try:
    # Inisialisasi driver
    print_green("Mohon tunggu sedang diproses...")
    driver = initialize_driver()

    # Proses login
    driver.get("https://domainanda.serpul.co.id/login")
    print_green("Script sedang berjalan....")

    # Input email
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    print_green("Sedang proses login....")
    email_input.send_keys("Masukan alamat email disini")

    # Pilih metode pengiriman OTP
    select_sender = Select(driver.find_element(By.NAME, "channel_sender"))
    select_sender.select_by_value("EMAIL")

    # Klik tombol kirim OTP
    kirim_otp_button = driver.find_element(By.ID, "btn-request-otp")
    kirim_otp_button.click()

    # Input password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys("masukan password login disini")

    # Jeda untuk input OTP
    print_green("Script sedang jeda selama 15 detik")
    time.sleep(15)
    print_green("Jeda telah selesai, Lanjut ke step selanjutnya...")

    # Klik tombol masuk
    masuk_button = driver.find_element(By.ID, "btn-login")
    masuk_button.click()

    print_green("Sedang proses....")
    time.sleep(5)

    # Navigasi ke halaman create produk
    driver.get("https://domainanda.serpul.co.id/product/prabayar/product/create")
    print_green("Sedang proses Create produk prabayar H2H serpul.....")

    # Baca file Excel
    excel_path = os.path.join(os.path.expanduser("~"), "Downloads", "prabayar h2h.xlsx")
    df = pd.read_excel(excel_path, dtype={'PRODUK': str})  # Baca kolom PRODUK sebagai string
    print_green(f"Membaca {len(df)} data dari Excel....")

    # Proses setiap baris data
    for index, row in df.iterrows():
        try:
            print_green(f"Memproses data ke-{index + 1}....")
            wait_for_internet_connection()

            # Proses pemilihan kategori
            print_green("Memilih kategori...")
            category_select_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "prabayar_category_id"))
            )
            category_select = Select(category_select_element)
            if not wait_and_select_option(driver, category_select, int(row['KATEGORY'])):
                raise Exception(f"Kategori dengan value {row['KATEGORY']} tidak ditemukan")

            # Proses pemilihan operator
            print_green("Memilih operator...")
            time.sleep(2)
            operator_select_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "prabayar_operator_id"))
            )
            operator_select = Select(operator_select_element)
            if not wait_and_select_option(driver, operator_select, int(row['OPERATOR'])):
                raise Exception(f"Operator dengan value {row['OPERATOR']} tidak ditemukan")

            # Input Product ID
            print_green("Mengisi Product ID...")
            produk_id_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control.text-uppercase"))
            )
            clear_input(produk_id_input)
            produk_id_input.send_keys(str(row['PRODUK ID']))

            # Input Product Name dengan format angka yang benar
            print_green("Mengisi Product Name...")
            product_name_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control.text-capitalize"))
            )
            clear_input(product_name_input)
            product_name = str(row['PRODUK']).strip()
            if product_name.replace('.', '').isdigit():
                product_name = "{:,.0f}".format(float(product_name.replace(',', '').replace('.', ''))).replace(',', '.')
            product_name_input.send_keys(product_name)

            # Input Detail
            print_green("Mengisi Detail...")
            detail_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.form-control"))
            )
            clear_input(detail_input)
            if pd.notna(row['DETAIL']):
                detail_input.send_keys(str(row['DETAIL']))

            # Input Zona
            print_green("Mengisi Zona...")
            zona_inputs = driver.find_elements(By.CSS_SELECTOR, "textarea.form-control")
            if len(zona_inputs) > 1:
                clear_input(zona_inputs[1])
                if pd.notna(row['ZONA']):
                    zona_inputs[1].send_keys(str(row['ZONA']))

            # Input Markup
            print_green("Mengisi Markup...")
            markup_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[oninput*='replace']"))
            )
            clear_input(markup_input)
            if pd.notna(row['MARKUP']):
                markup_input.send_keys(str(int(row['MARKUP'])))

            # Proses penyimpanan data
            print_green("Menyimpan data...")
            simpan_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary.btn-block.btn-lg"))
            )
            driver.execute_script("arguments[0].scrollIntoView(true);", simpan_button)
            time.sleep(1)
            simpan_button.click()

            # Konfirmasi penyimpanan
            ok_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.swal2-confirm"))
            )
            ok_button.click()
            
            print_green(f"Data ke-{index + 1} berhasil disimpan!")
            time.sleep(2)

        except Exception as e:
            print_red(f"Terjadi kesalahan pada data ke-{index + 1}: {str(e)}")
            print_green("Melanjutkan ke data berikutnya...")
            continue

    print_green("Semua data telah selesai diproses. Tekan Enter untuk menutup browser.")
    input()

except Exception as e:
    print_red(f"Terjadi kesalahan: {str(e)}")
    print_green("Tekan Enter untuk menutup browser.")
    input()

finally:
    driver.quit()
