# -*- coding: utf-8 -*-
import json
import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_path = os.path.join(base_dir, "dist", "uspeh-777", "index.html")
data_path = os.path.join(base_dir, "data", "businesses.json")
out_dir = os.path.join(base_dir, "dist", "careta")
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "index.html")

with open(template_path, "r", encoding="utf-8") as f:
    html = f.read()

with open(data_path, "r", encoding="utf-8") as f:
    businesses = json.load(f)

c = next(b for b in businesses if b["slug"] == "careta")
phone = c["phones"][0]
phone_clean = c["phone_clean"]
lat = c["geo"]["lat"]
lon = c["geo"]["lon"]

# 1. ЦВЕТОВАЯ СХЕМА: High-Tech Cobalt & Cyan (Bosch / BMW / Дилерский авто-синий)
html = html.replace("--accent: #ea580c;", "--accent: #2563eb;")
html = html.replace("--accent-light: #f97316;", "--accent-light: #38bdf8;")
html = html.replace("rgba(234, 88, 12, 0.22)", "rgba(37, 99, 235, 0.22)")
html = html.replace("rgba(234, 88, 12, 0.05)", "rgba(37, 99, 235, 0.06)")
html = html.replace("linear-gradient(180deg, #161210 0%, var(--bg-main) 100%)", "linear-gradient(180deg, #0e1726 0%, var(--bg-main) 100%)")
html = html.replace("linear-gradient(135deg, #ea580c 0%, #c2410c 100%)", "linear-gradient(135deg, #1d4ed8 0%, #0f172a 100%)")
html = html.replace("rgba(249, 115, 22, 0.32)", "rgba(56, 189, 248, 0.30)")
html = html.replace("rgba(249, 115, 22, 0.4)", "rgba(37, 99, 235, 0.35)")

# 2. МЕТА И БРЕНД
html = html.replace("Автосервис «Успех-777» — Воронеж, ул. Серова, 22 | СТО на Левом берегу",
                    f"{c['name']} — Воронеж, {c['address']} | Мультибрендовый техцентр")
html = html.replace("Автосервис «Успех-777» в Воронеже (ул. Серова, 22, Левобережный район). Рейтинг 4.8 в 2ГИС (343 оценки) и 4.4 в Яндекс Картах (377 оценок). Ремонт ДВС, подвески, проточка дисков, шиномонтаж.",
                    f"{c['name']} в Воронеже ({c['address']}). Оценка {c['rating']} на картах ({c['reviews_count']} отзывов). Обслуживание европейских, корейских и китайских автомобилей, ТО, подвеска, автокондиционеры.")

html = html.replace("УСПЕХ-777", "CARETA")
html = html.replace("АВТОСЕРВИС<br>«УСПЕХ-777»", "ТЕХЦЕНТР<br>«CARETA»")
html = html.replace("«Успех-777»", "«Careta»")
html = html.replace("Успех-777 на Серова 22", "Careta на Димитрова 112")

# 3. ДЕВИЗ И ПОДЗАГОЛОВОК
html = html.replace("Диагностика, плановое ТО и ремонт легковых автомобилей отечественного и иностранного производства на ул. Серова, 22. Более 20 лет опыта, запчасти в наличии и под заказ.",
                    "Современный мультибрендовый сервис на ул. Димитрова. Профессиональное оборудование, обслуживание китайских, корейских и европейских авто с гарантией качества.")

# Слоган в CTA:
html = html.replace("МАШИНА<br>НЕ ЖДЁТ", "БЕЗУПРЕЧНЫЙ СЕРВИС<br>С ОЦЕНКОЙ 5.0")
html = html.replace("Позвоните напрямую в сервис, чтобы записаться на удобное время или рассчитать стоимость работ и запчастей.",
                    "Запишитесь на плановое ТО или диагностику в удобное время. Честные цены и фиксированная смета до начала работ.")

# 4. ТЕЛЕФОНЫ: СТРОГО 1 НОМЕР
html = re.sub(r'<a href="tel:\+7[0-9]{10}" class="nav-cta">.*?</a>',
              f'<a href="tel:{phone_clean}" class="nav-cta">{phone}</a>', html)

