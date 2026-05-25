import os
import glob
from PIL import Image

brain_dir = '/Users/murthy/.gemini/antigravity/brain/9388d0b0-1b66-46f0-97ec-761803bc2921'
target_dir = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/public/images/questions/class_7/science'

os.makedirs(target_dir, exist_ok=True)

mappings = {
    'rusted_chain': 'pcc_001.webp',
    'brown_apple': 'pcc_002.webp',
    'factory_waste': 'abs_002.webp',
    'mushrooms_log': 'forests_decomposers_001.webp',
    'oil_drain': 'wastewater_oil_001.webp',
    'solar_heater': 'heat_001.webp',
    'thermal_image': 'heat_002.webp',
    'xylem_phloem': 'transportation_xylem_001.webp',
    'ant_biting': 'abs_001.webp'
}

for prefix, target_name in mappings.items():
    # Find the png file
    search_pattern = os.path.join(brain_dir, f"{prefix}_*.png")
    matches = glob.glob(search_pattern)
    if matches:
        latest = sorted(matches)[-1]  # get the most recently created
        # convert to webp
        target_path = os.path.join(target_dir, target_name)
        img = Image.open(latest)
        img.save(target_path, 'WEBP')
        print(f"Saved {target_path}")
    else:
        print(f"Warning: No source image found for {prefix}")
