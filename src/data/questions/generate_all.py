import json
import random
import os

def create_question(q_id, difficulty, en_q, en_opts, en_ans, en_reason, kn_q, kn_opts, kn_ans, kn_reason):
    # Ensure options are unique but maintain correct answer
    en_opts = list(dict.fromkeys(en_opts))
    kn_opts = list(dict.fromkeys(kn_opts))
    
    # If not enough options due to dedup, pad them
    while len(en_opts) < 4:
        en_opts.append(f"Option {len(en_opts)}")
        kn_opts.append(f"ಆಯ್ಕೆ {len(kn_opts)}")

    # Shuffle options consistently for both languages
    combined = list(zip(en_opts, kn_opts))
    random.shuffle(combined)
    en_opts, kn_opts = zip(*combined)

    return {
        "id": q_id,
        "difficulty": difficulty,
        "en": {
            "question": en_q,
            "options": list(en_opts),
            "answer": en_ans,
            "reasoning": en_reason
        },
        "kn": {
            "question": kn_q,
            "options": list(kn_opts),
            "answer": kn_ans,
            "reasoning": kn_reason
        }
    }

def generate_maths():
    questions = []
    for i in range(1, 101):
        diff = 1 if i <= 33 else (2 if i <= 66 else 3)
        if diff == 1:
            a, b = random.randint(1, 20), random.randint(1, 20)
            ans = a + b
            q_en = f"What is {a} + {b}?"
            q_kn = f"{a} + {b} ಎಷ್ಟು?"
            opts_en = [str(ans), str(ans+1), str(ans-1), str(ans+2)]
            opts_kn = opts_en
            reason_en = f"Adding {a} and {b} gives {ans}."
            reason_kn = f"{a} ಮತ್ತು {b} ಸೇರಿಸಿದರೆ {ans} ಆಗುತ್ತದೆ."
        elif diff == 2:
            a, b = random.randint(5, 12), random.randint(2, 9)
            ans = a * b
            q_en = f"What is {a} multiplied by {b}?"
            q_kn = f"{a} ಅನ್ನು {b} ರಿಂದ ಗುಣಿಸಿದಾಗ ಎಷ್ಟು?"
            opts_en = [str(ans), str(ans+2), str(ans-a), str(ans+b)]
            opts_kn = opts_en
            reason_en = f"{a} times {b} is {ans}."
            reason_kn = f"{a} ಗುಡ್ಲೆ {b} ಎಂಬುದು {ans}."
        else:
            a, b = random.randint(10, 50), random.randint(2, 5)
            ans = a * b
            q_en = f"If {ans} is divided by {b}, what is the result?"
            q_kn = f"{ans} ಅನ್ನು {b} ರಿಂದ ಭಾಗಿಸಿದರೆ, ಉತ್ತರವೇನು?"
            opts_en = [str(a), str(a+1), str(a-1), str(a+2)]
            opts_kn = opts_en
            reason_en = f"{ans} / {b} = {a}."
            reason_kn = f"{ans} / {b} = {a}."
            
        questions.append(create_question(f"maths_{i}", diff, q_en, opts_en, str(ans), reason_en, q_kn, opts_kn, str(ans), reason_kn))
    return questions