# В Hero:
hero_phones_old = """          <div class="hero-phones-row">
            <a href="tel:+79529568056" class="hero-phone-big">+7 (952) 956-80-56</a>
            <a href="tel:+74732568056" class="hero-phone-secondary">+7 (473) 256-80-56</a>
          </div>"""
hero_phones_new = f"""          <div class="hero-phones-row">
            <a href="tel:{phone_clean}" class="hero-phone-big">{phone}</a>
          </div>"""
html = html.replace(hero_phones_old, hero_phones_new)

# В Контактах:
contacts_phones_old = """            <div class="contact-block">
              <div class="contact-label">Телефоны сервиса</div>
              <a href="tel:+79529568056" class="contact-phone-item">+7 (952) 956-80-56</a>
              <a href="tel:+74732568056" class="contact-phone-item">+7 (473) 256-80-56</a>
              <a href="tel:+79290111777" class="contact-phone-item">+7 (929) 011-17-77</a>
            </div>"""
contacts_phones_new = f"""            <div class="contact-block">
              <div class="contact-label">Телефон для записи</div>
              <a href="tel:{phone_clean}" class="contact-phone-item">{phone}</a>
            </div>"""
html = html.replace(contacts_phones_old, contacts_phones_new)

# В CTA:
cta_phones_old = """      <div class="cta-banner-buttons">
        <a href="tel:+79529568056" class="btn-dark-pill">
          📞 +7 (952) 956-80-56
        </a>
        <a href="tel:+74732568056" class="btn-white-outline">
          📞 +7 (473) 256-80-56
        </a>
      </div>"""
cta_phones_new = f"""      <div class="cta-banner-buttons">
        <a href="tel:{phone_clean}" class="btn-dark-pill" style="border: 1px solid var(--accent-light);">
          📞 Позвонить в техцентр: {phone}
        </a>
        <a href="#contacts" class="btn-white-outline">
          📍 Схема проезда
        </a>
      </div>"""
html = html.replace(cta_phones_old, cta_phones_new)

html = re.sub(r'href="tel:\+7[0-9]{10}"', f'href="tel:{phone_clean}"', html)

# 5. ИНДИВИДУАЛЬНЫЙ LAYOUT: БЛОК МУЛЬТИБРЕНДОВ ВМЕСТО ШОУКЕЙСА
brand_chips = """
  <!-- МУЛЬТИБРЕНДОВЫЙ БЛОК CARETA -->
  <section class="showcase-section">
    <div class="container">
      <div style="background: linear-gradient(135deg, rgba(37,99,235,0.15) 0%, rgba(15,23,42,0.6) 100%); border: 1px solid rgba(56,189,248,0.3); border-radius: var(--radius-md); padding: 22px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 14px;">
          <div>
            <span style="font-size: 11px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.08em;">Мультибренд 2026</span>
            <div style="font-family: 'Unbounded', sans-serif; font-size: 18px; font-weight: 700; color: #fff;">Обслуживаем автомобили любого класса</div>
          </div>
          <div style="background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.4); color: #34d399; font-size: 12px; font-weight: 700; padding: 6px 12px; border-radius: 999px;">
            ✓ 100% честные отзывы на 5.0
          </div>
        </div>
        <div style="display: flex; flex-wrap: wrap; gap: 8px;">
          <span style="background: rgba(255,255,255,0.06); border: 1px solid var(--border-strong); padding: 5px 12px; border-radius: 6px; font-size: 12px; color: #e2e8f0;">🇨🇳 Haval / Chery / Geely / Changan</span>
          <span style="background: rgba(255,255,255,0.06); border: 1px solid var(--border-strong); padding: 5px 12px; border-radius: 6px; font-size: 12px; color: #e2e8f0;">🇰🇷 Kia / Hyundai / Genesis</span>
          <span style="background: rgba(255,255,255,0.06); border: 1px solid var(--border-strong); padding: 5px 12px; border-radius: 6px; font-size: 12px; color: #e2e8f0;">🇩🇪 VAG / BMW / Mercedes</span>
          <span style="background: rgba(255,255,255,0.06); border: 1px solid var(--border-strong); padding: 5px 12px; border-radius: 6px; font-size: 12px; color: #e2e8f0;">🇯🇵 Toyota / Nissan / Mazda</span>
        </div>
      </div>
    </div>
  </section>
"""
showcase_section_regex = r'<section class="showcase-section">.*?</section>'
html = re.sub(showcase_section_regex, brand_chips, html, flags=re.DOTALL)

