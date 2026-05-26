import json
import os

catalog_path = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/catalog.json'
menu_path = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/menuTranslations.json'

with open(catalog_path, 'r', encoding='utf-8') as f:
    catalog = json.load(f)

with open(menu_path, 'r', encoding='utf-8') as f:
    menu = json.load(f)

for cls in catalog.get('classes', []):
    if cls.get('id') == 'class_7':
        for sub in cls.get('subjects', []):
            if sub.get('id') == 'science':
                # Fix subject
                if 'en' in sub:
                    sub['name'] = sub['en']
                    del sub['en']
                if 'kn' in sub:
                    menu['class_7/science'] = sub['kn']
                    del sub['kn']
                
                # Fix chapters
                for ch in sub.get('chapters', []):
                    if 'en' in ch:
                        ch['name'] = ch['en']
                        del ch['en']
                    if 'kn' in ch:
                        menu[ch['id']] = ch['kn']
                        del ch['kn']

with open(catalog_path, 'w', encoding='utf-8') as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)

with open(menu_path, 'w', encoding='utf-8') as f:
    json.dump(menu, f, indent=2, ensure_ascii=False)

print("Fixed catalog and menu translations!")
