import json
import random

questions = []
id_counter = 1

def add_q(diff, q_text, ans, opts, reason):
    global id_counter
    random.shuffle(opts)
    questions.append({
        "id": f"math_{id_counter:03d}",
        "difficulty": diff,
        "question": q_text,
        "options": [str(o) for o in opts],
        "answer": str(ans),
        "reasoning": reason
    })
    id_counter += 1

# Easy (Level 1) - 17 questions
for _ in range(17):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(['+', '-'])
    if op == '-':
        if a < b: a, b = b, a # Ensure positive result
    ans = a + b if op == '+' else a - b
    opts = set([ans])
    while len(opts) < 4:
        opts.add(ans + random.randint(-5, 5))
        if 0 in opts and ans != 0: opts.remove(0)
    
    add_q(1, f"What is {a} {op} {b}?", ans, list(opts), f"{a} {op} {b} equals {ans}.")

# Medium (Level 2) - 17 questions
for _ in range(17):
    a = random.randint(2, 12)
    b = random.randint(2, 10)
    ans = a * b
    opts = set([ans])
    while len(opts) < 4:
        opts.add(ans + random.choice([-2, -1, 1, 2]) * a)
    add_q(2, f"What is {a} x {b}?", ans, list(opts), f"{a} multiplied by {b} is {ans}.")

# Hard (Level 3) - 16 questions (Word problems & division)
for i in range(16):
    a = random.randint(2, 10)
    ans = random.randint(3, 12)
    total = a * ans
    
    opts = set([ans])
    while len(opts) < 4:
        opts.add(ans + random.randint(-3, 3))
        if 0 in opts: opts.remove(0)
    
    q_texts = [
        f"If you have {total} gears and divide them equally among {a} engines, how many does each get?",
        f"A Tuk-Tuk travels {total} km in {a} hours. What is its speed in km/h?",
        f"Professor Puffin bought {a} items for a total of {total} coins. How much did one item cost?"
    ]
    q_text = random.choice(q_texts)
    add_q(3, q_text, ans, list(opts), f"{total} divided by {a} is {ans}.")

with open('src/data/questions/maths.json', 'w') as f:
    json.dump(questions, f, indent=2)

print("Generated maths.json")
