#!/bin/bash

# Wi-Fi ağına bağlanma fonksiyonu
connect_to_wifi() {
    SSID="ESOGU-WIFI"
    PASSWORD="esogubim"

    # Mevcut bağlantıyı kontrol et
    CURRENT_SSID=$(nmcli -t -f active,ssid dev wifi | grep '^yes' | cut -d':' -f2)
    if [ "$CURRENT_SSID" == "$SSID" ]; then
        echo "Zaten $SSID ağına bağlısınız."
        return 0
    fi

    # Ağa bağlan
    echo "Wi-Fi ağına bağlanılıyor: $SSID"
    nmcli dev wifi connect "$SSID" password "$PASSWORD"
    if [ $? -eq 0 ]; then
        echo "$SSID ağına başarıyla bağlanıldı."
        return 0
    else
        echo "$SSID ağına bağlanılamadı."
        return 1
    fi
}

# ESOGU-WIFI giriş işlemi
login_to_wifi() {
    USERNAME="kullanici_adi"  # Kullanıcı adınızı girin
    PASSWORD="sifre"          # Şifrenizi girin

    LOGIN_URL="https://netyetki.ogu.edu.tr/"

    echo "Giriş yapılıyor..."
    curl -X POST "$LOGIN_URL" \
        -d "inputUser=$USERNAME&inputPassword=$PASSWORD&chkSozlesme=Onay" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -c cookies.txt \
        -L

    if [ $? -eq 0 ]; then
        echo "Giriş başarılı!"
    else
        echo "Giriş başarısız oldu!"
    fi
}

# Wi-Fi bağlantısını kontrol et ve bağlan
if connect_to_wifi; then
    # Giriş işlemini başlat
    login_to_wifi
else
    echo "Wi-Fi bağlantısı başarısız oldu, giriş yapılamadı."
fi
