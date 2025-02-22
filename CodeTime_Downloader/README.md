# Code Time Downloader 🚀

VSCode içerisinde **"Code Time"** eklentisi ile ne kadar süre aktif kodlama yaptığınızı, çalışma saatleri dışındaki mesailerinizi ve birçok istatistiği görebilirsiniz. Ayrıca, **tarayıcı üzerinden hesabınıza giriş yaparak** detaylı grafikler ve haftalık raporlarla karşılaşabilirsiniz.

Ancak, **Code Time platformu bu verileri dışa aktarmaya izin vermediği için**, bu verileri almak ve daha sonra analiz edebilmek amacıyla bir otomasyon geliştirdik.

Bu script sayesinde:

✅ **Haftalık bazda tüm istatistiklerinizi HTML olarak kaydedebilirsiniz.**  
✅ **Otomatik olarak GitHub hesabınızla giriş yapar.**  
✅ **90 günlük (12 haftalık) geçmiş verileri indirir.**  
✅ **Tüm verileri içeren bir "index.html" sayfası oluşturur.**  
✅ **İlgili tarihlere tıklayarak detaylı raporları görebilirsiniz.**  


## **🔧 Kurulum**

Sistemde gerekli kütüphanelerin yüklü olduğundan emin olun. Eğer yüklü değilse, aşağıdaki komutları çalıştırarak yükleyebilirsiniz:

```sh
pip install selenium webdriver-manager requests

```


Giriş yapmak için github kullandığım için Selenium ile "github ile giriş yap" seçeneğini seçecek şekilde yaptım. İsterseniz kodu değiştirebilir veya kendi github bilgilerinizi kullanarak giriş yapabilirsiniz. 


## **📌 Kullanım**

### **1️⃣ Giriş Yaparak Code Time Verilerini İndir**
`1_codetime.py` dosyası, **GitHub hesabınızla otomatik giriş yaparak** ilgili HTML sayfalarını indirir.

**Not** : Kod içerisinde kendi github bilgilerinizi girin 
```python
GITHUB_USERNAME = "yourusername"
GITHUB_PASSWORD = "yourpassword"
```
Ardından çalıştırın

```sh
python  1_codetime.py
```

**📌 Ne yapar?**
- **GitHub ile otomatik giriş yapar.**
- **Son 12 haftaya ait haftalık istatistikleri çeker.**
- **Her hafta için bir `.html` dosyası kaydeder.**
- **Dosya adları `code_time_YYYY-MM-DD.html` formatında olur.**

### **2️⃣ Ana Sayfa (index.html) Oluştur**
İndirdiğimiz sayfalara kolayca erişebilmek için bir **ana sayfa (index.html) oluşturur.** Bunun için aşağıdaki komutu çalıştırın:

```sh
python 2_generate_homepage.py
```

**📌 Ne yapar?**
- **Tüm indirilen HTML dosyalarını tarar.**
- **Her hafta için bir satır içeren tabloyu oluşturur.**
- **Tablodaki tarihler haftalık formatta gösterilir (örn: `2024-12-02 - 2024-12-08`).**
- **Her sayfanın içine bir "Geri Dön" butonu ekler.**
- **Sonuçları `index.html` içine kaydeder.**

---

## **📂 Dosya Açıklamaları**
```sh
├── 1_codetime.py   # GitHub ile giriş yaparak Code Time verilerini indirir.
├── 2_generate_homepage.py     # Tüm HTML dosyalarından 'index.html' sayfasını oluşturur.
├── index.html            # Ana sayfa, buradan haftalık verilere erişebilirsiniz.
└── code_time_html/       # Haftalık verilerin kaydedildiği klasör.
```

---

## **🎯 Özellikler ve Geliştirmeler**
✔ **GitHub ile otomatik giriş yapma**  
✔ **Haftalık olarak tarihleri düzgün formatta listeleme**  
✔ **Verileri `.html` dosyaları olarak saklama**  
✔ **Kolay erişim için index.html oluşturma**  
✔ **Her rapor sayfasına "Geri Dön" butonu ekleme**  
✔ **Herhangi bir veri kaybı yaşamadan offline görüntüleme**  

---

### **📩 Geri Bildirim**
Eğer herhangi bir hata veya geliştirme önerin varsa, çekinmeden paylaşabilirsin! 😊

---
