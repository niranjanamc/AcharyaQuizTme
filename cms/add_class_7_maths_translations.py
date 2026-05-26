import json

menu_path = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/menuTranslations.json'

with open(menu_path, 'r', encoding='utf-8') as f:
    menu = json.load(f)

new_translations = {
    "class_7": "ತರಗತಿ 7 (NCERT)",
    "class_7/maths": "ಗಣಿತ",
    "integers": "ಪೂರ್ಣಾಂಕಗಳು",
    "fractions_decimals": "ಭಿನ್ನರಾಶಿಗಳು ಮತ್ತು ದಶಮಾಂಶಗಳು",
    "data_handling": "ದತ್ತಾಂಶ ನಿರ್ವಹಣೆ",
    "simple_equations": "ಸರಳ ಸಮೀಕರಣಗಳು",
    "lines_angles": "ರೇಖೆಗಳು ಮತ್ತು ಕೋನಗಳು",
    "triangles": "ತ್ರಿಭುಜ ಮತ್ತು ಅದರ ಗುಣಲಕ್ಷಣಗಳು",
    "congruence": "ತ್ರಿಭುಜಗಳ ಸರ್ವಸಮತೆ",
    "comparing_quantities": "ಪರಿಮಾಣಗಳ ಹೋಲಿಕೆ",
    "rational_numbers": "ಭಾಗಲಬ್ಧ ಸಂಖ್ಯೆಗಳು",
    "practical_geometry": "ಪ್ರಾಯೋಗಿಕ ರೇಖಾಗಣಿತ",
    "perimeter_area": "ಸುತ್ತಳತೆ ಮತ್ತು ವಿಸ್ತೀರ್ಣ",
    "algebraic_expressions": "ಬೀಜಗಣಿತದ ಅಭಿವ್ಯಕ್ತಿಗಳು",
    "exponents_powers": "ಘಾತಾಂಕಗಳು ಮತ್ತು ಘಾತಗಳು",
    "symmetry": "ಸಮಮಿತಿ",
    "solid_shapes": "ಘನಾಕೃತಿಗಳ ದೃಶ್ಯೀಕರಣ"
}

menu.update(new_translations)

with open(menu_path, 'w', encoding='utf-8') as f:
    json.dump(menu, f, indent=2, ensure_ascii=False)

print("Added Class 7 Maths Kannada translations!")
