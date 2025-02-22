import os
import datetime

# HTML dosyalarının bulunduğu klasör
SAVE_DIR = "code_time_html"
INDEX_FILE = "index.html"

# Klasördeki tüm .html dosyalarını al ve tarihe göre sırala
html_files = sorted([f for f in os.listdir(SAVE_DIR) if f.endswith(".html")])

# HTML şablonu oluştur (index.html için)
html_content = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Code Time Raporları</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; padding: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
        th { background-color: #007bff; color: white; }
        a { text-decoration: none; color: #007bff; font-weight: bold; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h2>Code Time Haftalık Raporları</h2>
    <table>
        <tr>
            <th>Hafta</th>
            <th>İlgili Rapor</th>
        </tr>
"""

# Tüm dosyaları listeye ekleyelim (haftalık isimlendirme ekleniyor)
for file in html_files:
    date_str = file.replace("code_time_", "").replace(".html", "")  # Tarih kısmını al
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")  # Tarihi nesneye çevir

    # Haftanın başlangıcı ve bitişini hesapla
    start_of_week = (date_obj - datetime.timedelta(days=date_obj.weekday())).strftime("%Y-%m-%d")
    end_of_week = (date_obj + datetime.timedelta(days=(6 - date_obj.weekday()))).strftime("%Y-%m-%d")

    week_label = f"{start_of_week} - {end_of_week}"
    file_path = os.path.join(SAVE_DIR, file)

    html_content += f"        <tr><td>{week_label}</td><td><a href='{file_path}' target='_blank'>Görüntüle</a></td></tr>\n"

# HTML kapanış tag'ları
html_content += """    </table>
</body>
</html>"""

# index.html dosyasını yaz
with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

print("[+] index.html başarıyla oluşturuldu.")

# 🌟 HTML SAYFALARINA "GERİ DÖN" BUTONU EKLEYELİM 🌟
for file in html_files:
    file_path = os.path.join(SAVE_DIR, file)

    # Mevcut HTML içeriğini oku
    with open(file_path, "r", encoding="utf-8") as f:
        old_content = f.read()

    # Yeni içerik (başına "Geri Dön" butonu ekleyerek)
    new_content = f"""<a href="../index.html" style="display: block; margin: 10px 0; padding: 10px; background-color: #007bff; color: white; text-align: center; width: 150px; border-radius: 5px; text-decoration: none;">
⬅ Geri Dön
</a>
""" + old_content

    # Güncellenmiş içeriği dosyaya yaz
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

print("[+] Tüm HTML sayfalarına 'Geri Dön' butonu eklendi.")