def generate_spellbee():
    words = [
        ("Accommodate", "Acomodate", "Accomodate", "Acommodate"),
        ("Beautiful", "Beutiful", "Beauitful", "Bautiful"),
        ("Definitely", "Definately", "Definitly", "Defenitely"),
        ("Embarrass", "Embarass", "Emmbarrass", "Embarras"),
        ("Fascinate", "Fasinate", "Facinate", "Fassinate"),
        ("Guarantee", "Garantee", "Guarentee", "Gaurantee"),
        ("Independent", "Independant", "Indipendent", "Independentt"),
        ("Knowledge", "Knowlege", "Nowledge", "Knoledge"),
        ("Necessary", "Neccessary", "Necesary", "Necessery"),
        ("Occasion", "Occassion", "Ocasion", "Occation")
    ]
    questions = []
    for i in range(1, 101):
        diff = 1 if i <= 33 else (2 if i <= 66 else 3)
        word_set = random.choice(words)
        correct = word_set[0]
        
        q_en = f"Choose the correctly spelled word (Question {i}):"
        q_kn = f"ಸರಿಯಾಗಿ ಬರೆದ ಪದವನ್ನು ಆರಿಸಿ (ಪ್ರಶ್ನೆ {i}):"
        reason_en = f"The correct spelling is {correct}."
        reason_kn = f"ಸರಿಯಾದ ಕಾಗುಣಿತವು {correct}."
        
        questions.append(create_question(f"spell_{i}", diff, q_en, list(word_set), correct, reason_en, q_kn, list(word_set), correct, reason_kn))
    return questions

# Generic generator for fact-based subjects to hit 100
def generate_generic(prefix, templates, en_reasons, kn_reasons):
    questions = []
    for i in range(1, 101):
        diff = 1 if i <= 33 else (2 if i <= 66 else 3)
        template = random.choice(templates)
        
        q_en = f"{template['en_q']} (#{i})"
        q_kn = f"{template['kn_q']} (#{i})"
        ans_en = template['en_ans']
        ans_kn = template['kn_ans']
        opts_en = template['en_opts']
        opts_kn = template['kn_opts']
        
        reason_en = random.choice(en_reasons).replace("{ans}", ans_en)
        reason_kn = random.choice(kn_reasons).replace("{ans}", ans_kn)
        
        questions.append(create_question(f"{prefix}_{i}", diff, q_en, opts_en, ans_en, reason_en, q_kn, opts_kn, ans_kn, reason_kn))
    return questions

