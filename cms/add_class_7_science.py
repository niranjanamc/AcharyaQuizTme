import json

catalog_path = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/catalog.json'

with open(catalog_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find class_7
class_7 = next((c for c in data['classes'] if c['id'] == 'class_7'), None)

if class_7:
    # Check if science already exists
    if not any(s['id'] == 'science' for s in class_7['subjects']):
        class_7['subjects'].append({
            "id": "science",
            "en": "Science",
            "kn": "ವಿಜ್ಞಾನ",
            "chapters": [
                {
                    "id": "nutrition_plants",
                    "file": "nutrition_plants.json",
                    "en": "Nutrition in Plants",
                    "kn": "ಸಸ್ಯಗಳಲ್ಲಿ ಪೋಷಣೆ"
                },
                {
                    "id": "nutrition_animals",
                    "file": "nutrition_animals.json",
                    "en": "Nutrition in Animals",
                    "kn": "ಪ್ರಾಣಿಗಳಲ್ಲಿ ಪೋಷಣೆ"
                },
                {
                    "id": "respiration",
                    "file": "respiration.json",
                    "en": "Respiration in Organisms",
                    "kn": "ಜೀವಿಗಳಲ್ಲಿ ಉಸಿರಾಟ"
                },
                {
                    "id": "heat",
                    "file": "heat.json",
                    "en": "Heat",
                    "kn": "ಉಷ್ಣ"
                },
                {
                    "id": "acids_bases_salts",
                    "file": "acids_bases_salts.json",
                    "en": "Acids, Bases and Salts",
                    "kn": "ಆಮ್ಲಗಳು, ಪ್ರತ್ಯಾಮ್ಲಗಳು ಮತ್ತು ಲವಣಗಳು"
                },
                {
                    "id": "physical_chemical_changes",
                    "file": "physical_chemical_changes.json",
                    "en": "Physical and Chemical Changes",
                    "kn": "ಭೌತ ಮತ್ತು ರಾಸಾಯನಿಕ ಬದಲಾವಣೆಗಳು"
                },
                {
                    "id": "transportation",
                    "file": "transportation.json",
                    "en": "Transportation in Animals and Plants",
                    "kn": "ಪ್ರಾಣಿಗಳು ಮತ್ತು ಸಸ್ಯಗಳಲ್ಲಿ ಸಾಗಾಣಿಕೆ"
                },
                {
                    "id": "reproduction_plants",
                    "file": "reproduction_plants.json",
                    "en": "Reproduction in Plants",
                    "kn": "ಸಸ್ಯಗಳಲ್ಲಿ ಸಂತಾನೋತ್ಪತ್ತಿ"
                },
                {
                    "id": "forests",
                    "file": "forests.json",
                    "en": "Forests: Our Lifeline",
                    "kn": "ಅರಣ್ಯಗಳು: ನಮ್ಮ ಜೀವನಾಡಿ"
                },
                {
                    "id": "wastewater",
                    "file": "wastewater.json",
                    "en": "Wastewater Story",
                    "kn": "ತ್ಯಾಜ್ಯ ನೀರಿನ ಕಥೆ"
                },
                {
                    "id": "motion_time",
                    "file": "motion_time.json",
                    "en": "Motion and Time",
                    "kn": "ಚಲನೆ ಮತ್ತು ಸಮಯ"
                },
                {
                    "id": "electric_current",
                    "file": "electric_current.json",
                    "en": "Electric Current and Its Effects",
                    "kn": "ವಿದ್ಯುತ್ ಪ್ರವಾಹ ಮತ್ತು ಅದರ ಪರಿಣಾಮಗಳು"
                },
                {
                    "id": "light",
                    "file": "light.json",
                    "en": "Light",
                    "kn": "ಬೆಳಕು"
                }
            ]
        })
        
        with open(catalog_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Successfully added science to class_7")
    else:
        print("Science already exists in class_7")
else:
    print("Class 7 not found in catalog")
