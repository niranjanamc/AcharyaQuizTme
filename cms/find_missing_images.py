import os
import json

base_dir = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/science'
public_dir = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/public/images/questions'

missing_images = []

for filename in os.listdir(base_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(base_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for q in data:
                    if 'image' in q and q['image'].get('type') == 'raster' and 'src' in q['image']:
                        src = q['image']['src']
                        full_path = os.path.join(public_dir, src)
                        if not os.path.exists(full_path):
                            alt_en = q['image'].get('alt', {}).get('en', 'Science image')
                            missing_images.append({'file': full_path, 'alt': alt_en})
        except Exception as e:
            print(f"Error reading {filename}: {e}")

for img in missing_images:
    print(f"{img['file']} | {img['alt']}")
