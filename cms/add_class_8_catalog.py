import json
import os

catalog_path = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/catalog.json'
menu_path = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/menuTranslations.json'

def update_catalog():
    with open(catalog_path, 'r', encoding='utf-8') as f:
        catalog = json.load(f)
    
    # Check if class_8 exists
    class_8 = next((c for c in catalog['classes'] if c['id'] == 'class_8'), None)
    if not class_8:
        class_8 = {
            "id": "class_8",
            "name": "Class 8 (NCERT)",
            "subjects": []
        }
        catalog['classes'].append(class_8)
        
    maths_subject = {
        "id": "maths",
        "name": "Mathematics",
        "chapters": [
            { "id": "rational_numbers", "name": "Rational Numbers" },
            { "id": "linear_equations", "name": "Linear Equations in One Variable" },
            { "id": "quadrilaterals", "name": "Understanding Quadrilaterals" },
            { "id": "data_handling", "name": "Data Handling" },
            { "id": "squares_roots", "name": "Squares and Square Roots" },
            { "id": "cubes_roots", "name": "Cubes and Cube Roots" },
            { "id": "comparing_quantities", "name": "Comparing Quantities" },
            { "id": "algebraic_expressions", "name": "Algebraic Expressions and Identities" },
            { "id": "mensuration", "name": "Mensuration" },
            { "id": "exponents_powers", "name": "Exponents and Powers" },
            { "id": "proportions", "name": "Direct and Inverse Proportions" },
            { "id": "factorisation", "name": "Factorisation" },
            { "id": "graphs", "name": "Introduction to Graphs" }
        ]
    }
    
    science_subject = {
        "id": "science",
        "name": "Science",
        "chapters": [
            { "id": "crop_production", "name": "Crop Production and Management" },
            { "id": "microorganisms", "name": "Microorganisms: Friend and Foe" },
            { "id": "coal_petroleum", "name": "Coal and Petroleum" },
            { "id": "combustion_flame", "name": "Combustion and Flame" },
            { "id": "conservation_plants_animals", "name": "Conservation of Plants and Animals" },
            { "id": "reproduction_animals", "name": "Reproduction in Animals" },
            { "id": "adolescence", "name": "Reaching the Age of Adolescence" },
            { "id": "force_pressure", "name": "Force and Pressure" },
            { "id": "friction", "name": "Friction" },
            { "id": "sound", "name": "Sound" },
            { "id": "electric_current", "name": "Chemical Effects of Electric Current" },
            { "id": "natural_phenomena", "name": "Some Natural Phenomena" },
            { "id": "light", "name": "Light" }
        ]
    }
    
    english_subject = {
        "id": "english",
        "name": "English (Honeydew)",
        "chapters": [
            { "id": "c8_eng_christmas", "name": "The Best Christmas Present in the World" },
            { "id": "c8_eng_tsunami", "name": "The Tsunami" },
            { "id": "c8_eng_glimpses", "name": "Glimpses of the Past" },
            { "id": "c8_eng_bepin", "name": "Bepin Choudhury's Lapse of Memory" },
            { "id": "c8_eng_summit", "name": "The Summit Within" }
        ]
    }
    
    history_subject = {
        "id": "history",
        "name": "History (Our Pasts - III)",
        "chapters": [
            { "id": "c8_his_trade", "name": "From Trade to Territory" },
            { "id": "c8_his_countryside", "name": "Ruling the Countryside" },
            { "id": "c8_his_rebel", "name": "When People Rebel" },
            { "id": "c8_his_education", "name": "Civilising the \"Native\", Educating the Nation" },
            { "id": "c8_his_national", "name": "The Making of the National Movement: 1870s-1947" }
        ]
    }
    
    kannada_subject = {
        "id": "kannada",
        "name": "Kannada",
        "chapters": [
            { "id": "c8_kan_kannadiga", "name": "ಕನ್ನಡತಿ / ಕನ್ನಡಿಗ (Kannadiga)" },
            { "id": "c8_kan_siddhartha", "name": "ಸಿದ್ಧಾರ್ಥನ ಕಾರುಣ್ಯ (Siddharthana Karunya)" },
            { "id": "c8_kan_buddha", "name": "ಬುದ್ಧನ ಸಂದೇಶ (Buddhana Sandesha)" },
            { "id": "c8_kan_sirigannada", "name": "ಸಿರಿಗನ್ನಡ (Sirigannada)" },
            { "id": "c8_kan_kranti", "name": "ಕ್ರಾಂತಿ ಕಹಳೆ (Kranti Kahale)" }
        ]
    }
    
    class_8['subjects'] = [maths_subject, science_subject, english_subject, history_subject, kannada_subject]
    
    with open(catalog_path, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
    print("Catalog updated successfully.")

def update_menu():
    with open(menu_path, 'r', encoding='utf-8') as f:
        menu = json.load(f)
        
    translations = {
        # ─────────────────────────────────────────────────────────────
        # IMPORTANT: Top-level class and subject keys MUST be added.
        # These are plain Kannada strings (not {en,kn} objects).
        # Without these keys the class/subject names will NOT switch
        # to Kannada when the user selects the Kannada language.
        # ─────────────────────────────────────────────────────────────
        "class_8":          "ತರಗತಿ 8 (NCERT)",
        "class_8/maths":    "ಗಣಿತ",
        "class_8/science":  "ವಿಜ್ಞಾನ",
        "class_8/english":  "ಇಂಗ್ಲಿಷ್ (ಹನಿಡ್ಯೂ)",
        "class_8/history":  "ಇತಿಹಾಸ (ನಮ್ಮ ಭೂತಕಾಲ - III)",
        "class_8/kannada":  "ಕನ್ನಡ",

        # Chapter-level entries use {en, kn} objects.
        # Maths
        "rational_numbers": { "en": "Rational Numbers", "kn": "ಭಾಗಲಬ್ಧ ಸಂಖ್ಯೆಗಳು" },
        "linear_equations": { "en": "Linear Equations in One Variable", "kn": "ಒಂದು ಚರಾಕ್ಷರವುಳ್ಳ ರೇಖಾತ್ಮಕ ಸಮೀಕರಣಗಳು" },
        "quadrilaterals": { "en": "Understanding Quadrilaterals", "kn": "ಚತುರ್ಭುಜಗಳ ತಿಳುವಳಿಕೆ" },
        "squares_roots": { "en": "Squares and Square Roots", "kn": "ವರ್ಗಗಳು ಮತ್ತು ವರ್ಗಮೂಲಗಳು" },
        "cubes_roots": { "en": "Cubes and Cube Roots", "kn": "ಘನಗಳು ಮತ್ತು ಘನಮೂಲಗಳು" },
        "comparing_quantities": { "en": "Comparing Quantities", "kn": "ಪರಿಮಾಣಗಳ ಹೋಲಿಕೆ" },
        "algebraic_expressions": { "en": "Algebraic Expressions and Identities", "kn": "ಬೀಜೋಕ್ತಿಗಳು ಮತ್ತು ನಿತ್ಯಸಮೀಕರಣಗಳು" },
        "mensuration": { "en": "Mensuration", "kn": "ಕ್ಷೇತ್ರಗಣಿತ" },
        "exponents_powers": { "en": "Exponents and Powers", "kn": "ಘಾತಾಂಕಗಳು ಮತ್ತು ಘಾತಗಳು" },
        "proportions": { "en": "Direct and Inverse Proportions", "kn": "ನೇರ ಮತ್ತು ವಿಲೋಮ ಅನುಪಾತಗಳು" },
        "factorisation": { "en": "Factorisation", "kn": "ಅಪವರ್ತನೀಕರಣ" },
        "graphs": { "en": "Introduction to Graphs", "kn": "ನಕ್ಷೆಗಳ ಪರಿಚಯ" },
        
        # Science
        "crop_production": { "en": "Crop Production and Management", "kn": "ಬೆಳೆ ಉತ್ಪಾದನೆ ಮತ್ತು ನಿರ್ವಹಣೆ" },
        "microorganisms": { "en": "Microorganisms: Friend and Foe", "kn": "ಸೂಕ್ಷ್ಮಜೀವಿಗಳು: ಮಿತ್ರ ಮತ್ತು ಶತ್ರು" },
        "coal_petroleum": { "en": "Coal and Petroleum", "kn": "ಕಲ್ಲಿದ್ದಲು ಮತ್ತು ಪೆಟ್ರೋಲಿಯಂ" },
        "combustion_flame": { "en": "Combustion and Flame", "kn": "ದಹನ ಮತ್ತು ಜ್ವಾಲೆ" },
        "conservation_plants_animals": { "en": "Conservation of Plants and Animals", "kn": "ಸಸ್ಯಗಳು ಮತ್ತು ಪ್ರಾಣಿಗಳ ಸಂರಕ್ಷಣೆ" },
        "reproduction_animals": { "en": "Reproduction in Animals", "kn": "ಪ್ರಾಣಿಗಳಲ್ಲಿ ಸಂತಾನೋತ್ಪತ್ತಿ" },
        "adolescence": { "en": "Reaching the Age of Adolescence", "kn": "ಹದಿಹರೆಯಕ್ಕೆ ತಲುಪುವುದು" },
        "force_pressure": { "en": "Force and Pressure", "kn": "ಬಲ ಮತ್ತು ಒತ್ತಡ" },
        "friction": { "en": "Friction", "kn": "ಘರ್ಷಣೆ" },
        "sound": { "en": "Sound", "kn": "ಶಬ್ದ" },
        "electric_current": { "en": "Chemical Effects of Electric Current", "kn": "ವಿದ್ಯುತ್ ಪ್ರವಾಹದ ರಾಸಾಯನಿಕ ಪರಿಣಾಮಗಳು" },
        "natural_phenomena": { "en": "Some Natural Phenomena", "kn": "ಕೆಲವು ನೈಸರ್ಗಿಕ ವಿದ್ಯಮಾನಗಳು" },
        "light": { "en": "Light", "kn": "ಬೆಳಕು" },
        
        # English
        "c8_eng_christmas": { "en": "The Best Christmas Present in the World", "kn": "ವಿಶ್ವದ ಅತ್ಯುತ್ತಮ ಕ್ರಿಸ್ಮಸ್ ಕೊಡುಗೆ" },
        "c8_eng_tsunami": { "en": "The Tsunami", "kn": "ಸುನಾಮಿ" },
        "c8_eng_glimpses": { "en": "Glimpses of the Past", "kn": "ಭೂತಕಾಲದ ನೋಟಗಳು" },
        "c8_eng_bepin": { "en": "Bepin Choudhury's Lapse of Memory", "kn": "ಬೆಪಿನ್ ಚೌಧುರಿಯವರ ಸ್ಮರಣಶಕ್ತಿ ಲೋಪ" },
        "c8_eng_summit": { "en": "The Summit Within", "kn": "ಅಂತರಂಗದ ಶಿಖರ" },
        
        # History
        "c8_his_trade": { "en": "From Trade to Territory", "kn": "ವ್ಯಾಪಾರದಿಂದ ಸಾಮ್ರಾಜ್ಯದವರೆಗೆ" },
        "c8_his_countryside": { "en": "Ruling the Countryside", "kn": "ಗ್ರಾಮೀಣ ಪ್ರದೇಶಗಳ ಆಡಳಿತ" },
        "c8_his_rebel": { "en": "When People Rebel", "kn": "ಜನರು ದಂಗೆ ಎದ್ದಾಗ" },
        "c8_his_education": { "en": "Civilising the \"Native\", Educating the Nation", "kn": "ಸ್ವದೇಶಿಗಳನ್ನು ಸುಸಂಸ್ಕೃತರನ್ನಾಗಿಸುವುದು, ರಾಷ್ಟ್ರಕ್ಕೆ ಶಿಕ್ಷಣ ನೀಡುವುದು" },
        "c8_his_national": { "en": "The Making of the National Movement: 1870s-1947", "kn": "ರಾಷ್ಟ್ರೀಯ ಚಳುವಳಿಯ ಸಂಘಟನೆ: ೧೮೭೦ರ ದಶಕದಿಂದ ೧೯೪೭ರವರೆಗೆ" },
        
        # Kannada
        "c8_kan_kannadiga": { "en": "ಕನ್ನಡತಿ / ಕನ್ನಡಿಗ (Kannadiga)", "kn": "ಕನ್ನಡತಿ / ಕನ್ನಡಿಗ" },
        "c8_kan_siddhartha": { "en": "ಸಿದ್ಧಾರ್ಥನ ಕಾರುಣ್ಯ (Siddharthana Karunya)", "kn": "ಸಿದ್ಧಾರ್ಥನ ಕಾರುಣ್ಯ" },
        "c8_kan_buddha": { "en": "ಬುದ್ಧನ ಸಂದೇಶ (Buddhana Sandesha)", "kn": "ಬುದ್ಧನ ಸಂದೇಶ" },
        "c8_kan_sirigannada": { "en": "ಸಿರಿಗನ್ನಡ (Sirigannada)", "kn": "ಸಿರಿಗನ್ನಡ" },
        "c8_kan_kranti": { "en": "ಕ್ರಾಂತಿ ಕಹಳೆ (Kranti Kahale)", "kn": "ಕ್ರಾಂತಿ ಕಹಳೆ" }
    }
    
    for key, val in translations.items():
        menu[key] = val
        
    with open(menu_path, 'w', encoding='utf-8') as f:
        json.dump(menu, f, indent=2, ensure_ascii=False)
    print("Menu translations updated successfully.")

if __name__ == "__main__":
    update_catalog()
    update_menu()
