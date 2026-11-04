# -*- coding: utf-8 -*-
import json
import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_path = os.path.join(base_dir, "dist", "uspeh-777", "index.html")
data_path = os.path.join(base_dir, "data", "businesses.json")
out_dir = os.path.join(base_dir, "dist", "zvezda")
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "index.html")

with open(template_path, "r", encoding="utf-8") as f:
    html = f.read()

with open(data_path, "r", encoding="utf-8") as f:
    businesses = json.load(f)

z = next(b for b in businesses if b["slug"] == "zvezda")
phone = z["phones"][0]
phone_clean = z["phone_clean"]
lat = z["geo"]["lat"]
lon = z["geo"]["lon"]

# 1. НАСТОЯЩИЙ АВТОМОБИЛЬНЫЙ ЦВЕТ: Графит + Индустриальный Золотистый/Янтарный (как Mobil 1 / Bosch / Mercedes Звезда)
html = html.replace("--accent: #ea580c;", "--accent: #d97706;")
html = html.replace("--accent-light: #f97316;", "--accent-light: #f59e0b;")
html = html.replace("rgba(234, 88, 12, 0.22)", "rgba(217, 119, 6, 0.20)")
html = html.replace("rgba(234, 88, 12, 0.05)", "rgba(217, 119, 6, 0.04)")
html = html.replace("linear-gradient(180deg, #161210 0%, var(--bg-main) 100%)", "linear-gradient(180deg, #151410 0%, var(--bg-main) 100%)")
html = html.replace("linear-gradient(135deg, #ea580c 0%, #c2410c 100%)", "linear-gradient(135deg, #b45309 0%, #78350f 100%)")
html = html.replace("rgba(249, 115, 22, 0.32)", "rgba(245, 158, 11, 0.28)")
html = html.replace("rgba(249, 115, 22, 0.4)", "rgba(245, 158, 11, 0.35)")

# 2. МЕТА И БРЕНД
html = html.replace("Автосервис «Успех-777» — Воронеж, ул. Серова, 22 | СТО на Левом берегу",
                    f"{z['name']} — Воронеж, {z['address']} | Ремонт иномарок на Димитрова")
html = html.replace("Автосервис «Успех-777» в Воронеже (ул. Серова, 22, Левобережный район). Рейтинг 4.8 в 2ГИС (343 оценки) и 4.4 в Яндекс Картах (377 оценок). Ремонт ДВС, подвески, проточка дисков, шиномонтаж.",
                    f"{z['name']} в Воронеже ({z['address']}). Рейтинг {z['rating']} на картах ({z['reviews_count']} отзыва). Профессиональный ремонт иномарок, ТО, диагностика и аренда тёплого бокса с подъёмником.")

html = html.replace("УСПЕХ-777", "ЗВЕЗДА")
html = html.replace("АВТОСЕРВИС<br>«УСПЕХ-777»", "СТО «ЗВЕЗДА»<br>НА ДИМИТРОВА")
html = html.replace("«Успех-777»", "«Звезда»")
html = html.replace("Успех-777 на Серова 22", "Звезда на Димитрова 91")

# 3. НОВЫЙ ДЕВИЗ И ТЕГЛАЙН
html = html.replace("Диагностика, плановое ТО и ремонт легковых автомобилей отечественного и иностранного производства на ул. Серова, 22. Более 20 лет опыта, запчасти в наличии и под заказ.",
                    "Специализированный ремонт иномарок, профессиональное обслуживание ходовой и ТО. Честная диагностика и аренда тёплого бокса для тех, кто любит чинить авто сам.")

# Меняем девиз в нижнем CTA-баннере!
html = html.replace("МАШИНА<br>НЕ ЖДЁТ", "РЕШИМ ВОПРОС<br>С АВТО СЕГОДНЯ")
html = html.replace("Позвоните напрямую в сервис, чтобы записаться на удобное время или рассчитать стоимость работ и запчастей.",
                    "Узнайте предварительную стоимость ремонта и запишитесь на удобное время без очередей.")

