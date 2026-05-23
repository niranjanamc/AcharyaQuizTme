import json
import random
import os

def create_q(q_id, diff, en_q, en_ans, en_opts, kn_q, kn_ans, kn_opts):
    en_opts = list(dict.fromkeys(en_opts))
    kn_opts = list(dict.fromkeys(kn_opts))
    while len(en_opts) < 4:
        en_opts.append("None")
        kn_opts.append("ಯಾವುದೂ ಅಲ್ಲ")
    
    combined = list(zip(en_opts, kn_opts))
    random.shuffle(combined)
    en_opts, kn_opts = zip(*combined)

    return {
        "id": q_id,
        "difficulty": diff,
        "en": {
            "question": en_q,
            "options": list(en_opts),
            "answer": en_ans,
            "reasoning": f"The correct answer is {en_ans}."
        },
        "kn": {
            "question": kn_q,
            "options": list(kn_opts),
            "answer": kn_ans,
            "reasoning": f"ಸರಿಯಾದ ಉತ್ತರ {kn_ans}."
        }
    }

def gen_science():
    elements = [
        ("Hydrogen", "H"), ("Helium", "He"), ("Lithium", "Li"), ("Beryllium", "Be"),
        ("Boron", "B"), ("Carbon", "C"), ("Nitrogen", "N"), ("Oxygen", "O"),
        ("Fluorine", "F"), ("Neon", "Ne"), ("Sodium", "Na"), ("Magnesium", "Mg"),
        ("Aluminum", "Al"), ("Silicon", "Si"), ("Phosphorus", "P"), ("Sulfur", "S"),
        ("Chlorine", "Cl"), ("Argon", "Ar"), ("Potassium", "K"), ("Calcium", "Ca"),
        ("Iron", "Fe"), ("Copper", "Cu"), ("Zinc", "Zn"), ("Gold", "Au"), ("Silver", "Ag")
    ]
    planets = [
        ("Mercury", "ಬುಧ"), ("Venus", "ಶುಕ್ರ"), ("Earth", "ಭೂಮಿ"), ("Mars", "ಮಂಗಳ"),
        ("Jupiter", "ಗುರು"), ("Saturn", "ಶನಿ"), ("Uranus", "ಯುರೇನಸ್"), ("Neptune", "ನೆಪ್ಚೂನ್")
    ]
    
    questions = []
    # 50 Element questions
    for i in range(50):
        el, sym = elements[i % len(elements)]
        opts_sym = [sym, sym+"x", sym[0], sym[::-1]]
        questions.append(create_q(
            f"sci_{len(questions)+1}", 1,
            f"What is the chemical symbol for {el}?", sym, opts_sym,
            f"{el} ನ ರಾಸಾಯನಿಕ ಚಿಹ್ನೆ ಯಾವುದು?", sym, opts_sym
        ))
        
    # 50 Planet/Physics questions
    for i in range(50):
        pl, kn_pl = planets[i % len(planets)]
        fake_pls = [p for p in planets if p[0] != pl]
        opts_en = [pl, fake_pls[0][0], fake_pls[1][0], fake_pls[2][0]]
        opts_kn = [kn_pl, fake_pls[0][1], fake_pls[1][1], fake_pls[2][1]]
        
        questions.append(create_q(
            f"sci_{len(questions)+1}", 2,
            f"Which of these is the planet {pl}?", pl, opts_en,
            f"ಇವುಗಳಲ್ಲಿ {kn_pl} ಗ್ರಹ ಯಾವುದು?", kn_pl, opts_kn
        ))
    return questions

def gen_history():
    years = list(range(1800, 1900))
    questions = []
    
    # Generate 100 historical timeline questions
    for i in range(100):
        year = years[i]
        diff = 1 if i < 33 else (2 if i < 66 else 3)
        opts = [str(year), str(year+10), str(year-5), str(year+20)]
        questions.append(create_q(
            f"his_{i+1}", diff,
            f"Which historical event occurred in {year}?", str(year), opts,
            f"{year} ರಲ್ಲಿ ಯಾವ ಐತಿಹಾಸಿಕ ಘಟನೆ ನಡೆಯಿತು?", str(year), opts
        ))
    return questions

def main():
    with open("science.json", "w") as f: json.dump(gen_science(), f, indent=2, ensure_ascii=False)
    with open("history.json", "w") as f: json.dump(gen_history(), f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
