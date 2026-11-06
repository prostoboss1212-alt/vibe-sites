# -*- coding: utf-8 -*-
import json
import os
import shutil

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "businesses.json")

with open(data_path, "r", encoding="utf-8") as f:
    businesses = json.load(f)

themes = {
    "uspeh-777": {
        "accent": "#ea580c",
        "accent_light": "#f97316",
        "hero_grad": "rgba(234, 88, 12, 0.25)",
        "banner_grad": "linear-gradient(135deg, #ea580c 0%, #c2410c 100%)",
        "shadow": "rgba(249, 115, 22, 0.32)",
        "border_hover": "rgba(249, 115, 22, 0.45)",
        "price_color": "#f97316",
        "values": [
            ("01", "Кузовной и покрасочный цех", "Собственная малярная камера, стапель для исправления геометрии, профессиональный подбор автоэмалей и локальная покраска деталей в стык."),
            ("02", "3D Развал-схождение и шиномонтаж", "Современный цифровой стенд сход-развала, калибровка подвески, проточка тормозных дисков и точная балансировка колес R13–R22."),
            ("03", "Выручают в срочных ситуациях", "По отзывам водителей, мастера идут навстречу при экстренных поломках, быстро подбирают запчасти и дают честную гарантию на работу.")
        ],
        "custom_showcase": '''
      <div class="showcase-grid">
        <div class="showcase-card" style="background-image: linear-gradient(180deg, rgba(12, 13, 16, 0.25) 0%, rgba(12, 13, 16, 0.94) 100%), url('https://images.unsplash.com/photo-1619642751034-765dfdf7c58e?auto=format&fit=crop&w=800&q=80'); background-size: cover; background-position: center;">
          <span class="showcase-badge">Слесарный и моторный цех</span>
          <div class="showcase-title">Ремонт ДВС, ходовой и проточка дисков</div>
          <div class="showcase-desc">Замена ГРМ, чистка впуска орехоструем, ремонт стоек, 3D сход-развал и проточка тормозных дисков на специализированном оборудовании</div>
        </div>
        <div class="showcase-card" style="background-image: linear-gradient(180deg, rgba(12, 13, 16, 0.25) 0%, rgba(12, 13, 16, 0.94) 100%), url('https://images.unsplash.com/photo-1580273916550-e323be2ae537?auto=format&fit=crop&w=800&q=80'); background-size: cover; background-position: center;">
          <span class="showcase-badge">Кузов, климат и шиномонтаж</span>
          <div class="showcase-title">Кузовные работы, кондиционеры и шины</div>
          <div class="showcase-desc">Кузовной ремонт и покраска в камере, заправка и антибактериальная обработка автокондиционеров, шиномонтаж и сезонное хранение шин</div>
        </div>
      </div>'''
    },
    "zvezda": {
        "accent": "#d97706",
        "accent_light": "#f59e0b",
        "hero_grad": "rgba(217, 119, 6, 0.24)",
        "banner_grad": "linear-gradient(135deg, #b45309 0%, #78350f 100%)",
        "shadow": "rgba(245, 158, 11, 0.28)",
        "border_hover": "rgba(245, 158, 11, 0.4)",
        "price_color": "#fbbf24",
        "values": [
            ("01", "Выручают в сложных ситуациях", "По отзывам водителей, мастера выручают при экстренных поломках в дороге и перед сверкой номеров ДВС в ГАИ, когда другие сервисы отказывают."),
            ("02", "Специализация на иномарках", "Знаем регламенты обслуживания европейских, корейских и японских авто. Оперативный заказ запчастей и масел под допуски производителей."),
            ("03", "Сварочные работы и тёплый бокс", "Оперативный ремонт выхлопных систем и глушителей, а также почасовая аренда тёплого бокса с подъёмником для самостоятельного ремонта.")
        ],
        "custom_showcase": '''
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px;">
        <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-md); padding: 18px; border-left: 4px solid var(--accent-light);">
          <div style="font-size: 11px; text-transform: uppercase; color: var(--accent-light); font-weight: 700; margin-bottom: 4px;">Специализация</div>
          <div style="color: #fff; font-weight: 700; font-size: 15px;">Ремонт иномарок и ТО</div>
          <div style="color: var(--text-muted); font-size: 13px; margin-top: 4px;">Европейские, корейские и японские авто</div>
        </div>
        <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-md); padding: 18px; border-left: 4px solid #10b981;">
          <div style="font-size: 11px; text-transform: uppercase; color: #34d399; font-weight: 700; margin-bottom: 4px;">Уникальная опция</div>
          <div style="color: #fff; font-weight: 700; font-size: 15px;">Аренда тёплого бокса</div>
          <div style="color: var(--text-muted); font-size: 13px; margin-top: 4px;">Подъёмник + инструмент от 400 ₽/час</div>
        </div>
        <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-md); padding: 18px; border-left: 4px solid #38bdf8;">
          <div style="font-size: 11px; text-transform: uppercase; color: #38bdf8; font-weight: 700; margin-bottom: 4px;">Репутация</div>
          <div style="color: #fff; font-weight: 700; font-size: 15px;">Знак «Хорошее место»</div>
          <div style="color: var(--text-muted); font-size: 13px; margin-top: 4px;">Рейтинг 4.9 в 2ГИС и 4.6 на Яндекс Картах</div>
        </div>
      </div>'''
    },
    "careta": {
        "accent": "#2563eb",
        "accent_light": "#38bdf8",
        "hero_grad": "rgba(37, 99, 235, 0.25)",
        "banner_grad": "linear-gradient(135deg, #1d4ed8 0%, #1e3a8a 100%)",
        "shadow": "rgba(56, 189, 248, 0.28)",
        "border_hover": "rgba(56, 189, 248, 0.4)",
        "price_color": "#38bdf8",
        "values": [
            ("01", "Понятно и без навязываний", "Мастера Дима и Олег всегда подробно и на понятном языке объяснят суть неисправности, предложат надежный и бюджетный вариант ремонта."),
            ("02", "Комплексный автотехцентр", "От планового техобслуживания и антикоррозийной обработки днища до сложного ремонта бензиновых и дизельных двигателей."),
            ("03", "Высшая оценка 5.0 в 2ГИС", "Безупречная репутация среди автовладельцев. Оперативная доставка запчастей, соблюдение сроков и гарантия на выполненные работы.")
        ],
        "custom_showcase": '''
      <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-md); padding: 22px;">
        <div style="font-family: 'Unbounded', sans-serif; font-size: 15px; font-weight: 700; color: #fff; margin-bottom: 8px;">
          🌐 Мультибрендовый автотехцентр на Димитрова, 112А
        </div>
        <div style="color: var(--text-muted); font-size: 13.5px; line-height: 1.5; margin-bottom: 14px;">
          Обслуживаем европейские, корейские, японские и современные китайские марки авто (Chery, Haval, Geely). Компьютерная диагностика электронных систем, проверенные технические жидкости и качественные расходники.
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
          <span style="background: rgba(56, 189, 248, 0.12); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 6px;">VAG & BMW</span>
          <span style="background: rgba(56, 189, 248, 0.12); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 6px;">Kia & Hyundai</span>
          <span style="background: rgba(56, 189, 248, 0.12); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 6px;">Toyota & Nissan</span>
          <span style="background: rgba(56, 189, 248, 0.12); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 6px;">Haval & Geely & Chery</span>
          <span style="background: rgba(56, 189, 248, 0.12); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 6px;">LADA</span>
        </div>
      </div>'''
    },
    "avtoray": {
        "accent": "#059669",
        "accent_light": "#10b981",
        "hero_grad": "rgba(5, 150, 105, 0.25)",
        "banner_grad": "linear-gradient(135deg, #047857 0%, #064e3b 100%)",
        "shadow": "rgba(16, 185, 129, 0.28)",
        "border_hover": "rgba(16, 185, 129, 0.4)",
        "price_color": "#34d399",
        "values": [
            ("01", "Открытая ремзона", "Полный контроль процесса ремонта: мастер Денис детально объясняет каждую операцию и наглядно показывает состояние узлов ходовой на подъёмнике."),
            ("02", "Фиксированная смета", "Стоимость согласуется до начала ремонта. Никаких сюрпризов в чеке — все работы выполняются строго по договоренности."),
            ("03", "Рейтинг 5.0 на Яндекс Картах", "Максимальная оценка 5.0 на основе 32 реальных отзывов водителей Воронежа. Чистота, аккуратность и честный подход к делу.")
        ],
        "custom_showcase": '''
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
        <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-md); padding: 20px; border-top: 3px solid #10b981;">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
            <span style="font-size: 18px;">👁️</span>
            <span style="font-family: 'Unbounded', sans-serif; font-size: 14px; font-weight: 700; color: #fff;">Открытая ремзона</span>
          </div>
          <div style="color: var(--text-muted); font-size: 13px; line-height: 1.45;">
            Вы можете лично присутствовать при диагностике подвески на подъёмнике. Мастер покажет каждую изношенную деталь.
          </div>
        </div>
        <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-md); padding: 20px; border-top: 3px solid #10b981;">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
            <span style="font-size: 18px;">📋</span>
            <span style="font-family: 'Unbounded', sans-serif; font-size: 14px; font-weight: 700; color: #fff;">Цена до начала работ</span>
          </div>
          <div style="color: var(--text-muted); font-size: 13px; line-height: 1.45;">
            Никаких внезапных сумм в чеке. Стоимость слесарных работ и запчастей согласовывается ДО того, как мастер возьмёт инструмент.
          </div>
        </div>
        <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-md); padding: 20px; border-top: 3px solid #10b981;">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
            <span style="font-size: 18px;">⚡</span>
            <span style="font-family: 'Unbounded', sans-serif; font-size: 14px; font-weight: 700; color: #fff;">Запчасти день-в-день</span>
          </div>
          <div style="color: var(--text-muted); font-size: 13px; line-height: 1.45;">
            Быстрый подбор качественных расходников и деталей под установку прямо в сервисе без необходимости мотаться по магазинам.
          </div>
        </div>
      </div>'''
    },
    "avtolux": {
        "accent": "#4f46e5",
        "accent_light": "#38bdf8",
        "hero_grad": "rgba(79, 70, 229, 0.25)",
        "banner_grad": "linear-gradient(135deg, #4338ca 0%, #312e81 100%)",
        "shadow": "rgba(56, 189, 248, 0.28)",
        "border_hover": "rgba(79, 70, 229, 0.45)",
        "price_color": "#818cf8",
        "values": [
            ("01", "Профильный опыт по автостёклам", "Специализированное оборудование для аккуратного демонтажа без повреждения рамки кузова и профессиональная вклейка лобовых и боковых стекол."),
            ("02", "Бессрочная гарантия на шов", "Используем проверенные праймеры и полиуретановые герметики. Предоставляем бессрочную гарантию на герметичность клеевого шва."),
            ("03", "Честное человеческое отношение", "По отзывам клиентов, мастера работают на совесть: качественно полируют кузов, заправляют кондиционеры и честно консультируют без лишних трат.")
        ],
        "custom_showcase": '''
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px;">
        <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-md); padding: 18px; border-left: 4px solid var(--accent-light);">
          <div style="font-size: 11px; text-transform: uppercase; color: var(--accent-light); font-weight: 700; margin-bottom: 4px;">Скорость</div>
          <div style="color: #fff; font-weight: 700; font-size: 15px;">Вклейка от 1.5 часов</div>
          <div style="color: var(--text-muted); font-size: 13px; margin-top: 4px;">Надежный быстросохнущий полиуретановый клей-герметик</div>
        </div>
        <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-md); padding: 18px; border-left: 4px solid #10b981;">
          <div style="font-size: 11px; text-transform: uppercase; color: #34d399; font-weight: 700; margin-bottom: 4px;">Надежность</div>
          <div style="color: #fff; font-weight: 700; font-size: 15px;">Бессрочная гарантия</div>
          <div style="color: var(--text-muted); font-size: 13px; margin-top: 4px;">Гарантируем герметичность клеевого шва от протечек</div>
        </div>
        <div style="background: var(--bg-card); border: 1px solid var(--border-strong); border-radius: var(--radius-md); padding: 18px; border-left: 4px solid #a855f7;">
          <div style="font-size: 11px; text-transform: uppercase; color: #c084fc; font-weight: 700; margin-bottom: 4px;">Ремонт сколов</div>
          <div style="color: #fff; font-weight: 700; font-size: 15px;">Оптический фотополимер</div>
          <div style="color: var(--text-muted); font-size: 13px; margin-top: 4px;">Остановка трещин и восстановление прозрачности стекла</div>
        </div>
      </div>'''
    }
}