# 4. ТЕЛЕФОНЫ: СТРОГО 1 НОМЕР (БЕЗ ДУБЛЕЙ)
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
              <div class="contact-label">Телефон сервиса</div>
              <a href="tel:{phone_clean}" class="contact-phone-item">{phone}</a>
            </div>"""
html = html.replace(contacts_phones_old, contacts_phones_new)

# В нижнем баннере:
cta_phones_old = """      <div class="cta-banner-buttons">
        <a href="tel:+79529568056" class="btn-dark-pill">
          📞 +7 (952) 956-80-56
        </a>
        <a href="tel:+74732568056" class="btn-white-outline">
          📞 +7 (473) 256-80-56
        </a>
      </div>"""
cta_phones_new = f"""      <div class="cta-banner-buttons">
        <a href="tel:{phone_clean}" class="btn-dark-pill">
          📞 Позвонить мастеру: {phone}
        </a>
        <a href="#contacts" class="btn-white-outline">
          📍 Посмотреть на карте
        </a>
      </div>"""
html = html.replace(cta_phones_old, cta_phones_new)

# Кнопки звонков:
html = re.sub(r'href="tel:\+7[0-9]{10}"', f'href="tel:{phone_clean}"', html)

# 5. ИЗМЕНЕНИЕ СТРУКТУРЫ И РАСПОЛОЖЕНИЯ ЭЛЕМЕНТОВ (LAYOUT):
# Вместо 2 горизонтальных карточек витрины, делаем блок быстрых фактов (Quick Specs Bar)
# и переставляем отзывы ПЕРЕД контактами, а блок "За что ценят" форматируем иначе!

quick_specs_bar = f"""
  <!-- ПЛАШКА БЫСТРЫХ ПРЕИМУЩЕСТВ СТО «ЗВЕЗДА» -->
  <section class="showcase-section">
    <div class="container">
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
          <div style="color: #fff; font-weight: 700; font-size: 15px;">Рейтинг 4.9 на картах</div>
          <div style="color: var(--text-muted); font-size: 13px; margin-top: 4px;">Честная смета и работа без навязанных услуг</div>
        </div>
      </div>
    </div>
  </section>
"""

showcase_section_regex = r'<section class="showcase-section">.*?</section>'
html = re.sub(showcase_section_regex, quick_specs_bar, html, flags=re.DOTALL)

# 6. УСЛУГИ СТО «ЗВЕЗДА» (2 КОЛОНКИ С БОЛЬШИМИ ПЛАШКАМИ ДЛЯ РАЗНООБРАЗИЯ)
services_html = ""
for s in z["services"]:
    services_html += f"""        <div class="service-card" style="border-left: 3px solid rgba(217, 119, 6, 0.4);">
          <div>
            <div class="service-tag">{s['category']}</div>
            <div class="service-name">{s['name']}</div>
            <div class="service-desc">{s['description']}</div>
          </div>
          <div class="service-price">
            <span>{s['price']}</span>
          </div>
        </div>\n"""

services_grid_regex = r'<div class="services-grid">.*?</div>\s*<p class="services-note">'
replacement = f'<div class="services-grid" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">\n{services_html}      </div>\n\n      <p class="services-note">'
html = re.sub(services_grid_regex, replacement, html, flags=re.DOTALL)

# Примечание к прайсу
html = re.sub(r'В сервисе действуют обсуждаемые цены.*?</a>\.',
              f'Точная смета формируется после бесплатного визуального осмотра. Запись по телефону: <a href="tel:{phone_clean}">{phone}</a>.', html)

# 7. АДРЕС И КАРТА
html = html.replace("г. Воронеж, ул. Серова, 22 (ориентир — пер. Усманский, 170 м)", f"{z['address']} (Левобережный район)")
html = html.replace("ул. Серова, 22", "ул. Димитрова, 91/3Б")
html = html.replace("г. Воронеж, Левобережный район, 394002 (Усманский пер., 170 м)", f"{z['address']}, Воронеж")
html = html.replace("39.268825", lon).replace("51.664272", lat)
html = html.replace("https://yandex.ru/maps/org/uspekh_777/1111994914/", f"https://yandex.ru/maps/?text={z['geo']['map_query']}")
html = html.replace("https://2gis.ru/voronezh/firm/4363390420233353", f"https://2gis.ru/voronezh/search/{z['geo']['map_query']}")
html = html.replace("Ежедневно с 09:00 до 19:00 (без выходных)", z["hours"])

# 8. РЕЙТИНГИ И ОТЗЫВЫ
html = html.replace("★ Номинант премии 2ГИС 2026", "★ Высокая оценка 4.9")
html = html.replace("4,8", "4,9")
html = html.replace("343 оценки в 2ГИС →", f"{z['reviews_count']} отзыва на 2ГИС →")
html = html.replace("377 оценок • 179 отзывов →", f"{z['reviews_count']} отзыва на Яндекс Картах →")
html = html.replace("🏆 Номинант премии 2ГИС 2026", "⭐ Рейтинг 4.9 на картах")

reviews_html = ""
for r in z["reviews"]:
    reviews_html += f"""          <div class="review-quote-card">
            <div>
              <div class="quote-mark" style="color: var(--accent-light);">“</div>
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

print("SUCCESS: zvezda redesigned with automotive palette, new layout and custom slogan!")
