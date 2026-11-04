# -*- coding: utf-8 -*-
import json
import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_path = os.path.join(base_dir, "dist", "uspeh-777", "index.html")
data_path = os.path.join(base_dir, "data", "businesses.json")
out_dir = os.path.join(base_dir, "dist", "avtoray")
os.makedirs(out_dir, exist_ok=True)
out_file = os.path.join(out_dir, "index.html")

with open(template_path, "r", encoding="utf-8") as f:
    html = f.read()

with open(data_path, "r", encoding="utf-8") as f:
    businesses = json.load(f)

a = next(b for b in businesses if b["slug"] == "avtoray")
phone = a["phones"][0]
phone_clean = a["phone_clean"]
lat = a["geo"]["lat"]
lon = a["geo"]["lon"]

# 1. ЦВЕТОВАЯ СХЕМА: Изумрудный Racing Green + Нефрит (Надежность, безопасность, чистый ремонт)
html = html.replace("--accent: #ea580c;", "--accent: #059669;")
html = html.replace("--accent-light: #f97316;", "--accent-light: #10b981;")
html = html.replace("rgba(234, 88, 12, 0.22)", "rgba(5, 150, 105, 0.22)")
html = html.replace("rgba(234, 88, 12, 0.05)", "rgba(5, 150, 105, 0.05)")
html = html.replace("linear-gradient(180deg, #161210 0%, var(--bg-main) 100%)", "linear-gradient(180deg, #0a1612 0%, var(--bg-main) 100%)")
html = html.replace("linear-gradient(135deg, #ea580c 0%, #c2410c 100%)", "linear-gradient(135deg, #047857 0%, #064e3b 100%)")
html = html.replace("rgba(249, 115, 22, 0.32)", "rgba(16, 185, 129, 0.28)")
html = html.replace("rgba(249, 115, 22, 0.4)", "rgba(5, 150, 105, 0.35)")

# 2. МЕТА И БРЕНД
html = html.replace("Автосервис «Успех-777» — Воронеж, ул. Серова, 22 | СТО на Левом берегу",
                    f"{a['name']} — Воронеж, {a['address']} | Ремонт подвески и ТО на Богатырской")
html = html.replace("Автосервис «Успех-777» в Воронеже (ул. Серова, 22, Левобережный район). Рейтинг 4.8 в 2ГИС (343 оценки) и 4.4 в Яндекс Картах (377 оценок). Ремонт ДВС, подвески, проточка дисков, шиномонтаж.",
                    f"{a['name']} в Воронеже ({a['address']}). Рейтинг {a['rating']} на картах ({a['reviews_count']} отзывов). Надежный ремонт подвески, слесарные работы, замена ГРМ и масел в Железнодорожном районе.")

html = html.replace("УСПЕХ-777", "АВТОРАЙ")
html = html.replace("АВТОСЕРВИС<br>«УСПЕХ-777»", "АВТОСЕРВИС<br>«АВТОРАЙ»")
html = html.replace("«Успех-777»", "«Авторай»")
html = html.replace("Успех-777 на Серова 22", "Авторай на Богатырской 9/2")

# 3. ПОДЗАГОЛОВОК И ДЕВИЗ
html = html.replace("Диагностика, плановое ТО и ремонт легковых автомобилей отечественного и иностранного производства на ул. Серова, 22. Более 20 лет опыта, запчасти в наличии и под заказ.",
                    "Честное техобслуживание и ремонт ходовой в Железнодорожном районе. Открытая ремзона, осмотр на подъёмнике при вас и прозрачные цены без накруток.")