# 6. УСЛУГИ СТО CARETA
services_html = ""
for s in c["services"]:
    services_html += f"""        <div class="service-card" style="border-top: 3px solid var(--accent-light);">
          <div>
            <div class="service-tag">{s['category']}</div>
            <div class="service-name">{s['name']}</div>
            <div class="service-desc">{s['description']}</div>
          </div>
          <div class="service-price">
            <span style="color: #38bdf8;">{s['price']}</span>
          </div>
        </div>\n"""

services_grid_regex = r'<div class="services-grid">.*?</div>\s*<p class="services-note">'
replacement = f'<div class="services-grid">\n{services_html}      </div>\n\n      <p class="services-note">'
html = re.sub(services_grid_regex, replacement, html, flags=re.DOTALL)

html = re.sub(r'В сервисе действуют обсуждаемые цены.*?</a>\.',
              f'Стоимость запчастей и регламентных работ рассчитывается по VIN-номеру. Звоните: <a href="tel:{phone_clean}">{phone}</a>.', html)

# 7. АДРЕС И КАРТА
html = html.replace("г. Воронеж, ул. Серова, 22 (ориентир — пер. Усманский, 170 м)", f"{c['address']} (Левобережный район)")
html = html.replace("ул. Серова, 22", "ул. Димитрова, 112/3")
html = html.replace("г. Воронеж, Левобережный район, 394002 (Усманский пер., 170 м)", f"{c['address']}, Воронеж")
html = html.replace("39.268825", lon).replace("51.664272", lat)
html = html.replace("https://yandex.ru/maps/org/uspekh_777/1111994914/", f"https://yandex.ru/maps/?text={c['geo']['map_query']}")
html = html.replace("https://2gis.ru/voronezh/firm/4363390420233353", f"https://2gis.ru/voronezh/search/{c['geo']['map_query']}")
html = html.replace("Ежедневно с 09:00 до 19:00 (без выходных)", c["hours"])

# 8. РЕЙТИНГИ 5.0
html = html.replace("★ Номинант премии 2ГИС 2026", "⭐ Идеальная оценка 5.0")
html = html.replace("4,8", "5,0")
html = html.replace("4,4", "5,0")
html = html.replace("343 оценки в 2ГИС →", f"{c['reviews_count']} отзывов на картах →")
html = html.replace("377 оценок • 179 отзывов →", f"{c['reviews_count']} подтвержденных отзывов →")
html = html.replace("🏆 Номинант премии 2ГИС 2026", "🏆 100% рекомендаций клиентов")

# 9. ОТЗЫВЫ CARETA
reviews_html = ""
for r in c["reviews"]:
    reviews_html += f"""          <div class="review-quote-card">
            <div>
              <div class="quote-mark" style="color: #38bdf8;">“</div>
              <p class="review-body">
                {r['text']}
              </p>
            </div>
            <div class="review-meta">
              <span>{r['author_note']}</span>
              <span style="color: #fbbf24;">★★★★★</span>
            </div>
          </div>\n"""

reviews_grid_regex = r'<div class="reviews-cards-grid">.*?</div>\s*</div>\s*<p class="reviews-footnote">'
reviews_replacement = f'<div class="reviews-cards-grid">\n{reviews_html}        </div>\n      </div>\n\n      <p class="reviews-footnote">'
html = re.sub(reviews_grid_regex, reviews_replacement, html, flags=re.DOTALL)

with open(out_file, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: careta generated with Cobalt/Cyan palette, brand chips layout and 5.0 slogan!")
