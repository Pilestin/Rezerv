# CodeTime Screenshot Downloader 📊

VSCode içerisinde **"Code Time"** eklentisi ile ne kadar süre aktif kodlama yaptığınızı, çalışma saatleri dışındaki mesailerinizi ve birçok istatistiği görebilirsiniz. Ayrıca, **tarayıcı üzerinden hesabınıza giriş yaparak** detaylı grafikler ve haftalık raporlarla karşılaşabilirsiniz.

Ancak, **Code Time platformu bu verileri dışa aktarmaya izin vermediği için**, bu verileri almak ve daha sonra analiz edebilmek amacıyla bir otomasyon geliştirdik.

Bu script sayesinde:

✅ **Haftalık bazda tüm istatistiklerinizi ekran görüntüsü olarak kaydedebilirsiniz.**  
✅ **Otomatik olarak GitHub hesabınızla giriş yapar.**  
✅ **Son 90 günlük (13 haftalık) geçmiş verileri indirir.**  
✅ **Tüm verileri görsel olarak içeren bir "index.html" sayfası oluşturur.**  
✅ **Responsive Bootstrap tasarımı ile mobil uyumlu arayüz.**  
✅ **Modal pencereler ile büyütülmüş görüntü desteği.**

## **🔧 Kurulum**

Sistemde gerekli kütüphanelerin yüklü olduğundan emin olun:

```sh
pip install selenium webdriver-manager python-dotenv
```

### **🔑 Ortam Dosyası (.env) Kurulumu**

Güvenlik için GitHub bilgilerinizi `.env` dosyasında saklayın:

```env
GITHUB_USERNAME=yourusername
GITHUB_PASSWORD=yourpassword
```

## **📌 Kullanım**

### **1️⃣ CodeTime Verilerini Ekran Görüntüsü Olarak İndir**
`1_codetime.py` dosyası, **GitHub hesabınızla otomatik giriş yaparak** haftalık istatistiklerin ekran görüntüsünü alır.

```sh
python 1_codetime.py
```

**📌 Ne yapar?**
- **GitHub ile otomatik giriş yapar.**
- **Kullanıcıdan onay bekler (2FA veya diğer doğrulamalar için).**
- **Son 13 haftaya ait haftalık istatistiklerin ekran görüntüsünü alır.**
- **Her hafta için bir `.png` dosyası kaydeder.**
- **Dosya adları `code_time_week_YYYY-MM-DD.png` formatında olur.**
- **Otomatik olarak HTML index sayfasını oluşturur.**

### **2️⃣ Manuel HTML İndex Oluşturma (Opsiyonel)**
Eğer sadece HTML sayfasını yeniden oluşturmak istiyorsanız:

```sh
python generate_index.py
```

**📌 Ne yapar?**
- **Tüm indirilen screenshot'ları tarar.**
- **Her hafta için görsel kart içeren responsive sayfa oluşturur.**
- **Haftalık tarihleri düzgün formatta gösterir.**
- **Modal pencereler ile büyütülmüş görüntü desteği.**
- **Özet istatistikler ile toplam hafta sayısı gösterir.**

---

## **📂 Dosya Yapısı**
```sh
├── 1_codetime.py              # Ana script - GitHub giriş ve screenshot alma
├── generate_index.py          # HTML index sayfası oluşturucu
├── .env                       # GitHub giriş bilgileri (güvenli)
├── index.html                 # Ana sayfa - haftalık görsel raporlar
└── code_time_screenshots/     # Haftalık ekran görüntüleri klasörü
    ├── code_time_week_2024-01-01.png
    ├── code_time_week_2024-01-08.png
    └── ...
```

---

## **🎯 Özellikler**

### **🔐 Güvenlik**
- `.env` dosyası ile güvenli kimlik bilgisi yönetimi
- Kullanıcı onayı ile manuel kontrol imkanı

### **📱 Modern Arayüz**
- Bootstrap 5 ile responsive tasarım
- Modal pencereler ile büyütülmüş görüntü
- Gradient renkler ve modern kartlar
- Mobil uyumlu tasarım

### **📊 Veri Yönetimi**
- Haftalık bazda organize edilmiş veriler
- Tarih sıralı görüntüleme (en yeni önce)
- Özet istatistikler ve veri sayısı
- PNG formatında yüksek kaliteli görüntüler

### **⚡ Performans**
- Selenium ile otomatik tarayıcı kontrolü
- 13 haftalık veri toplama (90 gün kapsamı)
- Hata kontrolü ve güvenli dosya işlemleri

---

## **🚀 Kullanım Talimatları**

1. **Depoyu klonlayın ve gereksinimleri yükleyin**
2. **`.env` dosyasını oluşturun ve GitHub bilgilerinizi girin**
3. **`python 1_codetime.py` komutu ile veri toplama işlemini başlatın**
4. **Giriş tamamlandıktan sonra Enter'a basarak devam edin**
5. **İşlem tamamlandığında `index.html` dosyasını açın**
6. **Haftalık istatistiklerinizi görsel olarak inceleyin**

---

## **⚠️ Önemli Notlar**

- Script çalışırken tarayıcı penceresi açılacaktır
- 2FA aktif ise manual doğrulama gerekebilir
- Her hafta için yaklaşık 3 saniye bekleme süresi vardır
- Toplam işlem süresi yaklaşık 1-2 dakikadır

---

### **📩 Geri Bildirim**
Herhangi bir sorun yaşarsanız veya geliştirme öneriniz varsa, çekinmeden paylaşabilirsiniz! 🚀
