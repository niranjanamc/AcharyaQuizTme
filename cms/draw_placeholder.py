from PIL import Image, ImageDraw, ImageFont
import os

target_dir = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/public/images/questions/class_7/science'
os.makedirs(target_dir, exist_ok=True)
target_path = os.path.join(target_dir, 'transportation_xylem_001.webp')

img = Image.new('RGB', (600, 400), color = (73, 109, 137))
d = ImageDraw.Draw(img)
d.text((50,180), "Xylem and Phloem Microscope View", fill=(255,255,0))
img.save(target_path, 'WEBP')
print(f"Saved placeholder {target_path}")
