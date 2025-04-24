from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random 

# def sayfa_kaydir(driver, total_scrolls: int, kaydirma_suresi:int):
#     """Sayfayı yavaş yavaş aşağı kaydırır."""

#     scroll_pause_time = kaydirma_suresi / total_scrolls
    
#     for i in range(total_scrolls):
#         driver.execute_script("window.scrollBy(0, document.body.scrollHeight / 20);")
#         time.sleep(scroll_pause_time)

import time

def yavas_sonuna_kadar_kaydir(driver, kaydirma_adimi=300, bekleme_suresi=0.5, max_scroll=100):
    """Sayfayı yavaş yavaş sonuna kadar kaydırır."""
    prev_scroll_y = -1

    for i in range(max_scroll):
        driver.execute_script(f"window.scrollBy(0, {kaydirma_adimi});")
        time.sleep(bekleme_suresi)

        # Mevcut scroll konumu
        current_scroll_y = driver.execute_script("return window.pageYOffset + window.innerHeight")
        total_height = driver.execute_script("return document.body.scrollHeight")

        # Sayfa sonuna ulaşıldı mı?
        if current_scroll_y >= total_height:
            print(f"[✓] Sayfa sonuna ulaşıldı ({i+1} adımda).")
            break




def selenium_tekrarli_scroll(url, tekrar_sayisi):
    import random

    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
        "Mozilla/5.0 (X11; Linux x86_64)...",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)...",
        # Daha fazla eklersin
    ]

    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={random.choice(USER_AGENTS)}")
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    options.add_argument(f"--window-size={random.randint(1024, 1920)},{random.randint(720, 1080)}")
    options.add_argument("--incognito")
    
    for i in range(tekrar_sayisi):
        total_scrolls = random.randint(5, 25)  # Kaydırma sayısını rastgele belirle
        kaydirma_suresi = random.randint(15, 90)  # Kaydırma süresini rastgele belirle
        print("===============================")
        print(f"TUR: {i + 1}")
        print(f"Kaydırma Sayısı: {total_scrolls}")
        print(f"Kaydırma Süresi: {kaydirma_suresi} saniye")
        print("===================================")
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        time.sleep(3)  # Sayfa yüklenme süresi
        # sayfa_kaydir(driver, total_scrolls, kaydirma_suresi)
        bekleme_suresi = kaydirma_suresi / total_scrolls
        max_deneme = total_scrolls * 2
        yavas_sonuna_kadar_kaydir(driver)
        try:
            driver.quit()
        except OSError as e:
            print("Tarayıcı zaten kapanmış.")
        # Sekmeyi kapat

        # Yeni bir pencere açmak için yeni driver oluştur
        # Alternatif olarak sekme yerine pencere açmak istersen aşağıdaki gibi yapabilirsin:
        # driver.execute_script("window.open('');")
        # driver.switch_to.window(driver.window_handles[-1])

link = "https://www.mdpi.com/2076-3417/15/9/4703"

selenium_tekrarli_scroll(link, tekrar_sayisi=30)
