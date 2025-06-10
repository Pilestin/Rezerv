from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # .env dosyasını yükle


# GITHUB_USERNAME ve GITHUB_PASSWORD değerlerini .env dosyasından al
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_PASSWORD = os.getenv("GITHUB_PASSWORD")


# Kayıtları saklayacağımız klasör
SAVE_DIR = "code_time_screenshots"
os.makedirs(SAVE_DIR, exist_ok=True)

# Bugünün tarihi
today = datetime.date.today()

# Son 90 günü haftalara çevir (yaklaşık 13 hafta)
weeks_to_fetch = 13

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

# 📋 Kullanıcıdan onay bekle
input("Giriş işlemi tamamlandı. Devam etmek için Enter'a basınız...")

# 5️⃣ Son 13 hafta boyunca sayfaları indir
for i in range(weeks_to_fetch):
    # İlgili haftanın tarihini hesapla (bugünden geriye doğru)
    target_date = today - datetime.timedelta(weeks=i)
    
    # Haftanın başlangıç tarihini hesapla (Pazartesi)
    days_since_monday = target_date.weekday()
    week_start = target_date - datetime.timedelta(days=days_since_monday)
    formatted_date = week_start.strftime("%Y-%m-%d")

    # URL'yi oluştur
    url = base_url.format(formatted_date)

    # 6️⃣ Sayfaya git
    driver.get(url)
    time.sleep(3)  # Sayfanın tam yüklenmesini bekle

    # 7️⃣ Ekran görüntüsü al ve kaydet
    screenshot_path = os.path.join(SAVE_DIR, f"code_time_week_{formatted_date}.png")
    driver.save_screenshot(screenshot_path)

    print(f"[+] {formatted_date} haftası ekran görüntüsü alındı.")

# İşlem bitti, tarayıcıyı kapat
driver.quit()

print("Tüm işlemler tamamlandı.")
