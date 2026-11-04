# -*- coding: utf-8 -*-
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "businesses.json")
out_file = os.path.join(base_dir, "dist", "index.html")

with open(data_path, "r", encoding="utf-8") as f:
    businesses = json.load(f)

# Styles for cards
card_styles = {
    "uspeh-777": {"color": "#f97316", "bg": "rgba(234, 88, 12, 0.12)", "border": "rgba(249, 115, 22, 0.35)", "tag": "Кузовной цех и ТО"},
    "zvezda": {"color": "#f59e0b", "bg": "rgba(217, 119, 6, 0.12)", "border": "rgba(245, 158, 11, 0.35)", "tag": "Иномарки и Тёплый бокс"},
    "careta": {"color": "#38bdf8", "bg": "rgba(37, 99, 235, 0.12)", "border": "rgba(56, 189, 248, 0.35)", "tag": "Мультибренд 5.0"},
    "avtoray": {"color": "#34d399", "bg": "rgba(5, 150, 105, 0.12)", "border": "rgba(52, 211, 153, 0.35)", "tag": "Подвеска и ТО"},
    "avtolux": {"color": "#818cf8", "bg": "rgba(79, 70, 229, 0.12)", "border": "rgba(129, 140, 248, 0.35)", "tag": "Автостекла и Кузов"}
}

cards_html = ""
for b in businesses:
    slug = b["slug"]
    st = card_styles.get(slug, {"color": "#38bdf8", "bg": "rgba(255,255,255,0.05)", "border": "rgba(255,255,255,0.15)", "tag": "СТО"})
    phone = b["phones"][0]
    phone_clean = b["phone_clean"]
    
    cards_html += f"""
    <div class="biz-card" style="border-top: 3px solid {st['color']};">
      <div class="biz-top">
        <span class="biz-tag" style="color: {st['color']}; background: {st['bg']}; border: 1px solid {st['border']};">{st['tag']}</span>
        <span class="biz-rating">★ {b['rating']} <span style="color: #94a3b8; font-size: 11px;">({b['reviews_count']} отз.)</span></span>
      </div>
      <h2 class="biz-name">{b['name']}</h2>
      <p class="biz-address">📍 {b['address']}</p>
      <p class="biz-tagline">{b['tagline']}</p>
      
      <div class="biz-actions">
        <a href="./{slug}/index.html" class="btn btn-view" style="background: {st['color']}; color: #0b0d11;">
          📱 Открыть демо-сайт →
        </a>
        <a href="tel:{phone_clean}" class="btn btn-call">
          📞 {phone}
        </a>
      </div>
    </div>
    """

hub_html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>Vibe-Sites Воронеж | Каталог готовых мобильных сайтов СТО</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Unbounded:wght@700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #090a0d;
      color: #f1f5f9;
      font-family: 'Inter', sans-serif;
      line-height: 1.5;
      padding: 40px 16px 80px;
    }}
    .container {{
      max-width: 960px;
      margin: 0 auto;
    }}
    .header {{
      text-align: center;
      margin-bottom: 36px;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      background: rgba(249, 115, 22, 0.12);
      border: 1px solid rgba(249, 115, 22, 0.35);
      color: #fb923c;
      font-size: 12px;
      font-weight: 700;
      border-radius: 999px;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 12px;
    }}
    h1 {{
      font-family: 'Unbounded', sans-serif;
      font-size: clamp(24px, 4.5vw, 38px);
      font-weight: 800;
      line-height: 1.15;
      margin-bottom: 10px;
      color: #fff;
    }}
    .subtitle {{
      color: #94a3b8;
      font-size: 15px;
      max-width: 600px;
      margin: 0 auto;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
      gap: 16px;
    }}
    .biz-card {{
      background: #12141a;
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 14px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.2s, border-color 0.2s;
    }}
    .biz-card:hover {{
      transform: translateY(-2px);
      border-color: rgba(255,255,255,0.2);
    }}
    .biz-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}
    .biz-tag {{
      font-size: 11px;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 6px;
      text-transform: uppercase;
    }}
    .biz-rating {{
      color: #fbbf24;
      font-weight: 700;
      font-size: 14px;
    }}
    .biz-name {{
      font-family: 'Unbounded', sans-serif;
      font-size: 17px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 6px;
    }}
    .biz-address {{
      font-size: 13px;
      color: #94a3b8;
      margin-bottom: 10px;
    }}
    .biz-tagline {{
      font-size: 13px;
      color: #cbd5e1;
      line-height: 1.45;
      margin-bottom: 20px;
      flex: 1;
    }}
    .biz-actions {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .btn {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 12px;
      border-radius: 9px;
      font-size: 13.5px;
      font-weight: 700;
      text-decoration: none;
      transition: opacity 0.2s;
    }}
    .btn-view:hover {{
      opacity: 0.9;
    }}
    .btn-call {{
      background: rgba(255,255,255,0.06);
      color: #e2e8f0;
      border: 1px solid rgba(255,255,255,0.1);
    }}
    .btn-call:hover {{
      background: rgba(255,255,255,0.12);
    }}
    .footer-note {{
      text-align: center;
      margin-top: 36px;
      font-size: 12px;
      color: #64748b;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="badge">⚡ Эксперимент Vibe-Coding 2026</div>
      <h1>ВИТРИНА МОБИЛЬНЫХ САЙТОВ СТО</h1>
      <p class="subtitle">г. Воронеж. Автономные посадочные страницы для автосервисов без сайта с рейтингом 4.8–5.0 по методике ролика kayy.</p>
    </div>

    <div class="grid">
      {cards_html}
    </div>

    <div class="footer-note">
      <p>5 сайтов сгенерированы с уникальным дизайном, персональными авто-палитрами и живыми часами работы.</p>
      <p style="margin-top: 4px;">Сверено с карточками 2ГИС и Яндекс Карт: Ноябрь 2026 г.</p>
    </div>
  </div>
</body>
</html>
"""

with open(out_file, "w", encoding="utf-8") as f:
    f.write(hub_html)

print("SUCCESS: dist/index.html hub catalog created!")
