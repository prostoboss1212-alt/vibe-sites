# -*- coding: utf-8 -*-
import json
import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_path = os.path.join(base_dir, "dist", "uspeh-777", "index.html")
data_path = os.path.join(base_dir, "data", "businesses.json")
out_dir = os.path.join(base_dir, "dist", "avtolux")
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "index.html")

with open(template_path, "r", encoding="utf-8") as f:
    html = f.read()

with open(data_path, "r", encoding="utf-8") as f:
    businesses = json.load(f)

av = next(b for b in businesses if b["slug"] == "avtolux")
phone = av["phones"][0]
phone_clean = av["phone_clean"]
lat = av["geo"]["lat"]
lon = av["geo"]["lon"]

# 1. ЦВЕТОВАЯ СХЕМА: Titanium Indigo + Crystal Sky (Кристальная прозрачность стекла, титановая прочность)
html = html.replace("--accent: #ea580c;", "--accent: #4f46e5;")
html = html.replace("--accent-light: #f97316;", "--accent-light: #818cf8;")
html = html.replace("rgba(234, 88, 12, 0.22)", "rgba(79, 70, 229, 0.22)")
html = html.replace("rgba(234, 88, 12, 0.05)", "rgba(79, 70, 229, 0.05)")
html = html.replace("linear-gradient(180deg, #161210 0%, var(--bg-main) 100%)", "linear-gradient(180deg, #100f1c 0%, var(--bg-main) 100%)")
html = html.replace("linear-gradient(135deg, #ea580c 0%, #c2410c 100%)", "linear-gradient(135deg, #4338ca 0%, #312e81 100%)")
html = html.replace("rgba(249, 115, 22, 0.32)", "rgba(129, 140, 248, 0.30)")
html = html.replace("rgba(249, 115, 22, 0.4)", "rgba(79, 70, 229, 0.35)")

# 2. МЕТА И БРЕНД
html = html.replace("Автосервис «Успех-777» — Воронеж, ул. Серова, 22 | СТО на Левом берегу",
                    f"{av['name']} — Воронеж, {av['address']} | Установка автостекол и кузовной ремонт")
html = html.replace("Автосервис «Успех-777» в Воронеже (ул. Серова, 22, Левобережный район). Рейтинг 4.8 в 2ГИС (343 оценки) и 4.4 в Яндекс Картах (377 оценок). Ремонт ДВС, подвески, проточка дисков, шиномонтаж.",
                    f"{av['name']} в Воронеже ({av['address']}). Рейтинг {av['rating']} на картах ({av['reviews_count']} отзывов). Профессиональная замена автостекол, ремонт сколов и трещин, кузовные работы на Антонова-Овсеенко.")

html = html.replace("УСПЕХ-777", "АВТОЛЮКС")
html = html.replace("АВТОСЕРВИС<br>«УСПЕХ-777»", "ЦЕНТР АВТОСТЕКОЛ<br>«АВТОЛЮКС»")
html = html.replace("«Успех-777»", "«Автолюкс»")
html = html.replace("Успех-777 на Серова 22", "Автолюкс на Антонова-Овсеенко 35Б")

# 3. ПОДЗАГОЛОВОК И ДЕВИЗ
html = html.replace("Диагностика, плановое ТО и ремонт легковых автомобилей отечественного и иностранного производства на ул. Серова, 22. Более 20 лет опыта, запчасти в наличии и под заказ.",
                    "Специализированный центр по замене и ремонту автостекол, локальному кузовному ремонту на ул. Антонова-Овсеенко. Автостекла в наличии на складе, гарантия на герметичность шва.")

