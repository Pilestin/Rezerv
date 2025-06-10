import os
import datetime
from collections import defaultdict

def generate_html_index():
    # Screenshots klasörü
    SCREENSHOTS_DIR = "code_time_screenshots"
    
    # Dosyaları tarih sırasına göre grupla
    weeks_data = defaultdict(list)
    
    if os.path.exists(SCREENSHOTS_DIR):
        for filename in os.listdir(SCREENSHOTS_DIR):
            if filename.endswith('.png') and 'code_time_week_' in filename:
                # Dosya adından tarihi çıkar
                date_str = filename.replace('code_time_week_', '').replace('.png', '')
                try:
                    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                    weeks_data[date_str] = {
                        'date': date_obj,
                        'filename': filename,
                        'week_start': date_obj,
                        'week_end': date_obj + datetime.timedelta(days=6)
                    }
                except ValueError:
                    continue
    
    # Tarihe göre sırala (en yeni önce)
    sorted_weeks = sorted(weeks_data.items(), key=lambda x: x[1]['date'], reverse=True)
    
    # HTML içeriği oluştur
    html_content = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodeTime İstatistikleri</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .screenshot-card {{
            transition: transform 0.2s;
            cursor: pointer;
        }}
        .screenshot-card:hover {{
            transform: scale(1.02);
        }}
        .screenshot-img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
        .week-header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin: 20px 0 10px 0;
            padding: 15px;
            border-radius: 10px;
        }}
    </style>
</head>
<body class="bg-light">
    <div class="container my-5">
        <div class="row">
            <div class="col-12">
                <div class="text-center mb-5">
                    <h1 class="display-4 text-primary">📊 CodeTime İstatistikleri</h1>
                    <p class="lead">Haftalık kodlama aktivitelerinizi görüntüleyin</p>
                    <small class="text-muted">Toplam {len(sorted_weeks)} hafta verisi bulundu</small>
                </div>
            </div>
        </div>
        
        <div class="row">
            <div class="col-12">
"""
    
    # Her hafta için kart oluştur
    for week_key, week_data in sorted_weeks:
        week_start = week_data['week_start'].strftime('%d %B %Y')
        week_end = week_data['week_end'].strftime('%d %B %Y')
        filename = week_data['filename']
        
        html_content += f"""
                <div class="week-header">
                    <h3 class="mb-1">📅 {week_start} - {week_end}</h3>
                    <small>Hafta başlangıcı: {week_key}</small>
                </div>
                
                <div class="card mb-4 screenshot-card" data-bs-toggle="modal" data-bs-target="#modal-{week_key.replace('-', '')}">
                    <div class="card-body p-3">
                        <div class="row">
                            <div class="col-12">
                                <img src="{SCREENSHOTS_DIR}/{filename}" alt="CodeTime {week_start}" class="screenshot-img w-100">
                            </div>
                        </div>
                    </div>
                </div>
                
                <!-- Modal for {week_key} -->
                <div class="modal fade" id="modal-{week_key.replace('-', '')}" tabindex="-1">
                    <div class="modal-dialog modal-xl">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title">CodeTime - {week_start} / {week_end}</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                            </div>
                            <div class="modal-body text-center">
                                <img src="{SCREENSHOTS_DIR}/{filename}" alt="CodeTime {week_start}" class="img-fluid">
                            </div>
                        </div>
                    </div>
                </div>
"""
    
    html_content += """
            </div>
        </div>
        
        <div class="row mt-5">
            <div class="col-12 text-center">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">📈 Özet Bilgiler</h5>
                        <div class="row">
                            <div class="col-md-4">
                                <h6 class="text-primary">Toplam Hafta</h6>
                                <p class="h4">""" + str(len(sorted_weeks)) + """</p>
                            </div>
                            <div class="col-md-4">
                                <h6 class="text-success">İlk Kayıt</h6>
                                <p class="h6">""" + (sorted_weeks[-1][1]['week_start'].strftime('%d.%m.%Y') if sorted_weeks else 'Veri yok') + """</p>
                            </div>
                            <div class="col-md-4">
                                <h6 class="text-info">Son Kayıt</h6>
                                <p class="h6">""" + (sorted_weeks[0][1]['week_start'].strftime('%d.%m.%Y') if sorted_weeks else 'Veri yok') + """</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""
    
    # HTML dosyasını kaydet
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ index.html dosyası oluşturuldu! ({len(sorted_weeks)} hafta verisi işlendi)")

if __name__ == "__main__":
    generate_html_index()