# Слоган в CTA-баннере:
html = html.replace("МАШИНА<br>НЕ ЖДЁТ", "РЕМОНТ БЕЗ НЕРВОВ<br>И ПЕРЕПЛАТ")
html = html.replace("Позвоните напрямую в сервис, чтобы записаться на удобное время или рассчитать стоимость работ и запчастей.",
                    "Приезжайте на честную диагностику на Богатырской. Покажем все неисправности лично и назовем фиксированную стоимость.")

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
          📞 Позвонить мастеру: {phone}
        </a>
        <a href="#contacts" class="btn-white-outline">
          📍 Как проехать
        </a>
      </div>"""
html = html.replace(cta_phones_old, cta_phones_new)

html = re.sub(r'href="tel:\+7[0-9]{10}"', f'href="tel:{phone_clean}"', html)

# 5. ИНДИВИДУАЛЬНЫЙ LAYOUT: БЛОК ПРИНЦИПОВ ЧЕСТНОГО РЕМОНТА
principles_bar = """
  <!-- БЛОК ПРИНЦИПОВ СТО «АВТОРАЙ» -->
  <section class="showcase-section">
    <div class="container">
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
            <span style="font-family: 'Unbounded', sans-serif; font-size: 14px; font-weight: 700; color: #fff;">Запчасти за 40 минут</span>
          </div>
          <div style="color: var(--text-muted); font-size: 13px; line-height: 1.45;">
            Быстрый подбор качественных дубликатов и оригиналов. Детали привозят курьером прямо в сервис без вашего участия.
          </div>
        </div>
      </div>
    </div>
  </section>
"""
showcase_section_regex = r'<section class="showcase-section">.*?</section>'
html = re.sub(showcase_section_regex, principles_bar, html, flags=re.DOTALL)

# 6. УСЛУГИ СТО «АВТОРАЙ»
services_html = ""
for s in a["services"]:
    services_html += f"""        <div class="service-card" style="border-left: 3px solid #059669;">
          <div>
            <div class="service-tag">{s['category']}</div>
            <div class="service-name">{s['name']}</div>
            <div class="service-desc">{s['description']}</div>
          </div>
          <div class="service-price">
            <span style="color: #34d399;">{s['price']}</span>
          </div>
        </div>\n"""

services_grid_regex = r'<div class="services-grid">.*?</div>\s*<p class="services-note">'
replacement = f'<div class="services-grid">\n{services_html}      </div>\n\n      <p class="services-note">'
html = re.sub(services_grid_regex, replacement, html, flags=re.DOTALL)

html = re.sub(r'В сервисе действуют обсуждаемые цены.*?</a>\.',
              f'Точная смета формируется после бесплатного осмотра на подъемнике. Звоните: <a href="tel:{phone_clean}">{phone}</a>.', html)

# 7. АДРЕС И КАРТА
html = html.replace("г. Воронеж, ул. Серова, 22 (ориентир — пер. Усманский, 170 м)", f"{a['address']} (Железнодорожный район)")
html = html.replace("ул. Серова, 22", "ул. Богатырская, 9/2")
html = html.replace("г. Воронеж, Левобережный район, 394002 (Усманский пер., 170 м)", f"{a['address']}, Воронеж")
html = html.replace("39.268825", lon).replace("51.664272", lat)
html = html.replace("https://yandex.ru/maps/org/uspekh_777/1111994914/", f"https://yandex.ru/maps/?text={a['geo']['map_query']}")
html = html.replace("https://2gis.ru/voronezh/firm/4363390420233353", f"https://2gis.ru/voronezh/search/{a['geo']['map_query']}")
html = html.replace("Ежедневно с 09:00 до 19:00 (без выходных)", a["hours"])

# 8. РЕЙТИНГИ
html = html.replace("★ Номинант премии 2ГИС 2026", "★ Рейтинг 4.8 на картах")
html = html.replace("4,8", "4,8")
html = html.replace("4,4", "4,8")
html = html.replace("343 оценки в 2ГИС →", f"{a['reviews_count']} проверенных отзывов →")
html = html.replace("377 оценок • 179 отзывов →", f"{a['reviews_count']} оценок на картах →")
html = html.replace("🏆 Номинант премии 2ГИС 2026", "⭐ Высокая оценка клиентов 4.8")

# 9. ОТЗЫВЫ АВТОРАЙ
reviews_html = ""
for r in a["reviews"]:
    reviews_html += f"""          <div class="review-quote-card">
            <div>
              <div class="quote-mark" style="color: #10b981;">“</div>
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

print("SUCCESS: avtoray generated with Emerald Green theme, Open-Workshop layout and 1 phone!")
