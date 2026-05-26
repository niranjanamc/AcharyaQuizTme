import json

def update_catalog():
    with open('src/data/catalog.json', 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    # Find class 7
    class_7 = next((c for c in catalog['classes'] if c['id'] == 'class_7'), None)
    if not class_7:
        print("Class 7 not found!")
        return

    english = {
        "id": "english",
        "name": "English (Honeycomb & An Alien Hand)",
        "chapters": [
            {"id": "c7_eng_patrick", "name": "Who Did Patrick's Homework?"},
            {"id": "c7_eng_master", "name": "How the Dog Found Himself a New Master!"},
            {"id": "c7_eng_taro", "name": "Taro's Reward"},
            {"id": "c7_eng_kalpana", "name": "Kalpana Chawla"},
            {"id": "c7_eng_school", "name": "A Different Kind of School"},
            {"id": "c7_eng_who", "name": "Who I Am"},
            {"id": "c7_eng_fair", "name": "Fair Play"},
            {"id": "c7_eng_game", "name": "A Game of Chance"},
            {"id": "c7_eng_desert", "name": "Desert Animals"},
            {"id": "c7_eng_banyan", "name": "The Banyan Tree"},
            {"id": "c7_eng_teacher", "name": "The Tiny Teacher"},
            {"id": "c7_eng_alien", "name": "An Alien Hand"},
            {"id": "c7_eng_chappals", "name": "A Gift of Chappals"},
            {"id": "c7_eng_hilsa", "name": "Gopal and the Hilsa Fish"},
            {"id": "c7_eng_ashes", "name": "The Ashes That Made Trees Bloom"},
            {"id": "c7_eng_quality", "name": "Quality"},
            {"id": "c7_eng_detectives", "name": "Expert Detectives"}
        ]
    }

    history = {
        "id": "history",
        "name": "History (Our Pasts II)",
        "chapters": [
            {"id": "c7_his_intro", "name": "What, Where, How and When?"},
            {"id": "c7_his_hunt", "name": "From Hunting to Growing Food"},
            {"id": "c7_his_cities", "name": "In the Earliest Cities"},
            {"id": "c7_his_books", "name": "What Books and Burials Tell Us"},
            {"id": "c7_his_kings", "name": "Kingdoms and Early Republic"},
            {"id": "c7_his_tracing", "name": "Tracing Changes Through a Thousand Years"},
            {"id": "c7_his_newkings", "name": "New Kings and Kingdoms"},
            {"id": "c7_his_sultans", "name": "The Delhi Sultans"},
            {"id": "c7_his_mughals", "name": "The Mughal Empire"},
            {"id": "c7_his_rulers", "name": "Rulers and Buildings"},
            {"id": "c7_his_towns", "name": "Towns, Traders and Craftspersons"},
            {"id": "c7_his_tribes", "name": "Tribes and Nomads"},
            {"id": "c7_his_devotional", "name": "Devotional Paths to the Divine"}
        ]
    }

    kannada = {
        "id": "kannada",
        "name": "Kannada",
        "chapters": [
            {"id": "c7_kan_taayi", "name": "ಕನ್ನಡಿಗರ ತಾಯಿ"},
            {"id": "c7_kan_ganga", "name": "ಗಂಗಾವತರಣ"},
            {"id": "c7_kan_dharma", "name": "ಧರ್ಮಬುದ್ಧಿ"},
            {"id": "c7_kan_hosavarsha", "name": "ಹೊಸವರ್ಷ"},
            {"id": "c7_kan_abbakka", "name": "ವೀರರಾಣಿ ಅಬ್ಬಕ್ಕದೇವಿ"},
            {"id": "c7_kan_sankalpa", "name": "ಸಂಕಲ್ಪ ಗೀತೆ"},
            {"id": "c7_kan_sailor", "name": "ಸಿಂಧಬಾದನ ಸಾಹಸ"},
            {"id": "c7_kan_exam", "name": "ಪರೀಕ್ಷೆ"},
            {"id": "c7_kan_freedom", "name": "ಸ್ವಾತಂತ್ರ್ಯದೊಡ್ಡಾಟ"},
            {"id": "c7_kan_puttajji", "name": "ಪುಟ್ಟಜ್ಜಿ ಪುಟ್ಟಜ್ಜಿ ಕಥೆ ಹೇಳು"}
        ]
    }

    # remove them if they exist
    class_7['subjects'] = [s for s in class_7['subjects'] if s['id'] not in ('english', 'history', 'kannada')]
    
    class_7['subjects'].extend([english, history, kannada])

    with open('src/data/catalog.json', 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)

def update_menu():
    with open('src/data/menuTranslations.json', 'r', encoding='utf-8') as f:
        menu = json.load(f)

    # Class 7 English
    menu['english'] = {"en": "English", "kn": "ಇಂಗ್ಲಿಷ್"}
    menu['c7_eng_patrick'] = {"en": "Who Did Patrick's Homework?", "kn": "ಪ್ಯಾಟ್ರಿಕ್ ನ ಮನೆಗೆಲಸ ಯಾರು ಮಾಡಿದರು?"}
    menu['c7_eng_master'] = {"en": "How the Dog Found Himself a New Master!", "kn": "ನಾಯಿ ತನ್ನ ಹೊಸ ಯಜಮಾನನನ್ನು ಹೇಗೆ ಹುಡುಕಿತು!"}
    menu['c7_eng_taro'] = {"en": "Taro's Reward", "kn": "ಟಾರೋನ ಪ್ರತಿಫಲ"}
    menu['c7_eng_kalpana'] = {"en": "Kalpana Chawla", "kn": "ಕಲ್ಪನಾ ಚಾವ್ಲಾ"}
    menu['c7_eng_school'] = {"en": "A Different Kind of School", "kn": "ಒಂದು ವಿಭಿನ್ನ ರೀತಿಯ ಶಾಲೆ"}
    menu['c7_eng_who'] = {"en": "Who I Am", "kn": "ನಾನು ಯಾರು"}
    menu['c7_eng_fair'] = {"en": "Fair Play", "kn": "ನ್ಯಾಯಸಮ್ಮತ ಆಟ"}
    menu['c7_eng_game'] = {"en": "A Game of Chance", "kn": "ಒಂದು ಅವಕಾಶದ ಆಟ"}
    menu['c7_eng_desert'] = {"en": "Desert Animals", "kn": "ಮರುಭೂಮಿಯ ಪ್ರಾಣಿಗಳು"}
    menu['c7_eng_banyan'] = {"en": "The Banyan Tree", "kn": "ಆಲದ ಮರ"}
    menu['c7_eng_teacher'] = {"en": "The Tiny Teacher", "kn": "ಪುಟ್ಟ ಶಿಕ್ಷಕ"}
    menu['c7_eng_alien'] = {"en": "An Alien Hand", "kn": "ಒಂದು ಅನ್ಯಗ್ರಹ ಜೀವಿ"}
    menu['c7_eng_chappals'] = {"en": "A Gift of Chappals", "kn": "ಚಪ್ಪಲಿಗಳ ಕೊಡುಗೆ"}
    menu['c7_eng_hilsa'] = {"en": "Gopal and the Hilsa Fish", "kn": "ಗೋಪಾಲ್ ಮತ್ತು ಹಿಲ್ಸಾ ಮೀನು"}
    menu['c7_eng_ashes'] = {"en": "The Ashes That Made Trees Bloom", "kn": "ಮರಗಳನ್ನು ಅರಳಿಸಿದ ಬೂದಿ"}
    menu['c7_eng_quality'] = {"en": "Quality", "kn": "ಗುಣಮಟ್ಟ"}
    menu['c7_eng_detectives'] = {"en": "Expert Detectives", "kn": "ಪರಿಣತ ಪತ್ತೇದಾರರು"}

    # Class 7 History
    menu['history'] = {"en": "History", "kn": "ಇತಿಹಾಸ"}
    menu['c7_his_intro'] = {"en": "What, Where, How and When?", "kn": "ಏನು, ಎಲ್ಲಿ, ಹೇಗೆ ಮತ್ತು ಯಾವಾಗ?"}
    menu['c7_his_hunt'] = {"en": "From Hunting to Growing Food", "kn": "ಬೇಟೆಯಿಂದ ಆಹಾರ ಬೆಳೆಯುವವರೆಗೆ"}
    menu['c7_his_cities'] = {"en": "In the Earliest Cities", "kn": "ಆರಂಭಿಕ ನಗರಗಳಲ್ಲಿ"}
    menu['c7_his_books'] = {"en": "What Books and Burials Tell Us", "kn": "ಪುಸ್ತಕಗಳು ಮತ್ತು ಸಮಾಧಿಗಳು ಏನು ಹೇಳುತ್ತವೆ"}
    menu['c7_his_kings'] = {"en": "Kingdoms and Early Republic", "kn": "ಸಾಮ್ರಾಜ್ಯಗಳು ಮತ್ತು ಆರಂಭಿಕ ಗಣರಾಜ್ಯ"}
    menu['c7_his_tracing'] = {"en": "Tracing Changes Through a Thousand Years", "kn": "ಸಾವಿರ ವರ್ಷಗಳ ಬದಲಾವಣೆಗಳು"}
    menu['c7_his_newkings'] = {"en": "New Kings and Kingdoms", "kn": "ಹೊಸ ರಾಜರು ಮತ್ತು ಸಾಮ್ರಾಜ್ಯಗಳು"}
    menu['c7_his_sultans'] = {"en": "The Delhi Sultans", "kn": "ದೆಹಲಿ ಸುಲ್ತಾನರು"}
    menu['c7_his_mughals'] = {"en": "The Mughal Empire", "kn": "ಮೊಘಲ್ ಸಾಮ್ರಾಜ್ಯ"}
    menu['c7_his_rulers'] = {"en": "Rulers and Buildings", "kn": "ಆಡಳಿತಗಾರರು ಮತ್ತು ಕಟ್ಟಡಗಳು"}
    menu['c7_his_towns'] = {"en": "Towns, Traders and Craftspersons", "kn": "ಪಟ್ಟಣಗಳು, ವ್ಯಾಪಾರಿಗಳು ಮತ್ತು ಕುಶಲಕರ್ಮಿಗಳು"}
    menu['c7_his_tribes'] = {"en": "Tribes and Nomads", "kn": "ಬುಡಕಟ್ಟುಗಳು ಮತ್ತು ಅಲೆಮಾರಿಗಳು"}
    menu['c7_his_devotional'] = {"en": "Devotional Paths to the Divine", "kn": "ದೈವಿಕ ಭಕ್ತಿಯ ಮಾರ್ಗಗಳು"}

    # Class 7 Kannada
    menu['kannada'] = {"en": "Kannada", "kn": "ಕನ್ನಡ"}
    menu['c7_kan_taayi'] = {"en": "ಕನ್ನಡಿಗರ ತಾಯಿ", "kn": "ಕನ್ನಡಿಗರ ತಾಯಿ"}
    menu['c7_kan_ganga'] = {"en": "ಗಂಗಾವತರಣ", "kn": "ಗಂಗಾವತರಣ"}
    menu['c7_kan_dharma'] = {"en": "ಧರ್ಮಬುದ್ಧಿ", "kn": "ಧರ್ಮಬುದ್ಧಿ"}
    menu['c7_kan_hosavarsha'] = {"en": "ಹೊಸವರ್ಷ", "kn": "ಹೊಸವರ್ಷ"}
    menu['c7_kan_abbakka'] = {"en": "ವೀರರಾಣಿ ಅಬ್ಬಕ್ಕದೇವಿ", "kn": "ವೀರರಾಣಿ ಅಬ್ಬಕ್ಕದೇವಿ"}
    menu['c7_kan_sankalpa'] = {"en": "ಸಂಕಲ್ಪ ಗೀತೆ", "kn": "ಸಂಕಲ್ಪ ಗೀತೆ"}
    menu['c7_kan_sailor'] = {"en": "ಸಿಂಧಬಾದನ ಸಾಹಸ", "kn": "ಸಿಂಧಬಾದನ ಸಾಹಸ"}
    menu['c7_kan_exam'] = {"en": "ಪರೀಕ್ಷೆ", "kn": "ಪರೀಕ್ಷೆ"}
    menu['c7_kan_freedom'] = {"en": "ಸ್ವಾತಂತ್ರ್ಯದೊಡ್ಡಾಟ", "kn": "ಸ್ವಾತಂತ್ರ್ಯದೊಡ್ಡಾಟ"}
    menu['c7_kan_puttajji'] = {"en": "ಪುಟ್ಟಜ್ಜಿ ಪುಟ್ಟಜ್ಜಿ ಕಥೆ ಹೇಳು", "kn": "ಪುಟ್ಟಜ್ಜಿ ಪುಟ್ಟಜ್ಜಿ ಕಥೆ ಹೇಳು"}

    with open('src/data/menuTranslations.json', 'w', encoding='utf-8') as f:
        json.dump(menu, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    update_catalog()
    update_menu()
    print("Added remaining subjects to catalog and translations")
