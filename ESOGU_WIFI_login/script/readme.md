# ESOGÜ-WIFI Otomatik Giriş Scripti

Bu Python scripti, Eskişehir Osmangazi Üniversitesi'nin (ESOGÜ) **Wi-Fi ağına** otomatik olarak giriş yapmanızı sağlar. Kullanıcı bilgilerinizi yalnızca bir kez girerek bir `user_info.json` dosyasında kaydedebilirsiniz. Daha sonraki çalıştırmalarda bilgiler otomatik olarak bu dosyadan alınır.

---

## Özellikler
- **Otomatik giriş**: Kullanıcı adı ve şifreyi girip, kullanım sözleşmesini kabul ederek ESOGÜ-WIFI ağına giriş yapar.
- **Bilgi saklama**: Kullanıcı bilgileri `user_info.json` dosyasında saklanır, böylece tekrarlı giriş bilgisi girmenize gerek kalmaz.
- **Dinamik oluşturma**: Eğer `user_info.json` dosyası bulunmuyorsa, kullanıcıdan bilgiler istenir ve otomatik olarak oluşturulur.
- **Headless tarayıcı desteği**: Tarayıcıyı arka planda çalıştırmak için ayarlanabilir.

---

## Gereksinimler

Bu scriptin çalışması için aşağıdaki araçlar ve kütüphaneler gereklidir:

### 1. **Sistem Gereksinimleri**
- **Python**: 3.7 veya üzeri
- **Google Chrome**: Yüklü olmalıdır.
- **ChromeDriver**: Google Chrome sürümünüzle uyumlu olmalıdır. İndirme bağlantısı: [ChromeDriver](https://sites.google.com/chromium.org/driver/)

### 2. **Python Kütüphaneleri**
Aşağıdaki kütüphaneleri yüklemek için şu komutu çalıştırın:
```bash
pip install selenium, json