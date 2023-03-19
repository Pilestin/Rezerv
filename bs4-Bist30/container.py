import requests
from bs4 import BeautifulSoup as BS


web_site = requests.get('https://borsa.doviz.com/hisseler').content
soup = BS(web_site,'html.parser')

bist30 = [] 
table = soup.find("table",{"id": "stocks"})

# aslında direk ilgili div verilebilir. Ama her satırı alıp, satırın özeline ineceğim
rows   = table.find_all("div",{"class": "currency-details"}) # Sonuçlar liste şeklinde gelecek    resultSet yapısında gelecek. Yani dizi gibi erişebilirim

# çektiğimiz bilginin ilk elemanı şu şekilde : 
# <div class="currency-details">
# <div>ISCTR</div>
# <div class="cname">IS BANKASI (C)</div>
# </div>
# 
# Bize ISCTR kısmı lazım. yani içerideki ilk divin TEXT kısmı. Bunu bir döngünün ilk elemanının text'i şeklinde yapacağız.

for row in rows:
    
    # burada her bir satır gelecek. Bu satırı sırasıyla text'ini alıcaz. Ardından da boşlukları atacağız.
    hisse_bilgisi = row.text.split()
    # Sonuçta şunun gibi gözükecek
    # print(row.text.split())
    # ['ISCTR', 'IS', 'BANKASI', '(C)']
    # . . . 
    # Ve bu bilgilerin ilkini alacağız 
    hisse_kodu    = hisse_bilgisi[0]
    
    # bu bilgileri ayrıca bist30 listesine atıcam 
    bist30.append(hisse_kodu)
    
bist30 = bist30[:30]
print(bist30)