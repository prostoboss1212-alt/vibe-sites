# -*- coding: utf-8 -*-
import glob
import re

folders = ['dist', 'docs']
sites = [
    ('uspeh-777', '1111994914'),
    ('zvezda', '123827273070'),
    ('careta', '46985389595'),
    ('avtoray', '127217533580'),
    ('avtolux', '161339787019')
]

issues = []
for folder in folders:
    for slug, oid in sites:
        path = f'{folder}/{slug}/index.html'
        c = open(path, encoding='utf-8').read()
        
        if 'сеть из 2 филиалов' in c.lower() or '2 филиал' in c.lower():
            issues.append(f'{path}: содержит упоминание 2 филиалов')
            
        if f'oid={oid}' not in c:
            issues.append(f'{path}: отсутствует точный oid={oid} в виджете карты')
            
        if slug != 'uspeh-777' and ('343 оценки' in c or '377 оценок' in c):
            issues.append(f'{path}: утечка чужих счетчиков отзывов 343/377')
            
        if 'reviews/' in c and '?text=' in c:
            issues.append(f'{path}: битая ссылка reviews/ в параметре text')
            
        if 'undefined' in c or 'null' in c:
            issues.append(f'{path}: содержит плейсхолдеры')

if not issues:
    print('AUDIT PASSED: All 5 sites in dist/ and docs/ are 100% verified and clean!')
else:
    print('AUDIT FAILED:', issues)
