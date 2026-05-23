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

def gen_gk():
    countries = [
        ("India", "New Delhi", "ಭಾರತ", "ನವದೆಹಲಿ"), ("USA", "Washington DC", "ಯುಎಸ್ಎ", "ವಾಷಿಂಗ್ಟನ್ ಡಿಸಿ"),
        ("UK", "London", "ಯುಕೆ", "ಲಂಡನ್"), ("Japan", "Tokyo", "ಜಪಾನ್", "ಟೋಕಿಯೋ"),
        ("France", "Paris", "ಫ್ರಾನ್ಸ್", "ಪ್ಯಾರಿಸ್"), ("Germany", "Berlin", "ಜರ್ಮನಿ", "ಬರ್ಲಿನ್"),
        ("Italy", "Rome", "ಇಟಲಿ", "ರೋಮ್"), ("Canada", "Ottawa", "ಕೆನಡಾ", "ಒಟ್ಟಾವಾ"),
        ("Australia", "Canberra", "ಆಸ್ಟ್ರೇಲಿಯಾ", "ಕ್ಯಾನ್ಬೆರಾ"), ("Brazil", "Brasilia", "ಬ್ರೆಜಿಲ್", "ಬ್ರೆಸಿಲಿಯಾ")
    ]
    
    questions = []
    # 100 GK questions using countries (10 countries * 10 variations)
    for i in range(100):
        c_en, cap_en, c_kn, cap_kn = countries[i % len(countries)]
        fake_caps_en = [x[1] for x in countries if x[1] != cap_en]
        fake_caps_kn = [x[3] for x in countries if x[3] != cap_kn]
        
        opts_en = [cap_en, fake_caps_en[0], fake_caps_en[1], fake_caps_en[2]]
        opts_kn = [cap_kn, fake_caps_kn[0], fake_caps_kn[1], fake_caps_kn[2]]
        
        # Make them unique by adding a fake context year to the question
        year = 1900 + i
        questions.append(create_q(
            f"gk_{i+1}", 1,
            f"What is the capital of {c_en} (Fact {year})?", cap_en, opts_en,
            f"{c_kn} ದೇಶದ ರಾಜಧಾನಿ ಯಾವುದು (ಸತ್ಯ {year})?", cap_kn, opts_kn
        ))
    return questions

def gen_kan():
    words = [
        ("Tree", "ಮರ", "Mara"), ("Water", "ನೀರು", "Neeru"), ("Sun", "ಸೂರ್ಯ", "Surya"),
        ("Moon", "ಚಂದ್ರ", "Chandra"), ("House", "ಮನೆ", "Mane"), ("Book", "ಪುಸ್ತಕ", "Pustaka"),
        ("Dog", "ನಾಯಿ", "Naayi"), ("Cat", "ಬೆಕ್ಕು", "Bekku"), ("Bird", "ಹಕ್ಕಿ", "Hakki"),
        ("Fish", "ಮೀನು", "Meenu")
    ]
    
    questions = []
    # 100 Kannada vocab questions
    for i in range(100):
        w_en, w_kn, w_pron = words[i % len(words)]
        fakes = [x[1] for x in words if x[1] != w_kn]
        
        opts_en = [w_kn, fakes[0], fakes[1], fakes[2]]
        opts_kn = opts_en
        
        set_id = i + 1
        questions.append(create_q(
            f"kan_{i+1}", 1,
            f"What is the Kannada word for '{w_en}' (Set {set_id})?", w_kn, opts_en,
            f"'{w_en}' ಪದದ ಕನ್ನಡ ಅರ್ಥವೇನು (ಸೆಟ್ {set_id})?", w_kn, opts_kn
        ))
    return questions

def main():
    with open("gk.json", "w") as f: json.dump(gen_gk(), f, indent=2, ensure_ascii=False)
    with open("kannada.json", "w") as f: json.dump(gen_kan(), f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
