import json

def update_catalog():
    with open('src/data/catalog.json', 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    # Find class 6
    class_6 = next((c for c in catalog['classes'] if c['id'] == 'class_6'), None)
    if not class_6:
        print("Class 6 not found!")
        return

    english = {
        "id": "english",
        "name": "English (Honeysuckle)",
        "chapters": [
            {"id": "c6_eng_patrick", "name": "Who Did Patrick's Homework?"},
            {"id": "c6_eng_master", "name": "How the Dog Found Himself a New Master!"},
            {"id": "c6_eng_taro", "name": "Taro's Reward"},
            {"id": "c6_eng_kalpana", "name": "Kalpana Chawla"},
            {"id": "c6_eng_school", "name": "A Different Kind of School"}
        ]
    }

    history = {
        "id": "history",
        "name": "History (Our Pasts I)",
        "chapters": [
            {"id": "c6_his_intro", "name": "What, Where, How and When?"},
            {"id": "c6_hunting_gathering", "name": "From Hunting to Growing Food"},
            {"id": "c6_earliest_cities", "name": "In the Earliest Cities"},
            {"id": "c6_books_burials", "name": "What Books and Burials Tell Us"},
            {"id": "c6_kingdoms", "name": "Kingdoms and Early Republic"}
        ]
    }

    kannada = {
        "id": "kannada",
        "name": "Kannada",
        "chapters": [
            {"id": "c6_kan_taayi", "name": "ಕನ್ನಡಿಗರ ತಾಯಿ"},
            {"id": "c6_kan_ganga", "name": "ಗಂಗಾವತರಣ"},
            {"id": "c6_kan_dharma", "name": "ಧರ್ಮಬುದ್ಧಿ"},
            {"id": "c6_kan_hosavarsha", "name": "ಹೊಸವರ್ಷ"},
            {"id": "c6_kan_abbakka", "name": "ವೀರರಾಣಿ ಅಬ್ಬಕ್ಕದೇವಿ"}
        ]
    }

    # remove them if they exist
    class_6['subjects'] = [s for s in class_6['subjects'] if s['id'] not in ('english', 'history', 'kannada')]
    
    class_6['subjects'].extend([english, history, kannada])

    with open('src/data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)

def update_menu():
    with open('src/data/menuTranslations.json', 'r', encoding='utf-8') as f:
        menu = json.load(f)

    # Class 6 English
    menu['c6_eng_patrick'] = {"en": "Who Did Patrick's Homework?", "kn": "ಪ್ಯಾಟ್ರಿಕ್ ನ ಮನೆಗೆಲಸ ಯಾರು ಮಾಡಿದರು?"}
    menu['c6_eng_master'] = {"en": "How the Dog Found Himself a New Master!", "kn": "ನಾಯಿ ತನ್ನ ಹೊಸ ಯಜಮಾನನನ್ನು ಹೇಗೆ ಹುಡುಕಿತು!"}
    menu['c6_eng_taro'] = {"en": "Taro's Reward", "kn": "ಟಾರೋನ ಪ್ರತಿಫಲ"}
    menu['c6_eng_kalpana'] = {"en": "Kalpana Chawla", "kn": "ಕಲ್ಪನಾ ಚಾವ್ಲಾ"}
    menu['c6_eng_school'] = {"en": "A Different Kind of School", "kn": "ಒಂದು ವಿಭಿನ್ನ ರೀತಿಯ ಶಾಲೆ"}

    # Class 6 History
    menu['c6_hunting_gathering'] = {"en": "From Hunting to Growing Food", "kn": "ಬೇಟೆಯಿಂದ ಆಹಾರ ಬೆಳೆಯುವವರೆಗೆ"}
    menu['c6_earliest_cities'] = {"en": "In the Earliest Cities", "kn": "ಆರಂಭಿಕ ನಗರಗಳಲ್ಲಿ"}
    menu['c6_books_burials'] = {"en": "What Books and Burials Tell Us", "kn": "ಪುಸ್ತಕಗಳು ಮತ್ತು ಸಮಾಧಿಗಳು ಏನು ಹೇಳುತ್ತವೆ"}
    menu['c6_kingdoms'] = {"en": "Kingdoms and Early Republic", "kn": "ಸಾಮ್ರಾಜ್ಯಗಳು ಮತ್ತು ಆರಂಭಿಕ ಗಣರಾಜ್ಯ"}

    # Class 6 Kannada
    menu['c6_kan_taayi'] = {"en": "ಕನ್ನಡಿಗರ ತಾಯಿ", "kn": "ಕನ್ನಡಿಗರ ತಾಯಿ"}
    menu['c6_kan_ganga'] = {"en": "ಗಂಗಾವತರಣ", "kn": "ಗಂಗಾವತರಣ"}
    menu['c6_kan_dharma'] = {"en": "ಧರ್ಮಬುದ್ಧಿ", "kn": "ಧರ್ಮಬುದ್ಧಿ"}
    menu['c6_kan_hosavarsha'] = {"en": "ಹೊಸವರ್ಷ", "kn": "ಹೊಸವರ್ಷ"}
    menu['c6_kan_abbakka'] = {"en": "ವೀರರಾಣಿ ಅಬ್ಬಕ್ಕದೇವಿ", "kn": "ವೀರರಾಣಿ ಅಬ್ಬಕ್ಕದೇವಿ"}

    with open('src/data/menuTranslations.json', 'w', encoding='utf-8') as f:
        json.dump(menu, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    update_catalog()
    update_menu()
    print("Added remaining subjects to Class 6 catalog and translations")