for b in businesses:
    slug = b["slug"]
    th = themes[slug]
    phone_main = b["phones"][0]
    phone_clean = b["phone_clean"]
    lat = b["geo"]["lat"]
    lon = b["geo"]["lon"]
    oid = b["yandex_oid"]
    
    if len(b["phones"]) > 1:
        sec_clean = "+74732568056"
        hero_phones_html = f'\n            <a href="tel:{phone_clean}" class="hero-phone-big">{b["phones"][0]}</a>\n            <a href="tel:{sec_clean}" class="hero-phone-secondary">{b["phones"][1]}</a>'
        contacts_phones_html = f'\n              <div class="contact-label">Телефоны сервиса</div>\n              <a href="tel:{phone_clean}" class="contact-phone-item">{b["phones"][0]}</a>\n              <a href="tel:{sec_clean}" class="contact-phone-item">{b["phones"][1]}</a>'
        cta_buttons_html = f'\n        <a href="tel:{phone_clean}" class="btn-dark-pill">📞 {b["phones"][0]}</a>\n        <a href="tel:{sec_clean}" class="btn-white-outline">📞 {b["phones"][1]}</a>'
    else:
        hero_phones_html = f'\n            <a href="tel:{phone_clean}" class="hero-phone-big">{phone_main}</a>'
        contacts_phones_html = f'\n              <div class="contact-label">Телефон сервиса</div>\n              <a href="tel:{phone_clean}" class="contact-phone-item">{phone_main}</a>'
        cta_buttons_html = f'\n        <a href="tel:{phone_clean}" class="btn-dark-pill">📞 Позвонить мастеру: {phone_main}</a>\n        <a href="#contacts" class="btn-white-outline">📍 Схема проезда</a>'

    gallery_cards = ""
    for g in b["gallery"]:
        gallery_cards += f'''
        <div class="gallery-card" style="background-image: linear-gradient(180deg, rgba(12, 13, 16, 0.15) 0%, rgba(12, 13, 16, 0.92) 100%), url('{g["url"]}');">
          <span class="gallery-tag">{g["tag"]}</span>
          <div class="gallery-title">{g["title"]}</div>
          <div class="gallery-desc">{g["desc"]}</div>
        </div>'''

    services_html = ""
    for s in b["services"]:
        services_html += f'''
        <div class="service-card" style="border-left: 3px solid {th["accent"]};">
          <div>
            <div class="service-tag">{s["category"]}</div>
            <div class="service-name">{s["name"]}</div>
            <div class="service-desc">{s["description"]}</div>
          </div>
          <div class="service-price">
            <span style="color: {th["price_color"]};">{s["price"]}</span>
          </div>
        </div>'''

    values_html = ""
    for num, vtitle, vtext in th["values"]:
        values_html += f'''
        <div class="value-card">
          <div class="value-num">{num}</div>
          <div class="value-title">{vtitle}</div>
          <div class="value-text">{vtext}</div>
        </div>'''

    reviews_html = ""
    for r in b["reviews"]:
        reviews_html += f'''
          <div class="review-quote-card">
            <div>
              <div class="quote-mark" style="color: {th["accent_light"]};">“</div>
              <p class="review-body">{r["text"]}</p>
            </div>
            <div class="review-meta">
              <span>{r["author_note"]}</span>
              <span style="color: #fbbf24;">★★★★★</span>
            </div>
          </div>'''

    features_html = ""
    for feat in b["features"]:
        features_html += f'              <li><span class="check-icon">✓</span> {feat}</li>\n'

    yandex_stars = "★★★★★" if float(b["rating_yandex"].replace(",", ".")) >= 4.6 else "★★★★☆"
    short_title_brand = b["brand_short"].title() if b["brand_short"] != "CARETA" else "Careta"

    html_doc = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>{b['name']} — {b['address']} | {b['category_pill']} в Воронеже</title>
  <meta name="description" content="{b['name']} в Воронеже ({b['address']}, {b['district']}). Рейтинг {b['rating_2gis']} в 2ГИС ({b['reviews_count_2gis']}) и {b['rating_yandex']} на Яндекс Картах ({b['reviews_count_yandex']}). {b['tagline']}.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Unbounded:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-main: #0c0d10;
      --bg-card: #15171c;
      --bg-card-hover: #1c1f26;
      --bg-elevated: #1e2128;
      --text-main: #f3f4f6;
      --text-muted: #9ca3af;
      --text-dim: #6b7280;
      --accent: {th['accent']};
      --accent-light: {th['accent_light']};
      --border: rgba(255, 255, 255, 0.08);
      --border-strong: rgba(255, 255, 255, 0.14);
      --success: #10b981;
      --radius-lg: 16px;
      --radius-md: 12px;
      --radius-sm: 8px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    html {{
      scroll-behavior: smooth;
      overflow-x: hidden;
    }}

    body {{
      background-color: var(--bg-main);
      color: var(--text-main);
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.5;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }}

    @media (max-width: 768px) {{
      body {{
        padding-bottom: 78px;
      }}
    }}

    .container {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    /* Навигация */
    .navbar {{
      position: sticky;
      top: 0;
      z-index: 90;
      background: rgba(12, 13, 16, 0.90);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border);
    }}

    .navbar-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 64px;
    }}

    .nav-brand {{
      font-family: 'Unbounded', sans-serif;
      font-size: 15px;
      font-weight: 800;
      color: var(--text-main);
      text-decoration: none;
      letter-spacing: -0.02em;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .nav-brand-dot {{
      width: 10px;
      height: 10px;
      background: var(--accent-light);
      border-radius: 3px;
      display: inline-block;
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 24px;
    }}

    .nav-links a {{
      color: var(--text-muted);
      text-decoration: none;
      font-size: 14px;
      font-weight: 500;
      transition: color 0.2s;
    }}

    .nav-links a:hover {{
      color: var(--text-main);
    }}

    .nav-cta {{
      background: var(--accent);
      color: #fff !important;
      padding: 9px 16px;
      border-radius: var(--radius-sm);
      font-weight: 600 !important;
      font-size: 13px !important;
      transition: background 0.2s, transform 0.15s !important;
    }}

    .nav-cta:hover {{
      background: var(--accent-light);
      transform: translateY(-1px);
    }}

    @media (max-width: 720px) {{
      .nav-links a:not(.nav-cta) {{
        display: none;
      }}
    }}

    /* Hero-секция с атмосферным фото ремзоны (без номеров и личных данных) */
    .hero {{
      position: relative;
      padding: 64px 0 52px;
      background-image:
        radial-gradient(circle at 80% 20%, {th['hero_grad']} 0%, transparent 65%),
        linear-gradient(90deg, rgba(12, 13, 16, 0.96) 0%, rgba(12, 13, 16, 0.88) 55%, rgba(12, 13, 16, 0.72) 100%),
        linear-gradient(180deg, rgba(12, 13, 16, 0.3) 0%, var(--bg-main) 100%),
        url('{b["hero_bg"]}');
      background-size: cover;
      background-position: center;
      border-bottom: 1px solid var(--border);
      overflow: hidden;
    }}

    .hero-content {{
      position: relative;
      z-index: 2;
      max-width: 800px;
    }}

    .hero-pills {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      margin-bottom: 20px;
    }}

    .pill {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }}

    .pill-primary {{
      background: var(--accent);
      color: #fff;
    }}

    .pill-secondary {{
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid var(--border-strong);
      color: var(--text-main);
      backdrop-filter: blur(6px);
    }}

    .pill-award {{
      background: rgba(245, 158, 11, 0.16);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: #fbbf24;
      backdrop-filter: blur(6px);
    }}

    .hero-title {{
      font-family: 'Unbounded', sans-serif;
      font-size: clamp(30px, 5.5vw, 54px);
      font-weight: 800;
      line-height: 1.08;
      letter-spacing: -0.03em;
      text-transform: uppercase;
      color: #ffffff;
      margin-bottom: 18px;
    }}

    .hero-sub {{
      font-size: clamp(16px, 2vw, 18px);
      color: #e5e7eb;
      max-width: 660px;
      margin-bottom: 28px;
      font-weight: 400;
      line-height: 1.55;
    }}

    .hero-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 28px;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      padding: 15px 26px;
      border-radius: 999px;
      font-size: 15px;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.2s ease;
      border: 1px solid transparent;
    }}

    .btn-primary {{
      background: var(--accent-light);
      color: #0c0d10;
      font-weight: 700;
      box-shadow: 0 6px 22px {th['shadow']};
    }}

    .btn-primary:hover {{
      filter: brightness(1.08);
      transform: translateY(-2px);
    }}

    .btn-outline {{
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-main);
      border-color: var(--border-strong);
      backdrop-filter: blur(8px);
    }}

    .btn-outline:hover {{
      background: rgba(255, 255, 255, 0.14);
      transform: translateY(-2px);
    }}

    @media (max-width: 520px) {{
      .hero-actions {{
        display: grid;
        grid-template-columns: 1fr 1fr;
      }}
      .btn {{
        padding: 14px 16px;
        font-size: 14px;
      }}
    }}

    .hero-contact-meta {{
      padding-top: 18px;
      border-top: 1px solid var(--border-strong);
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}

    .hero-phones-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: baseline;
      gap: 18px;
    }}

    .hero-phone-big {{
      font-family: 'Unbounded', sans-serif;
      font-size: clamp(19px, 2.8vw, 25px);
      font-weight: 700;
      color: #ffffff;
      text-decoration: none;
      letter-spacing: -0.02em;
    }}

    .hero-phone-big:hover {{
      color: var(--accent-light);
    }}

    .hero-phone-secondary {{
      font-family: 'Unbounded', sans-serif;
      font-size: clamp(15px, 2vw, 18px);
      font-weight: 600;
      color: var(--text-muted);
      text-decoration: none;
    }}

    .hero-phone-secondary:hover {{
      color: #ffffff;
    }}

    .hero-address-line {{
      font-size: 14px;
      color: #d1d5db;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
    }}

    .status-open {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #34d399;
      font-weight: 500;
    }}

    .status-closed {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #9ca3af;
      font-weight: 500;
    }}

    .status-closing-soon {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      color: #fbbf24;
      font-weight: 500;
    }}

    .status-dot {{
      width: 7px;
      height: 7px;
      background: #10b981;
      border-radius: 50%;
      box-shadow: 0 0 8px #10b981;
      animation: pulse-dot 2s infinite ease-in-out;
    }}

    .status-dot.closed {{
      background: #6b7280;
      box-shadow: none;
      animation: none;
    }}

    .status-dot.closing-soon {{
      background: #f59e0b;
      box-shadow: 0 0 8px #f59e0b;
    }}

    @keyframes pulse-dot {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.55; transform: scale(1.15); }}
    }}

    .sync-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.25);
      color: #34d399;
      font-size: 11.5px;
      font-weight: 600;
      padding: 5px 10px;
      border-radius: 6px;
    }}

    /* Витрина специализаций */
    .showcase-section {{
      margin-top: -20px;
      margin-bottom: 24px;
      position: relative;
      z-index: 5;
    }}

    .showcase-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }}

    @media (max-width: 680px) {{
      .showcase-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .showcase-card {{
      position: relative;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-strong);
      background: #14161b;
      min-height: 210px;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 22px;
    }}

    .showcase-badge {{
      position: absolute;
      top: 16px;
      left: 16px;
      background: rgba(12, 13, 16, 0.84);
      backdrop-filter: blur(6px);
      border: 1px solid var(--border-strong);
      color: var(--text-main);
      padding: 5px 10px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .showcase-title {{
      font-family: 'Unbounded', sans-serif;
      font-size: 17px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 6px;
      position: relative;
      z-index: 2;
    }}

    .showcase-desc {{
      font-size: 13px;
      color: #d1d5db;
      position: relative;
      z-index: 2;
    }}

    /* Фотогалерея оснащения (без номеров авто и лиц) */
    .gallery-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-top: 24px;
    }}

    @media (max-width: 680px) {{
      .gallery-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .gallery-card {{
      position: relative;
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border-strong);
      min-height: 210px;
      background-size: cover;
      background-position: center;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 22px;
    }}

    .gallery-tag {{
      position: absolute;
      top: 14px;
      left: 14px;
      background: rgba(12, 13, 16, 0.84);
      backdrop-filter: blur(6px);
      border: 1px solid var(--border-strong);
      color: var(--accent-light);
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 10.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .gallery-title {{
      font-family: 'Unbounded', sans-serif;
      font-size: 16px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 4px;
    }}

    .gallery-desc {{
      font-size: 13px;
      color: #d1d5db;
    }}

    /* Секции */
    .section {{
      padding: 52px 0;
      border-bottom: 1px solid var(--border);
    }}

    .section-eyebrow {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--accent-light);
      margin-bottom: 10px;
    }}

    .section-eyebrow::before {{
      content: "";
      width: 18px;
      height: 2px;
      background: var(--accent-light);
      display: inline-block;
    }}

    .section-heading {{
      font-family: 'Unbounded', sans-serif;
      font-size: clamp(22px, 3.5vw, 32px);
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #ffffff;
      margin-bottom: 28px;
    }}

    /* УСЛУГИ И ЦЕНЫ */
    .services-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
    }}

    @media (max-width: 900px) {{
      .services-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
    }}

    @media (max-width: 560px) {{
      .services-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .service-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: border-color 0.2s, background 0.2s, transform 0.2s;
    }}

    .service-card:hover {{
      border-color: {th['border_hover']};
      background: var(--bg-card-hover);
      transform: translateY(-2px);
    }}

    .service-tag {{
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-dim);
      margin-bottom: 8px;
    }}

    .service-name {{
      font-size: 16px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 8px;
      line-height: 1.3;
    }}

    .service-desc {{
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.45;
      margin-bottom: 18px;
    }}

    .service-price {{
      font-family: 'Unbounded', sans-serif;
      font-size: 15px;
      font-weight: 700;
      color: var(--accent-light);
      padding-top: 12px;
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .services-note {{
      margin-top: 20px;
      font-size: 13px;
      color: var(--text-muted);
    }}

    .services-note a {{
      color: var(--accent-light);
      text-decoration: none;
      font-weight: 600;
    }}

    /* ЗА ЧТО ЦЕНЯТ КЛИЕНТЫ */
    .values-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }}

    @media (max-width: 820px) {{
      .values-grid {{
        grid-template-columns: 1fr;
      }}
    }}

    .value-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 24px;
    }}

    .value-num {{
      font-family: 'Unbounded', sans-serif;
      font-size: 24px;
      font-weight: 800;
      color: var(--accent-light);
      margin-bottom: 12px;
      line-height: 1;
    }}

    .value-title {{
      font-size: 16px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 8px;
    }}

    .value-text {{
      font-size: 13.5px;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* ОТЗЫВЫ И ЖИВОЙ ВИДЖЕТ ЯНДЕКС КАРТ */
    .reviews-layout {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 20px;
      align-items: stretch;
    }}

    @media (max-width: 860px) {{
      .reviews-layout {{
        grid-template-columns: 1fr;
      }}
    }}

    .ratings-sidebar {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .rating-summary-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 22px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}

    .rating-platform-badge {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-muted);
      margin-bottom: 6px;
    }}

    .rating-big-number {{
      font-family: 'Unbounded', sans-serif;
      font-size: 44px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1;
      letter-spacing: -0.03em;
      margin-bottom: 8px;
    }}

    .rating-stars {{
      color: var(--accent-light);
      font-size: 16px;
      letter-spacing: 2px;
      margin-bottom: 6px;
    }}

    .rating-count-link {{
      font-size: 13px;
      color: var(--text-muted);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}

    .rating-count-link:hover {{
      color: #fff;
    }}

    .rating-award-pill {{
      margin-top: 12px;
      display: inline-block;
      background: rgba(245, 158, 11, 0.12);
      border: 1px solid rgba(245, 158, 11, 0.3);
      color: #fbbf24;
      font-size: 11px;
      font-weight: 600;
      padding: 6px 10px;
      border-radius: 6px;
      line-height: 1.35;
    }}

    .reviews-cards-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
    }}

    .review-quote-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .quote-mark {{
      font-family: Georgia, serif;
      font-size: 28px;
      line-height: 1;
      color: var(--accent-light);
      margin-bottom: 4px;
      font-weight: 700;
    }}

    .review-body {{
      font-size: 13.5px;
      color: #e5e7eb;
      line-height: 1.5;
      margin-bottom: 10px;
    }}

    .review-meta {{
      font-size: 11px;
      color: var(--text-dim);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .live-reviews-details {{
      margin-top: 20px;
      background: var(--bg-card);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-md);
      overflow: hidden;
    }}

    .live-reviews-summary {{
      padding: 16px 20px;
      cursor: pointer;
      font-weight: 600;
      font-size: 14px;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: space-between;
      list-style: none;
      user-select: none;
    }}

    .live-reviews-summary::-webkit-details-marker {{
      display: none;
    }}

    .live-reviews-summary:hover {{
      background: var(--bg-card-hover);
    }}

    .live-reviews-widget-wrap {{
      padding: 0 20px 20px;
      border-top: 1px solid var(--border);
    }}

    .reviews-footnote {{
      margin-top: 16px;
      font-size: 12px;
      color: var(--text-dim);
    }}

    .reviews-footnote a {{
      color: var(--accent-light);
      text-decoration: none;
    }}

    /* КАК ДОБРАТЬСЯ + КАРТА */
    .location-layout {{
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: 24px;
      align-items: stretch;
    }}

    @media (max-width: 860px) {{
      .location-layout {{
        grid-template-columns: 1fr;
      }}
    }}

    .location-info {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 28px 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}

    .location-address-title {{
      font-family: 'Unbounded', sans-serif;
      font-size: clamp(20px, 2.8vw, 25px);
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 4px;
      line-height: 1.25;
    }}

    .location-district {{
      font-size: 13.5px;
      color: var(--text-muted);
      margin-bottom: 22px;
    }}

    .contact-block {{
      margin-bottom: 18px;
    }}

    .contact-label {{
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-dim);
      margin-bottom: 6px;
    }}

    .contact-phone-item {{
      display: block;
      font-family: 'Unbounded', sans-serif;
      font-size: 16px;
      font-weight: 700;
      color: var(--accent-light);
      text-decoration: none;
      margin-bottom: 4px;
    }}

    .contact-phone-item:hover {{
      text-decoration: underline;
    }}

    .contact-hours {{
      font-size: 14px;
      color: var(--text-main);
      font-weight: 500;
    }}

    .features-list-contacts {{
      list-style: none;
      margin: 12px 0 22px;
      display: grid;
      grid-template-columns: 1fr;
      gap: 7px;
    }}

    .features-list-contacts li {{
      font-size: 13px;
      color: #d1d5db;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .check-icon {{
      color: var(--accent-light);
      font-weight: bold;
    }}

    .route-buttons {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .btn-route {{
      flex: 1;
      min-width: 155px;
      background: var(--bg-elevated);
      border: 1px solid var(--border-strong);
      color: #ffffff;
      padding: 12px 14px;
      border-radius: var(--radius-sm);
      font-size: 13px;
      font-weight: 600;
      text-decoration: none;
      text-align: center;
      transition: background 0.2s, border-color 0.2s;
    }}

    .btn-route:hover {{
      background: #272b35;
      border-color: var(--accent-light);
    }}

    .map-container {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      overflow: hidden;
      min-height: 380px;
      position: relative;
    }}

    .map-container iframe {{
      width: 100%;
      height: 100%;
      min-height: 380px;
      border: 0;
      display: block;
    }}

    /* CTA-баннер */
    .cta-banner {{
      background: {th['banner_grad']};
      padding: 56px 0;
      color: #ffffff;
    }}

    .cta-banner-inner {{
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      gap: 16px;
    }}

    .cta-banner-title {{
      font-family: 'Unbounded', sans-serif;
      font-size: clamp(28px, 4.8vw, 44px);
      font-weight: 800;
      line-height: 1.08;
      letter-spacing: -0.02em;
      text-transform: uppercase;
      color: #ffffff;
    }}

    .cta-banner-sub {{
      font-size: 16px;
      color: rgba(255, 255, 255, 0.9);
      max-width: 540px;
    }}

    .cta-banner-buttons {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 8px;
    }}

    .btn-dark-pill {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: #0c0d10;
      color: #ffffff;
      padding: 15px 24px;
      border-radius: 999px;
      font-family: 'Unbounded', sans-serif;
      font-size: 13.5px;
      font-weight: 700;
      text-decoration: none;
      transition: transform 0.2s, background 0.2s;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.28);
    }}

    .btn-dark-pill:hover {{
      background: #181a20;
      transform: translateY(-2px);
    }}

    .btn-white-outline {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.14);
      border: 1px solid rgba(255, 255, 255, 0.35);
      color: #ffffff;
      padding: 15px 20px;
      border-radius: 999px;
      font-size: 13.5px;
      font-weight: 600;
      text-decoration: none;
      transition: background 0.2s;
    }}

    .btn-white-outline:hover {{
      background: rgba(255, 255, 255, 0.24);
    }}

    /* Футер с дисклеймером */
    .footer {{
      background: #08090b;
      padding: 28px 0;
      border-top: 1px solid var(--border);
      font-size: 12px;
      color: var(--text-dim);
      line-height: 1.6;
    }}

    /* Плавающая мобильная панель */
    .mobile-sticky-bar {{
      display: none;
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      z-index: 100;
      background: rgba(12, 13, 16, 0.94);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-top: 1px solid var(--border-strong);
      padding: 10px 16px;
    }}

    .mobile-sticky-grid {{
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 10px;
    }}

    .mob-btn-call {{
      background: var(--accent-light);
      color: #0c0d10;
      font-weight: 700;
      font-size: 14px;
      padding: 13px;
      border-radius: 10px;
      text-decoration: none;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}

    .mob-btn-map {{
      background: var(--bg-elevated);
      color: #ffffff;
      border: 1px solid var(--border-strong);
      font-weight: 600;
      font-size: 13px;
      padding: 13px;
      border-radius: 10px;
      text-decoration: none;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}

    @media (max-width: 768px) {{
      .mobile-sticky-bar {{
        display: block;
      }}
    }}
  </style>
</head>
<body>

  <!-- Навигация -->
  <nav class="navbar">
    <div class="container navbar-inner">
      <a href="#" class="nav-brand">
        <span class="nav-brand-dot"></span>
        {b['brand_short']}
      </a>
      <div class="nav-links">
        <a href="#services">Услуги и прайс</a>
        <a href="#why">О сервисе</a>
        <a href="#reviews">Отзывы ({b['total_reviews_nav']})</a>
        <a href="#contacts">Контакты</a>
        <a href="tel:{phone_clean}" class="nav-cta">{phone_main}</a>
      </div>
    </div>
  </nav>

  <!-- HERO-БЛОК -->
  <header class="hero">
    <div class="container">
      <div class="hero-content">
        <div class="hero-pills">
          <span class="pill pill-primary">{b['category_pill']}</span>
          <span class="pill pill-secondary">{b['district']}</span>
          <span class="pill pill-award">{b['badge']}</span>
        </div>

        <h1 class="hero-title">{b['hero_title']}</h1>

        <p class="hero-sub">
          {b['hero_sub']}
        </p>

        <div class="hero-actions">
          <a href="tel:{phone_clean}" class="btn btn-primary">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            Позвонить
          </a>
          <a href="#contacts" class="btn btn-outline">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            Маршрут
          </a>
        </div>

        <div class="hero-contact-meta">
          <div class="hero-phones-row">{hero_phones_html}
          </div>
          <div class="hero-address-line">
            <span>{b['address']} ({b['address_hint']})</span>
            <span>•</span>
            <span id="work-status" class="status-open"><span class="status-dot"></span> Открыто • {b['hours_short']}</span>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- БЛОК СПЕЦИАЛИЗАЦИИ -->
  <section class="showcase-section">
    <div class="container">{th['custom_showcase']}
    </div>
  </section>

  <!-- УСЛУГИ И ЦЕНЫ -->
  <section id="services" class="section">
    <div class="container">
      <div class="section-eyebrow">Услуги и цены</div>
      <h2 class="section-heading">Работы и прайс-лист</h2>

      <div class="services-grid">{services_html}
      </div>

      <p class="services-note">
        Точная стоимость работ и запчастей согласуется после осмотра автомобиля. Запись и консультация по телефону: <a href="tel:{phone_clean}">{phone_main}</a>.
      </p>
    </div>
  </section>

  <!-- ЗА ЧТО ЦЕНЯТ КЛИЕНТЫ + ИЛЛЮСТРАЦИИ ОСНАЩЕНИЯ -->
  <section id="why" class="section">
    <div class="container">
      <div class="section-eyebrow">Факты о сервисе</div>
      <h2 class="section-heading">За что клиенты выбирают «{short_title_brand}»</h2>

      <div class="values-grid">{values_html}
      </div>

      <div class="gallery-grid">{gallery_cards}
      </div>
    </div>
  </section>

  <!-- ОТЗЫВЫ КЛИЕНТОВ + ЖИВАЯ ЛЕНТА ЯНДЕКС КАРТ -->
  <section id="reviews" class="section">
    <div class="container">
      <div class="section-eyebrow">Репутация на картах</div>
      <h2 class="section-heading">Отзывы владельцев авто</h2>

      <div class="reviews-layout">
        <!-- Левая колонка: реальные рейтинги 2ГИС и Яндекс Карт -->
        <div class="ratings-sidebar">
          <div class="rating-summary-card">
            <div class="rating-platform-badge">Рейтинг в 2ГИС</div>
            <div class="rating-big-number">{b['rating_2gis']}</div>
            <div class="rating-stars">★★★★★</div>
            <a href="{b['2gis_reviews_url']}" target="_blank" rel="noopener" class="rating-count-link">
              {b['reviews_count_2gis']} в 2ГИС →
            </a>
            <div class="rating-award-pill">
              {b['award_pill']}
            </div>
          </div>

          <div class="rating-summary-card">
            <div class="rating-platform-badge">Яндекс Карты</div>
            <div class="rating-big-number">{b['rating_yandex']}</div>
            <div class="rating-stars">{yandex_stars}</div>
            <a href="{b['yandex_reviews_url']}" target="_blank" rel="noopener" class="rating-count-link">
              {b['reviews_count_yandex']} →
            </a>
          </div>

          <div class="sync-badge">
            ✓ Оценки сверены с картами: <span class="sync-date-text">ноябрь 2026 г.</span>
          </div>
        </div>

        <!-- Правая колонка с реальными отзывами -->
        <div class="reviews-cards-grid">{reviews_html}
        </div>
      </div>

      <!-- Автообновляемый официальный виджет отзывов Яндекс Карт -->
      <details class="live-reviews-details">
        <summary class="live-reviews-summary">
          <span>🔄 Открыть живую ленту отзывов Яндекс Карт (обновляется автоматически)</span>
          <span style="color: var(--accent-light); font-size: 13px;">Показать ▼</span>
        </summary>
        <div class="live-reviews-widget-wrap">
          <div style="max-width: 760px; height: 520px; overflow: hidden; position: relative; margin: 16px auto 0; border-radius: 10px; border: 1px solid var(--border-strong);">
            <iframe style="width: 100%; height: 100%; border: none; border-radius: 10px; box-sizing: border-box;" src="https://yandex.ru/maps-reviews-widget/{oid}?comments" loading="lazy" title="Живые отзывы Яндекс Карт — {b['name']}"></iframe>
          </div>
        </div>
      </details>

      <p class="reviews-footnote">
        Все оригиналы отзывов доступны в официальных карточках: <a href="{b['yandex_reviews_url']}" target="_blank" rel="noopener">Яндекс Карты ({b['rating_yandex']} • {b['reviews_count_yandex']})</a> и <a href="{b['2gis_reviews_url']}" target="_blank" rel="noopener">2ГИС ({b['rating_2gis']} • {b['reviews_count_2gis']})</a>.
      </p>
    </div>
  </section>

  <!-- КАК ДОБРАТЬСЯ И КАРТА -->
  <section id="contacts" class="section">
    <div class="container">
      <div class="section-eyebrow">Как добраться</div>
      <h2 class="section-heading">Координаты и телефоны</h2>

      <div class="location-layout">
        <div class="location-info">
          <div>
            <div class="location-address-title">{b['address_short']}</div>
            <div class="location-district">г. Воронеж, {b['district']} • Координаты: {lat}, {lon}</div>

            <div class="contact-block">{contacts_phones_html}
            </div>

            <div class="contact-block">
              <div class="contact-label">График работы</div>
              <div class="contact-hours">{b['hours']}</div>
            </div>

            <div class="contact-label">Удобства и стандарты сервиса</div>
            <ul class="features-list-contacts">
{features_html}            </ul>
          </div>

          <div class="route-buttons">
            <a href="{b['yandex_url']}" target="_blank" rel="noopener" class="btn-route">
              📍 Открыть в Яндекс Картах
            </a>
            <a href="{b['2gis_url']}" target="_blank" rel="noopener" class="btn-route">
              🧭 Открыть карточку 2ГИС
            </a>
          </div>
        </div>

        <div class="map-container">
          <iframe 
            src="https://yandex.ru/map-widget/v1/?ol=biz&oid={oid}" 
            title="Карта проезда в {b['name']} ({b['address_short']})"
            loading="lazy"
            allowfullscreen>
          </iframe>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA-БАННЕР ВНИЗУ -->
  <section class="cta-banner">
    <div class="container cta-banner-inner">
      <h2 class="cta-banner-title">{b['cta_title']}</h2>
      <p class="cta-banner-sub">
        {b['cta_sub']}
      </p>
      <div class="cta-banner-buttons">{cta_buttons_html}
      </div>
    </div>
  </section>

  <!-- ФУТЕР С ДИСКЛЕЙМЕРОМ ПО RULES.MD -->
  <footer class="footer">
    <div class="container">
      <div style="margin-bottom: 10px;">
        <span class="sync-badge">✓ Данные актуальны: <span class="sync-date-text">ноябрь 2026 г.</span></span>
      </div>
      <p>
        Демо-концепт мобильного сайта для {b['name']} ({b['address']}). Не является публичной офертой. Удалим или передадим права по первой просьбе владельца. Все данные сверены с открытыми карточками организации в 2ГИС и Яндекс Картах.
      </p>
    </div>
  </footer>

  <!-- ПЛАВАЮЩАЯ МОБИЛЬНАЯ ПАНЕЛЬ -->
  <div class="mobile-sticky-bar">
    <div class="mobile-sticky-grid">
      <a href="tel:{phone_clean}" class="mob-btn-call">
        📞 Позвонить
      </a>
      <a href="https://yandex.ru/maps/?rtext=~{lat},{lon}" target="_blank" rel="noopener" class="mob-btn-map">
        📍 Маршрут
      </a>
    </div>
  </div>

  <script>
    (function() {{
      // 1. Автоматическая актуализация месяца и года
      const now = new Date();
      const months = [
        'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
        'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'
      ];
      const monthName = months[now.getMonth()];
      const year = now.getFullYear();
      const formattedDate = monthName + ' ' + year + ' г.';

      document.querySelectorAll('.sync-date-text').forEach(el => {{
        el.textContent = formattedDate;
      }});

      // 2. Живой статус работы с учетом реального графика ({b['hours']})
      const statusEl = document.getElementById('work-status');
      if (statusEl) {{
        const day = now.getDay(); // 0 — воскресенье
        const hour = now.getHours();
        const min = now.getMinutes();
        const currentMin = hour * 60 + min;

        const openHour = {b['open_hour']};
        const closeHour = {b['close_hour']};
        const closedSunday = {'true' if b['closed_sunday'] else 'false'};

        const openMin = openHour * 60;
        const closeMin = closeHour * 60;
        const warnMin = closeMin - 30;
        const openTimeStr = (openHour < 10 ? '0' + openHour : openHour) + ':00';
        const closeTimeStr = closeHour + ':00';

        if (closedSunday && day === 0) {{
          statusEl.className = 'status-closed';
          statusEl.innerHTML = '<span class="status-dot closed"></span> Сегодня выходной • откроется в Пн в ' + openTimeStr;
        }} else if (currentMin >= openMin && currentMin < warnMin) {{
          statusEl.className = 'status-open';
          statusEl.innerHTML = '<span class="status-dot"></span> Открыто сейчас • до ' + closeTimeStr;
        }} else if (currentMin >= warnMin && currentMin < closeMin) {{
          const leftMin = closeMin - currentMin;
          statusEl.className = 'status-closing-soon';
          statusEl.innerHTML = '<span class="status-dot closing-soon"></span> Скоро закроется • ещё ' + leftMin + ' мин';
        }} else {{
          statusEl.className = 'status-closed';
          statusEl.innerHTML = '<span class="status-dot closed"></span> Сейчас закрыто • откроется в ' + openTimeStr;
        }}
      }}
    }})();
  </script>
</body>
</html>'''

    for folder in ["dist", "docs"]:
        out_dir = os.path.join(base_dir, folder, slug)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_doc)

    # Also update src/template.html with the clean uspeh-777 version so template.html has zero legacy bugs
    if slug == "uspeh-777":
        with open(os.path.join(base_dir, "src", "template.html"), "w", encoding="utf-8") as f:
            f.write(html_doc)

print("SUCCESS: All 5 sites generated and synced to dist/, docs/, and src/template.html!")
