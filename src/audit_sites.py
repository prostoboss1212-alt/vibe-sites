# -*- coding: utf-8 -*-
import json
import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "businesses.json")
dist_dir = os.path.join(base_dir, "dist")

with open(data_path, "r", encoding="utf-8") as f:
    businesses = json.load(f)

sites = ["uspeh-777", "zvezda", "careta", "avtoray", "avtolux"]
issues = []
report = []

for slug in sites:
    filepath = os.path.join(dist_dir, slug, "index.html")
    if not os.path.exists(filepath):
        issues.append(f"[{slug}] Файл не найден: {filepath}")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    biz = next(b for b in businesses if b["slug"] == slug)
    site_report = {"slug": slug, "name": biz["name"], "checks": {}}
    
    # 1. Проверка плейсхолдеров и артефактов
    placeholders = ["undefined", "null", "NaN", "TODO", "lorem", "{", "}"]
    bad_ph = [p for p in placeholders if p in html and p not in ["{", "}"]] # { } are in CSS
    if bad_ph:
        issues.append(f"[{slug}] Найдены плейсхолдеры: {bad_ph}")
    site_report["checks"]["placeholders"] = "PASS" if not bad_ph else f"FAIL ({bad_ph})"

    # 2. Проверка чужих брендов / кросс-контаминации
    other_slugs = [s for s in sites if s != slug]
    leaks = []
    for other in other_slugs:
        other_biz = next(b for b in businesses if b["slug"] == other)
        # Проверяем чистое название без кавычек
        clean_other_name = other_biz["name"].replace("Автосервис", "").replace("«", "").replace("»", "").strip()
        # Для uspeh-777 отдельная проверка
        if clean_other_name.lower() in html.lower() and clean_other_name.lower() not in biz["name"].lower():
            # исключение если случайно совпало слово
            leaks.append(f"Упоминание '{clean_other_name}'")
        
        # Проверяем чужой адрес
        other_street = other_biz["address"].split(",")[1].strip() if "," in other_biz["address"] else other_biz["address"]
        if other_street.lower() in html.lower() and other_street.lower() not in biz["address"].lower():
            leaks.append(f"Чужая улица: '{other_street}'")
            
        # Проверяем чужой телефон
        for other_p in other_biz["phones"]:
            if other_p in html and other_p not in biz["phones"]:
                leaks.append(f"Чужой телефон: '{other_p}'")
                
    if leaks:
        issues.append(f"[{slug}] Кросс-контаминация (утечки чужих данных): {leaks}")
    site_report["checks"]["cross_contamination"] = "PASS" if not leaks else f"FAIL: {leaks}"

    # 3. Проверка номеров телефонов
    tel_links = re.findall(r'href="tel:(.*?)"', html)
    tel_texts = re.findall(r'\+7\s*\([0-9]{3}\)\s*[0-9]{3}-[0-9]{2}-[0-9]{2}', html)
    
    # Все tel: должны быть валидными
    invalid_tels = [t for t in tel_links if not re.match(r'^\+7\d{10}$', t)]
    if invalid_tels:
        issues.append(f"[{slug}] Некорректные tel-ссылки: {invalid_tels}")
    
    # Если телефон 1, проверяем отсутствие других номеров
    if len(biz["phones"]) == 1:
        expected_clean = biz["phone_clean"]
        wrong_tels = [t for t in tel_links if t != expected_clean]
        if wrong_tels:
            issues.append(f"[{slug}] Обнаружены не те телефоны в tel: {wrong_tels}")
            
        expected_formatted = biz["phones"][0]
        wrong_texts = [t for t in tel_texts if t != expected_formatted]
        if wrong_texts:
            issues.append(f"[{slug}] Обнаружены чужие текстовые телефоны: {wrong_texts}")
            
    site_report["checks"]["phones"] = f"PASS (Найдено {len(set(tel_links))} уник. ссылок tel:)"

    # 4. Проверка координат и карты
    lat = biz["geo"]["lat"]
    lon = biz["geo"]["lon"]
    has_coords = lat in html and lon in html
    if not has_coords:
        issues.append(f"[{slug}] В коде отсутствуют точные координаты {lat}, {lon}")
    site_report["checks"]["geo"] = "PASS" if has_coords else "FAIL"

    # 5. Проверка noindex и дисклеймера
    has_noindex = '<meta name="robots" content="noindex, nofollow">' in html
    has_disclaimer = 'Не является публичной офертой' in html
    if not has_noindex or not has_disclaimer:
        issues.append(f"[{slug}] Ошибка: нет noindex или дисклеймера")
    site_report["checks"]["legal"] = "PASS" if (has_noindex and has_disclaimer) else "FAIL"

    # 6. Проверка живого JS (ноябрь 2026 и статус)
    has_js_date = 'sync-date-text' in html
    has_js_status = 'work-status' in html
    if not has_js_date or not has_js_status:
        issues.append(f"[{slug}] Ошибка: нет скрипта даты или статуса")
    site_report["checks"]["live_scripts"] = "PASS" if (has_js_date and has_js_status) else "FAIL"

    report.append(site_report)

# Проверка dist/index.html (хаб)
hub_path = os.path.join(dist_dir, "index.html")
if os.path.exists(hub_path):
    with open(hub_path, "r", encoding="utf-8") as f:
        hub_html = f.read()
    hub_links = re.findall(r'href="\./(.*?)/index\.html"', hub_html)
    hub_missing = [s for s in sites if s not in hub_links]
    if hub_missing:
        issues.append(f"[HUB] В каталоге отсутствуют ссылки на: {hub_missing}")
else:
    issues.append("[HUB] dist/index.html не найден!")

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=== РЕЗУЛЬТАТ АУДИТА ===")
for r in report:
    print(f"\n[{r['slug']}] {r['name']}")
    for k, v in r["checks"].items():
        print(f"  - {k}: {v}")

print("\n=== НАЙДЕННЫЕ ПРОБЛЕМЫ ===")
if issues:
    for i in issues:
        print("[FAIL]", i)
else:
    print("[SUCCESS] ВСЕ 5 САЙТОВ И ХАБ ПРОШЛИ СТРОГУЮ ПРОВЕРКУ БЕЗ ЕДИНОЙ ОШИБКИ!")