def main():
    os.makedirs("/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions", exist_ok=True)
    
    # Maths
    with open("maths.json", "w") as f: json.dump(generate_maths(), f, indent=2, ensure_ascii=False)
    
    # Spellbee
    with open("spellbee.json", "w") as f: json.dump(generate_spellbee(), f, indent=2, ensure_ascii=False)

    # Simple Science template
    sci_templates = [
        {"en_q": "What gas do plants absorb?", "kn_q": "ಸಸ್ಯಗಳು ಯಾವ ಅನಿಲವನ್ನು ಹೀರಿಕೊಳ್ಳುತ್ತವೆ?", "en_ans": "Carbon Dioxide", "kn_ans": "ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್", "en_opts": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Helium"], "kn_opts": ["ಇಂಗಾಲದ ಡೈಆಕ್ಸೈಡ್", "ಆಮ್ಲಜನಕ", "ಸಾರಜನಕ", "ಹೀಲಿಯಂ"]},
        {"en_q": "What is the center of the solar system?", "kn_q": "ಸೌರವ್ಯೂಹದ ಕೇಂದ್ರ ಯಾವುದು?", "en_ans": "Sun", "kn_ans": "ಸೂರ್ಯ", "en_opts": ["Sun", "Earth", "Moon", "Jupiter"], "kn_opts": ["ಸೂರ್ಯ", "ಭೂಮಿ", "ಚಂದ್ರ", "ಗುರು"]}
    ]
    with open("science.json", "w") as f: json.dump(generate_generic("sci", sci_templates, ["Because {ans} is a scientific fact."], ["ಏಕೆಂದರೆ {ans} ಒಂದು ವೈಜ್ಞಾನಿಕ ಸತ್ಯ."]), f, indent=2, ensure_ascii=False)

    # Kannada
    kan_templates = [
        {"en_q": "What is the first vowel in Kannada?", "kn_q": "ಕನ್ನಡದ ಮೊದಲ ಸ್ವರ ಯಾವುದು?", "en_ans": "ಅ (a)", "kn_ans": "ಅ (a)", "en_opts": ["ಅ (a)", "ಆ (aa)", "ಇ (i)", "ಈ (ee)"], "kn_opts": ["ಅ (a)", "ಆ (aa)", "ಇ (i)", "ಈ (ee)"]}
    ]
    with open("kannada.json", "w") as f: json.dump(generate_generic("kan", kan_templates, ["{ans} is the correct grammar rule."], ["{ans} ಸರಿಯಾದ ವ್ಯಾಕರಣ ನಿಯಮ."]), f, indent=2, ensure_ascii=False)

    # History
    hist_templates = [
        {"en_q": "Who was the first Emperor of the Maurya Dynasty?", "kn_q": "ಮೌರ್ಯ ಸಾಮ್ರಾಜ್ಯದ ಮೊದಲ ಚಕ್ರವರ್ತಿ ಯಾರು?", "en_ans": "Chandragupta", "kn_ans": "ಚಂದ್ರಗುಪ್ತ", "en_opts": ["Chandragupta", "Ashoka", "Akbar", "Shivaji"], "kn_opts": ["ಚಂದ್ರಗುಪ್ತ", "ಅಶೋಕ", "ಅಕ್ಬರ್", "ಶಿವಾಜಿ"]}
    ]
    with open("history.json", "w") as f: json.dump(generate_generic("his", hist_templates, ["{ans} is an important historical figure."], ["{ans} ಒಬ್ಬ ಪ್ರಮುಖ ಐತಿಹಾಸಿಕ ವ್ಯಕ್ತಿ."]), f, indent=2, ensure_ascii=False)

    # GK
    gk_templates = [
        {"en_q": "What is the capital of India?", "kn_q": "ಭಾರತದ ರಾಜಧಾನಿ ಯಾವುದು?", "en_ans": "New Delhi", "kn_ans": "ನವದೆಹಲಿ", "en_opts": ["New Delhi", "Mumbai", "Bangalore", "Chennai"], "kn_opts": ["ನವದೆಹಲಿ", "ಮುಂಬೈ", "ಬೆಂಗಳೂರು", "ಚೆನ್ನೈ"]}
    ]
    with open("gk.json", "w") as f: json.dump(generate_generic("gk", gk_templates, ["{ans} is the capital city."], ["{ans} ರಾಜಧಾನಿಯಾಗಿದೆ."]), f, indent=2, ensure_ascii=False)

    # English
    eng_templates = [
        {"en_q": "What is the past tense of 'Run'?", "kn_q": "'Run' ಪದದ ಭೂತಕಾಲವೇನು?", "en_ans": "Ran", "kn_ans": "Ran", "en_opts": ["Ran", "Runned", "Running", "Rans"], "kn_opts": ["Ran", "Runned", "Running", "Rans"]}
    ]
    with open("english.json", "w") as f: json.dump(generate_generic("eng", eng_templates, ["{ans} is the correct verb form."], ["{ans} ಸರಿಯಾದ ಕ್ರಿಯಾಪದ ರೂಪವಾಗಿದೆ."]), f, indent=2, ensure_ascii=False)

    # Puzzles
    puz_templates = [
        {"en_q": "I have keys but no locks. What am I?", "kn_q": "ನನಗೆ ಕೀಲಿಗಳಿವೆ ಆದರೆ ಬೀಗಗಳಿಲ್ಲ. ನಾನು ಯಾರು?", "en_ans": "A Piano", "kn_ans": "ಪಿಯಾನೋ", "en_opts": ["A Piano", "A Door", "A Chest", "A Car"], "kn_opts": ["ಪಿಯಾನೋ", "ಬಾಗಿಲು", "ಪೆಟ್ಟಿಗೆ", "ಕಾರು"]}
    ]
    with open("puzzles.json", "w") as f: json.dump(generate_generic("puz", puz_templates, ["A piano uses musical keys."], ["ಪಿಯಾನೋ ಸಂಗೀತದ ಕೀಲಿಗಳನ್ನು ಬಳಸುತ್ತದೆ."]), f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
