# -*- coding: utf-8 -*-
import urllib.request
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

orgs = [
    ('avtoray', 'https://yandex.ru/maps/org/avtoray/127217533580/reviews/'),
    ('zvezda', 'https://yandex.ru/maps/org/zvezda/123827273070/reviews/'),
    ('careta', 'https://yandex.ru/maps/org/avtoservis_careta/46985389595/reviews/'),
    ('avtolux', 'https://yandex.ru/maps/org/avtolyuks/161339787019/reviews/'),
    ('uspeh-777', 'https://yandex.ru/maps/org/uspekh_777/1111994914/reviews/')
]

for name, url in orgs:
    print(f"\n==================== {name} REVIEWS ====================")
    req = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        reviews = re.findall(r'<span class="[^"]*spoiler-view__text-container[^"]*">(.*?)</span>', html, re.DOTALL)
        # Ratings
        print(f"Total reviews extracted: {len(reviews)}")
        for i, r in enumerate(reviews[:4]):
            clean = re.sub(r'<[^>]+>', '', r).strip()
            print(f"--- Review {i+1} ---")
            print(clean)
    except Exception as e:
        print("Error:", e)
