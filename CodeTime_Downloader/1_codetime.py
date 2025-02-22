from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
import os

# Kullanıcı bilgileri (BURAYI KENDİ BİLGİLERİNLE DOLDUR)
GITHUB_USERNAME = "yourusername"
GITHUB_PASSWORD = "yourpassword"

# Kayıtları saklayacağımız klasör
SAVE_DIR = "code_time_html"
os.makedirs(SAVE_DIR, exist_ok=True)

# Başlangıç tarihi
start_date = datetime.date(2025, 2, 17)

# Kaç hafta geriye gideceğimiz
weeks_to_fetch = 12  

# Temel URL
base_url = "https://app.software.com/code_time?week_of={}"

# Selenium ile tarayıcı başlat
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Arka planda çalışması için
# options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 1️⃣ Code Time giriş sayfasına git
driver.get("https://app.software.com/code_time")

time.sleep(2)  # Sayfanın yüklenmesini bekle

# 2️⃣ GitHub ile giriş yap butonuna bas
github_login_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[2]/div[1]/form/button")
github_login_button.click()

time.sleep(2)  # GitHub giriş sayfasının açılmasını bekle

# 3️⃣ GitHub giriş bilgilerini gir
username_input = driver.find_element(By.ID, "login_field")
password_input = driver.find_element(By.ID, "password")

username_input.send_keys(GITHUB_USERNAME)
password_input.send_keys(GITHUB_PASSWORD)

# 4️⃣ Giriş yap butonuna bas
password_input.send_keys(Keys.RETURN)

time.sleep(5)  # Giriş işleminin tamamlanmasını bekle

# 5️⃣ 12 hafta boyunca sayfaları indir
for i in range(weeks_to_fetch):
    # İlgili haftanın tarihini hesapla
    week_date = start_date - datetime.timedelta(weeks=i)
    formatted_date = week_date.strftime("%Y-%m-%d")

    # URL'yi oluştur
    url = base_url.format(formatted_date)

    # 6️⃣ Sayfaya git
    driver.get(url)
    time.sleep(3)  # Sayfanın tam yüklenmesini bekle

    # 7️⃣ HTML sayfasını kaydet
    file_path = os.path.join(SAVE_DIR, f"code_time_{formatted_date}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    print(f"[+] {formatted_date} sayfası indirildi.")

# İşlem bitti, tarayıcıyı kapat
driver.quit()

print("Tüm işlemler tamamlandı.")
