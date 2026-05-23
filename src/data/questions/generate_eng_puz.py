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

def gen_english():
    questions = []
    # 100 verb past tense questions
    for i in range(1, 101):
        diff = 1 if i < 33 else (2 if i < 66 else 3)
        verb = f"Verb{i}"
        ans = f"{verb}ed"
        opts = [ans, f"{verb}d", f"{verb}ing", f"{verb}s"]
        
        questions.append(create_q(
            f"eng_{i}", diff,
            f"What is the past tense of '{verb}'?", ans, opts,
            f"'{verb}' ನ ಭೂತಕಾಲವೇನು?", ans, opts
        ))
    return questions

def gen_puzzles():
    questions = []
    # 100 sequence puzzles: e.g. 2, 4, 6, ? 
    for i in range(1, 101):
        diff = 1 if i < 33 else (2 if i < 66 else 3)
        start = random.randint(1, 20)
        step = random.randint(2, 10)
        
        seq = [start, start + step, start + 2*step, start + 3*step]
        ans = start + 4*step
        
        opts = [str(ans), str(ans+step), str(ans-step), str(ans+2)]
        
        questions.append(create_q(
            f"puz_{i}", diff,
            f"What comes next in the sequence: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...?", str(ans), opts,
            f"ಈ ಸರಣಿಯಲ್ಲಿ ಮುಂದೆ ಏನು ಬರುತ್ತದೆ: {seq[0]}, {seq[1]}, {seq[2]}, {seq[3]}, ...?", str(ans), opts
        ))
    return questions

def main():
    with open("english.json", "w") as f: json.dump(gen_english(), f, indent=2, ensure_ascii=False)
    with open("puzzles.json", "w") as f: json.dump(gen_puzzles(), f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
