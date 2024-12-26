import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time

# Kullanıcı bilgilerini JSON dosyasından oku
def load_credentials():
    # Eğer dosya yoksa, kullanıcıdan bilgileri al ve dosyayı oluştur
    if not os.path.exists("user_info.json"):
        print("Kullanıcı bilgileri bulunamadı. Lütfen bilgilerinizi giriniz.")
        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")
        credentials = {"username": username, "password": password}
        with open("user_info.json", "w") as file:
            json.dump(credentials, file)
        print("Bilgileriniz user_info.json dosyasına kaydedildi.")
        return credentials
    else:
        # Dosya mevcutsa içeriği oku
        with open("user_info.json", "r") as file:
            return json.load(file)


def login_to_wifi():
    credentials = load_credentials()
    USERNAME = credentials["username"]
    PASSWORD = credentials["password"]
    print("Kullanıcı bilgileriniz: ", USERNAME, PASSWORD)

    # ChromeDriver ayarları
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Tarayıcıyı arka planda çalıştırmak için (isteğe bağlı)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")


    driver = webdriver.Chrome()

    try:
        # ESOGU-WIFI giriş sayfasına git
        driver.get("https://netyetki.ogu.edu.tr/")
        time.sleep(2)  # Sayfanın yüklenmesini bekleyin

        # Kullanıcı adı kutusunu bul ve doldur
        username_field = driver.find_element(By.ID, "inputUser")
        username_field.send_keys(USERNAME)

        # Şifre kutusunu bul ve doldur
        password_field = driver.find_element(By.ID, "inputPassword")
        password_field.send_keys(PASSWORD)

        # Kullanım sözleşmesi kutusunu işaretle
        agreement_checkbox = driver.find_element(By.NAME, "chkSozlesme")
        agreement_checkbox.click()

        # Giriş yap butonuna tıkla
        login_button = driver.find_element(By.NAME, "submitGiris")
        login_button.click()

        # İşlemin tamamlanmasını bekle
        time.sleep(5)

        print("Giriş başarılı!")
    except Exception as e:
        print(f"Giriş işlemi sırasında bir hata oluştu: {e}")
    finally:
        # Tarayıcıyı kapat
        driver.quit()

if __name__ == "__main__":
    login_to_wifi()