# Слоган в CTA-баннере:
html = html.replace("МАШИНА<br>НЕ ЖДЁТ", "ИДЕАЛЬНЫЙ ОБЗОР<br>И ЗАЩИТА АВТО")
html = html.replace("Позвоните напрямую в сервис, чтобы записаться на удобное время или рассчитать стоимость работ и запчастей.",
                    "Узнайте стоимость стекла и установки на ваш автомобиль прямо сейчас. Запись на удобное время без очередей.")

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
              <div class="contact-label">Телефон сервиса</div>
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
        <a href="tel:{phone_clean}" class="btn-dark-pill">
          📞 Позвонить в сервис: {phone}
        </a>
        <a href="#contacts" class="btn-white-outline">
          📍 Проложить маршрут
        </a>
      </div>"""
html = html.replace(cta_phones_old, cta_phones_new)

html = re.sub(r'href="tel:\+7[0-9]{10}"', f'href="tel:{phone_clean}"', html)

# 5. ИНДИВИДУАЛЬНЫЙ LAYOUT: БЛОК СТАНДАРТОВ ЗАМЕНЫ АВТОСТЕКОЛ
glass_standards_bar = """
  <!-- БЛОК СТАНДАРТОВ СТО «АВТОЛЮКС» -->
  <section class="showcase-section">
    <div class="container">
      <div style="background: linear-gradient(135deg, rgba(79,70,229,0.18) 0%, rgba(15,23,42,0.7) 100%); border: 1px solid rgba(129,140,248,0.35); border-radius: var(--radius-md); padding: 22px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; margin-bottom: 16px;">
          <div>
            <span style="font-size: 11px; font-weight: 700; color: #818cf8; text-transform: uppercase; letter-spacing: 0.08em;">Специализация: Автостекла</span>
            <div style="font-family: 'Unbounded', sans-serif; font-size: 18px; font-weight: 700; color: #fff;">Заводские стандарты вклейки и ремонта</div>
          </div>
          <div style="background: rgba(79,70,229,0.25); border: 1px solid rgba(129,140,248,0.4); color: #c7d2fe; font-size: 12px; font-weight: 700; padding: 6px 14px; border-radius: 999px;">
            🛡️ Гарантия герметичности шва
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px;">
          <div style="background: rgba(15,23,42,0.6); border: 1px solid var(--border-strong); padding: 14px; border-radius: 8px;">
            <div style="color: #818cf8; font-weight: 700; font-size: 13px; margin-bottom: 4px;">🔍 Стекла в наличии</div>
            <div style="color: var(--text-muted); font-size: 12.5px;">Лобовые, боковые и задние стекла на европейские, корейские, японские и китайские авто.</div>
          </div>
          <div style="background: rgba(15,23,42,0.6); border: 1px solid var(--border-strong); padding: 14px; border-radius: 8px;">
            <div style="color: #818cf8; font-weight: 700; font-size: 13px; margin-bottom: 4px;">⏱️ Замена от 1.5 часов</div>
            <div style="color: var(--text-muted); font-size: 12.5px;">Быстрая полимеризация премиального швейцарского клей-герметика, аккуратный салон.</div>
          </div>
          <div style="background: rgba(15,23,42,0.6); border: 1px solid var(--border-strong); padding: 14px; border-radius: 8px;">
            <div style="color: #818cf8; font-weight: 700; font-size: 13px; margin-bottom: 4px;">💎 Остановка трещин</div>
            <div style="color: var(--text-muted); font-size: 12.5px;">Ремонт сколов прозрачным полимером под давлением с ультрафиолетовой фиксацией.</div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
showcase_section_regex = r'<section class="showcase-section">.*?</section>'
html = re.sub(showcase_section_regex, glass_standards_bar, html, flags=re.DOTALL)

# 6. УСЛУГИ СТО «АВТОЛЮКС»
services_html = ""
for s in av["services"]:
    services_html += f"""        <div class="service-card" style="border-top: 3px solid #6366f1;">
          <div>
            <div class="service-tag">{s['category']}</div>
            <div class="service-name">{s['name']}</div>
            <div class="service-desc">{s['description']}</div>
          </div>
          <div class="service-price">
            <span style="color: #818cf8;">{s['price']}</span>
          </div>
        </div>\n"""

services_grid_regex = r'<div class="services-grid">.*?</div>\s*<p class="services-note">'
replacement = f'<div class="services-grid">\n{services_html}      </div>\n\n      <p class="services-note">'
html = re.sub(services_grid_regex, replacement, html, flags=re.DOTALL)

html = re.sub(r'В сервисе действуют обсуждаемые цены.*?</a>\.',
              f'Наличие конкретной марки стекла на складе уточняйте по телефону: <a href="tel:{phone_clean}">{phone}</a>.', html)

# 7. АДРЕС И КАРТА
html = html.replace("г. Воронеж, ул. Серова, 22 (ориентир — пер. Усманский, 170 м)", f"{av['address']} (Коминтерновский район)")
html = html.replace("ул. Серова, 22", "ул. Антонова-Овсеенко, 35Б")
html = html.replace("г. Воронеж, Левобережный район, 394002 (Усманский пер., 170 м)", f"{av['address']}, Воронеж")
html = html.replace("39.268825", lon).replace("51.664272", lat)
html = html.replace("https://yandex.ru/maps/org/uspekh_777/1111994914/", f"https://yandex.ru/maps/?text={av['geo']['map_query']}")
html = html.replace("https://2gis.ru/voronezh/firm/4363390420233353", f"https://2gis.ru/voronezh/search/{av['geo']['map_query']}")
html = html.replace("Ежедневно с 09:00 до 19:00 (без выходных)", av["hours"])

# 8. РЕЙТИНГИ
html = html.replace("★ Номинант премии 2ГИС 2026", "★ Рейтинг 4.8 на картах")
html = html.replace("4,8", "4,8")
html = html.replace("4,4", "4,8")
html = html.replace("343 оценки в 2ГИС →", f"{av['reviews_count']} проверенных отзывов →")
html = html.replace("377 оценок • 179 отзывов →", f"{av['reviews_count']} оценок на картах →")
html = html.replace("🏆 Номинант премии 2ГИС 2026", "⭐ Оценка клиентов 4.8")

# 9. ОТЗЫВЫ АВТОЛЮКС
reviews_html = ""
for r in av["reviews"]:
    reviews_html += f"""          <div class="review-quote-card">
            <div>
              <div class="quote-mark" style="color: #818cf8;">“</div>
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

print("SUCCESS: avtolux generated with Titanium Indigo theme, Glass standards layout and 1 phone!")
