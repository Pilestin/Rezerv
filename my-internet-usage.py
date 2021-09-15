""" The file contains my internet usage data. 
    # file = open("C:\\Users\\Yasin\\Desktop\\yy.txt","r",encoding="utf-8")

2021 	5 (gün) 23 (saat) 25 (dakika) 	24,270 GB 	1,662 GB
2021 	32 (gün) 15 (saat) 27 (dakika) 	210,456 GB 	13,463 GB
2021 	31 (gün) 2 (saat) 2 (dakika) 	266,116 GB 	15,152 GB
2021 	29 (gün) 21 (saat) 22 (dakika) 	156,584 GB 	13,366 GB
2021 	28 (gün) 7 (saat) 11 (dakika) 	188,854 GB 	14,565 GB
2021 	29 (gün) 21 (saat) 31 (dakika) 	244,221 GB 	19,043 GB
2021 	32 (gün) 11 (saat) 6 (dakika) 	176,652 GB 	14,828 GB
2021 	27 (gün) 18 (saat) 43 (dakika) 	205,775 GB 	18,152 GB
2021 	30 (gün) 18 (saat) 22 (dakika) 	298,560 GB 	18,814 GB
2020 	23 (gün) 20 (saat) 48 (dakika) 	145,215 GB 	12,855 GB
2020 	6 (gün) 9 (saat) 12 (dakika) 	44,309 GB 	2,309 GB
2020 	29 (gün) 19 (saat) 36 (dakika) 	195,661 GB 	12,063 GB
2020 	30 (gün) 15 (saat) 19 (dakika) 	152,641 GB 	11,823 GB
2020 	29 (gün) 17 (saat) 29 (dakika) 	185,312 GB 	15,669 GB
2020 	31 (gün) 15 (saat) 59 (dakika) 	239,405 GB 	21,795 GB

"""

# 1 - listedeki download ksımındaki sayıları toplayan ve ortalamasını alan olan fonksiyon.
# 1 - The function that adds the numbers in the download section of the list and takes their average. 
# 2 - download kısmı liste içinde 7.indextedir.
# 2 - The download part is in the 7th index in the list. 
def avgOfDownload(liste):
    total = 0   # sum of the numbers
    l     = 0   # number of the lines 
    for line in liste:
        downNum = float(line[7].replace(",","."))
        total   = total + downNum
        l += 1
    average = total / l 
    return average

# 1 - listedeki upload kısmındaki sayıları toplayan ve ortalamasını alan fonksiyon.
# 1 - The function that adds the numbers in the upload part of the list and takes the average. 
# 2 - upload kısmındaki sayılar liste içinde 9. indextedir. 
# 2 - The upload part is in the 9th index in the list.
def avgOfUpload(list):
    total = 0  # sum of the numbers
    l     = 0  # number of the lines 
    for line in list:
        upNum = float(line[9].replace(",","."))
        total = total + upNum
        l += 1
    average = total / l 
    return average

# toplam download sayısını veren fonksiyon 
# Function that returns the number of downloads 
def sumOFDownload(liste):
    total = 0   # sum of the numbers 
    for line in liste:
        downNum = float(line[7].replace(",","."))
        total   = total + downNum

    return total

# toplam upload sayısnın veren fonksiyon
# Function that returns the number of uploads 
def sumOfUpload(liste):
    total = 0   # sum of the numbers 
    for line in liste:
        downNum = float(line[9].replace(",","."))
        total   = total + downNum
    
    return total

# 1 - txt dosyasından gelen sıralı ve düzgün yazıları okuma modunda açar.
# 1 - Opens sequential and neat texts from txt file in reading mode. 
# 2 - ardından bir listeye atar.
# 2 - then adds it to a list. 

def openFile(path):
    #with open("C:\\Users\\Yasin\\Desktop\\yy.txt","r",encoding="utf-8") as f:
   
    rezerv = [] # list
    with open(path , "r" , encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            rezerv.append(line.split())
    return rezerv
    


def start():
    # dosya uzantısı değişken olabilir.
    # watch out for the file path! 
    path   = "C:\\Users\\Yasin\\Desktop\\yy.txt"
    listem = openFile(path)
    
    print(f"""
        Bu zamana kadarki toplam indirme = {sumOFDownload(listem)} GB
        Bu zamana kadarki toplam yükleme = {sumOfUpload(listem)} GB

        Ortalama indirme = {avgOfDownload(listem)} GB
        Ortalama yükleme = {avgOfUpload(listem)} GB
    """)

def main(): 

    start()
 
main()

    