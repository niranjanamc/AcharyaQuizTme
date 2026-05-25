import json

with open("src/data/questions/class_7/maths/rational_numbers.json", "r") as f:
    d_rat = json.load(f)

q1 = {
    "id": "c7_math_rat_030",
    "difficulty": 3,
    "type": "single",
    "en": {
        "question": "Which of these rational numbers is the greatest? -3/4, -5/6, -2/3",
        "options": ["-2/3", "-3/4", "-5/6", "All are equal"],
        "answer": "-2/3",
        "reasoning": "Converting to common denominator 12: -9/12, -10/12, -8/12. -8/12 (-2/3) is the greatest."
    },
    "kn": {
        "question": "ಈ ಭಾಗಲಬ್ಧ ಸಂಖ್ಯೆಗಳಲ್ಲಿ ಯಾವುದು ದೊಡ್ಡದು? -3/4, -5/6, -2/3",
        "options": ["-2/3", "-3/4", "-5/6", "ಎಲ್ಲವೂ ಸಮಾನವಾಗಿವೆ"],
        "answer": "-2/3",
        "reasoning": "ಸಾಮಾನ್ಯ ಛೇದ 12 ಕ್ಕೆ ಪರಿವರ್ತಿಸಿದಾಗ: -9/12, -10/12, -8/12. -8/12 (-2/3) ದೊಡ್ಡದು."
    }
}
d_rat.append(q1)

with open("src/data/questions/class_7/maths/rational_numbers.json", "w") as f:
    json.dump(d_rat, f, indent=4, ensure_ascii=False)


with open("src/data/questions/class_7/maths/practical_geometry.json", "r") as f:
    d_geom = json.load(f)

q2 = {
    "id": "c7_math_geom_030",
    "difficulty": 3,
    "type": "single",
    "en": {
        "question": "In a right-angled triangle, if the hypotenuse is 13 cm and one leg is 5 cm, what is the length of the other leg?",
        "options": ["12 cm", "8 cm", "10 cm", "144 cm"],
        "answer": "12 cm",
        "reasoning": "By Pythagoras theorem, leg² = 13² - 5² = 169 - 25 = 144. So, leg = 12 cm."
    },
    "kn": {
        "question": "ಒಂದು ಲಂಬಕೋನ ತ್ರಿಕೋನದಲ್ಲಿ, ವಿಕರ್ಣವು 13 ಸೆಂ.ಮೀ ಮತ್ತು ಒಂದು ಬಾಹುವು 5 ಸೆಂ.ಮೀ ಆಗಿದ್ದರೆ, ಮತ್ತೊಂದು ಬಾಹುವಿನ ಉದ್ದ ಎಷ್ಟು?",
        "options": ["12 ಸೆಂ.ಮೀ", "8 ಸೆಂ.ಮೀ", "10 ಸೆಂ.ಮೀ", "144 ಸೆಂ.ಮೀ"],
        "answer": "12 ಸೆಂ.ಮೀ",
        "reasoning": "ಪೈಥಾಗರಸ್ ಪ್ರಮೇಯದ ಪ್ರಕಾರ, ಬಾಹು² = 13² - 5² = 169 - 25 = 144. ಆದ್ದರಿಂದ, ಬಾಹು = 12 ಸೆಂ.ಮೀ."
    }
}

d_geom.append(q2)
with open("src/data/questions/class_7/maths/practical_geometry.json", "w") as f:
    json.dump(d_geom, f, indent=4, ensure_ascii=False)

