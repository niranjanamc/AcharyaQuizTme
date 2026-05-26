import json

catalog_path = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/catalog.json'
menu_path = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/menuTranslations.json'

with open(catalog_path, 'r', encoding='utf-8') as f:
    catalog = json.load(f)

with open(menu_path, 'r', encoding='utf-8') as f:
    menu = json.load(f)

# Subjects to add
new_subjects = [
    {
        "id": "english",
        "name": "English (Honeycomb)",
        "chapters": [
            {"id": "c7_eng_questions", "name": "Three Questions & The Squirrel"},
            {"id": "c7_eng_chappals", "name": "A Gift of Chappals & The Rebel"},
            {"id": "c7_eng_hilsa", "name": "Gopal and the Hilsa Fish & The Shed"},
            {"id": "c7_eng_ashes", "name": "The Ashes That Made Trees Bloom & Chivvy"},
            {"id": "c7_eng_quality", "name": "Quality & Trees"}
        ]
    },
    {
        "id": "history",
        "name": "History (Our Pasts - II)",
        "chapters": [
            {"id": "c7_his_tracing", "name": "Tracing Changes Through a Thousand Years"},
            {"id": "c7_his_kings", "name": "New Kings and Kingdoms"},
            {"id": "c7_his_sultans", "name": "The Delhi Sultans"},
            {"id": "c7_his_mughals", "name": "The Mughal Empire"},
            {"id": "c7_his_rulers", "name": "Rulers and Buildings"}
        ]
    },
    {
        "id": "kannada",
        "name": "Kannada (Siri Kannada 7)",
        "chapters": [
            {"id": "c7_kan_puttajji", "name": "ಪುಟ್ಟಜ್ಜಿ ಪುಟ್ಟಜ್ಜಿ ಕಥೆ ಹೇಳು (Puttajji Puttajji Kathe Helu)"},
            {"id": "c7_kan_freedom", "name": "ಬಿಡುಗಡೆಯ ಹಾಡು (Song of Freedom)"},
            {"id": "c7_kan_exam", "name": "ಪರೀಕ್ಷೆ (Examination)"},
            {"id": "c7_kan_architects", "name": "ಭಾಗ್ಯಶಿಲ್ಪಿಗಳು (Architects of Destiny)"},
            {"id": "c7_kan_sailor", "name": "ಸತ್ಯವಂತ ನಾವಿಕ (The Truthful Sailor)"}
        ]
    }
]

# Add subjects to class 7
for cls in catalog.get('classes', []):
    if cls.get('id') == 'class_7':
        # Remove old ones if they exist (for idempotency)
        cls['subjects'] = [s for s in cls.get('subjects', []) if s['id'] not in ['english', 'history', 'kannada']]
        cls['subjects'].extend(new_subjects)

# Translations to add
new_translations = {
    "class_7/english": "ಇಂಗ್ಲಿಷ್",
    "class_7/history": "ಇತಿಹಾಸ (ನಮ್ಮ ಭೂತಕಾಲ - II)",
    "class_7/kannada": "ಕನ್ನಡ",
    "c7_eng_questions": "ಮೂರು ಪ್ರಶ್ನೆಗಳು",
    "c7_eng_chappals": "ಚಪ್ಪಲಿಗಳ ಉಡುಗೊರೆ",
    "c7_eng_hilsa": "ಗೋಪಾಲ್ ಮತ್ತು ಹಿಲ್ಸಾ ಮೀನು",
    "c7_eng_ashes": "ಮರಗಳನ್ನು ಅರಳಿಸಿದ ಬೂದಿ",
    "c7_eng_quality": "ಗುಣಮಟ್ಟ",
    "c7_his_tracing": "ಸಾವಿರ ವರ್ಷಗಳ ಬದಲಾವಣೆಗಳು",
    "c7_his_kings": "ಹೊಸ ರಾಜರು ಮತ್ತು ರಾಜ್ಯಗಳು",
    "c7_his_sultans": "ದೆಹಲಿ ಸುಲ್ತಾನರು",
    "c7_his_mughals": "ಮೊಘಲ್ ಸಾಮ್ರಾಜ್ಯ",
    "c7_his_rulers": "ಆಡಳಿತಗಾರರು ಮತ್ತು ಕಟ್ಟಡಗಳು",
    "c7_kan_puttajji": "ಪುಟ್ಟಜ್ಜಿ ಪುಟ್ಟಜ್ಜಿ ಕಥೆ ಹೇಳು",
    "c7_kan_freedom": "ಬಿಡುಗಡೆಯ ಹಾಡು",
    "c7_kan_exam": "ಪರೀಕ್ಷೆ",
    "c7_kan_architects": "ಭಾಗ್ಯಶಿಲ್ಪಿಗಳು",
    "c7_kan_sailor": "ಸತ್ಯವಂತ ನಾವಿಕ"
}

menu.update(new_translations)

with open(catalog_path, 'w', encoding='utf-8') as f:
    json.dump(catalog, f, indent=2, ensure_ascii=False)

with open(menu_path, 'w', encoding='utf-8') as f:
    json.dump(menu, f, indent=2, ensure_ascii=False)

print("Added Class 7 remaining subjects to catalog and translations!")
