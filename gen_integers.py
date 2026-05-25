import json
import os

questions = []
# 10 Easy, 10 Medium, 10 Hard
# 15 single, 5 image_single, 3 multiple, 2 image_multiple, 5 match

q = 1

def add_single(diff, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_int_{q:03d}",
        "type": "single",
        "difficulty": diff,
        "en": {
            "question": en_q,
            "options": en_opts,
            "answer": en_ans,
            "reasoning": en_reas
        },
        "kn": {
            "question": kn_q,
            "options": kn_opts,
            "answer": kn_ans,
            "reasoning": kn_reas
        }
    })
    q += 1

def add_multiple(diff, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_int_{q:03d}",
        "type": "multiple",
        "difficulty": diff,
        "en": {
            "question": en_q,
            "options": en_opts,
            "answer": en_ans,
            "reasoning": en_reas
        },
        "kn": {
            "question": kn_q,
            "options": kn_opts,
            "answer": kn_ans,
            "reasoning": kn_reas
        }
    })
    q += 1

def add_match(diff, en_q, kn_q, en_pairs, kn_pairs, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_int_{q:03d}",
        "type": "match",
        "difficulty": diff,
        "en": {
            "question": en_q,
            "pairs": en_pairs,
            "reasoning": en_reas
        },
        "kn": {
            "question": kn_q,
            "pairs": kn_pairs,
            "reasoning": kn_reas
        }
    })
    q += 1

def add_image_single(diff, svg, en_alt, kn_alt, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_int_{q:03d}",
        "type": "image_single",
        "difficulty": diff,
        "image": {
            "type": "svg",
            "svg": svg.strip(),
            "alt": {
                "en": en_alt,
                "kn": kn_alt
            }
        },
        "en": {
            "question": en_q,
            "options": en_opts,
            "answer": en_ans,
            "reasoning": en_reas
        },
        "kn": {
            "question": kn_q,
            "options": kn_opts,
            "answer": kn_ans,
            "reasoning": kn_reas
        }
    })
    q += 1

def add_image_multiple(diff, svg, en_alt, kn_alt, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_int_{q:03d}",
        "type": "image_multiple",
        "difficulty": diff,
        "image": {
            "type": "svg",
            "svg": svg.strip(),
            "alt": {
                "en": en_alt,
                "kn": kn_alt
            }
        },
        "en": {
            "question": en_q,
            "options": en_opts,
            "answer": en_ans,
            "reasoning": en_reas
        },
        "kn": {
            "question": kn_q,
            "options": kn_opts,
            "answer": kn_ans,
            "reasoning": kn_reas
        }
    })
    q += 1

# Easy (10)
# 6 single, 2 image_single, 1 multiple, 1 match
add_single(1, "What is the result of (-5) + 3?", "(-5) + 3 ರ ಫಲಿತಾಂಶವೇನು?", ["-2", "2", "-8", "8"], ["-2", "2", "-8", "8"], "-2", "-2", "When adding a positive and a negative integer, find the difference of their absolute values and use the sign of the larger absolute value.", "ಧನಾತ್ಮಕ ಮತ್ತು ಋಣಾತ್ಮಕ ಪೂರ್ಣಾಂಕವನ್ನು ಸೇರಿಸುವಾಗ, ಅವುಗಳ ಸಂಪೂರ್ಣ ಮೌಲ್ಯಗಳ ವ್ಯತ್ಯಾಸವನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ ಮತ್ತು ದೊಡ್ಡ ಸಂಪೂರ್ಣ ಮೌಲ್ಯದ ಚಿಹ್ನೆಯನ್ನು ಬಳಸಿ.")
add_single(1, "Which of the following is the additive inverse of -12?", "-12 ರ ಸಂಕಲನದ ವಿಲೋಮ (additive inverse) ಯಾವುದು?", ["12", "-12", "0", "1"], ["12", "-12", "0", "1"], "12", "12", "The additive inverse of a number a is -a, such that a + (-a) = 0.", "ಒಂದು ಸಂಖ್ಯೆ a ಯ ಸಂಕಲನದ ವಿಲೋಮ -a, ಏಕೆಂದರೆ a + (-a) = 0.")
add_single(1, "What is the product of (-4) and (-6)?", "(-4) ಮತ್ತು (-6) ರ ಗುಣಲಬ್ಧವೇನು?", ["-24", "24", "10", "-10"], ["-24", "24", "10", "-10"], "24", "24", "The product of two negative integers is always a positive integer.", "ಎರಡು ಋಣಾತ್ಮಕ ಪೂರ್ಣಾಂಕಗಳ ಗುಣಲಬ್ಧವು ಯಾವಾಗಲೂ ಧನಾತ್ಮಕ ಪೂರ್ಣಾಂಕವಾಗಿರುತ್ತದೆ.")
add_single(1, "Evaluate: 0 ÷ (-8)", "ಮೌಲ್ಯೀಕರಿಸಿ: 0 ÷ (-8)", ["0", "-8", "8", "Not defined"], ["0", "-8", "8", "ವ್ಯಾಖ್ಯಾನಿಸಲಾಗಿಲ್ಲ"], "0", "0", "Zero divided by any non-zero integer is zero.", "ಯಾವುದೇ ಶೂನ್ಯವಲ್ಲದ ಪೂರ್ಣಾಂಕದಿಂದ ಶೂನ್ಯವನ್ನು ಭಾಗಿಸಿದಾಗ ಫಲಿತಾಂಶ ಶೂನ್ಯವೇ ಆಗಿರುತ್ತದೆ.")
add_single(1, "Which integer is greater: -15 or -7?", "ಯಾವ ಪೂರ್ಣಾಂಕವು ದೊಡ್ಡದು: -15 ಅಥವಾ -7?", ["-15", "-7", "They are equal", "Cannot be determined"], ["-15", "-7", "ಅವು ಸಮ", "ನಿರ್ಧರಿಸಲಾಗುವುದಿಲ್ಲ"], "-7", "-7", "On the number line, -7 lies to the right of -15, so -7 is greater.", "ಸಂಖ್ಯಾರೇಖೆಯಲ್ಲಿ -15 ರ ಬಲಭಾಗದಲ್ಲಿ -7 ಇರುವುದರಿಂದ, -7 ದೊಡ್ಡದು.")
add_single(1, "What is the result of 10 - (-5)?", "10 - (-5) ರ ಫಲಿತಾಂಶವೇನು?", ["5", "-5", "15", "-15"], ["5", "-5", "15", "-15"], "15", "15", "Subtracting a negative integer is the same as adding its positive equivalent: 10 + 5 = 15.", "ಋಣಾತ್ಮಕ ಪೂರ್ಣಾಂಕವನ್ನು ಕಳೆಯುವುದು ಅದರ ಧನಾತ್ಮಕ ಮೌಲ್ಯವನ್ನು ಸೇರಿಸುವುದಕ್ಕೆ ಸಮ: 10 + 5 = 15.")

add_image_single(1, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 100">
  <line x1="20" y1="50" x2="280" y2="50" stroke="#2563EB" stroke-width="2" stroke-linecap="round"/>
  <polygon points="280,50 272,44 272,56" fill="#2563EB"/>
  <polygon points="20,50 28,44 28,56" fill="#2563EB"/>
  <line x1="150" y1="40" x2="150" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="150" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">0</text>
  <line x1="110" y1="40" x2="110" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="110" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">-1</text>
  <line x1="70" y1="40" x2="70" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="70" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">-2</text>
  <line x1="30" y1="40" x2="30" y2="60" stroke="#2563EB" stroke-width="1.5"/>
  <text x="30" y="75" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">A</text>
  <circle cx="30" cy="50" r="6" fill="#DC2626" stroke="white" stroke-width="2"/>
</svg>""", "A number line showing 0, -1, -2 and point A.", "0, -1, -2 ಮತ್ತು ಬಿಂದು A ಅನ್ನು ತೋರಿಸುವ ಸಂಖ್ಯಾ ರೇಖೆ.", "What integer does point A represent on the number line?", "ಸಂಖ್ಯಾ ರೇಖೆಯ ಮೇಲಿನ A ಬಿಂದುವು ಯಾವ ಪೂರ್ಣಾಂಕವನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತದೆ?", ["-3", "-4", "3", "1"], ["-3", "-4", "3", "1"], "-3", "-3", "Point A is one unit to the left of -2, which corresponds to -3.", "A ಬಿಂದುವು -2 ರ ಎಡಭಾಗದಲ್ಲಿ ಒಂದು ಮಾನ ದೂರದಲ್ಲಿದೆ, ಆದ್ದರಿಂದ ಇದು -3 ಆಗಿದೆ.")

add_image_single(1, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <rect x="100" y="50" width="100" height="100" fill="#DBEAFE" stroke="#2563EB" stroke-width="2" rx="2"/>
  <text x="150" y="105" fill="#DC2626" font-family="Arial, sans-serif" font-size="24" text-anchor="middle" font-weight="bold">-18</text>
  <text x="150" y="140" fill="#1F2937" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">÷ 3</text>
</svg>""", "A box showing -18 divided by 3.", "-18 ನ್ನು 3 ರಿಂದ ಭಾಗಿಸುವಿಕೆಯನ್ನು ತೋರಿಸುವ ಬಾಕ್ಸ್.", "Calculate the value shown in the image.", "ಚಿತ್ರದಲ್ಲಿ ತೋರಿಸಿರುವ ಮೌಲ್ಯವನ್ನು ಲೆಕ್ಕ ಹಾಕಿ.", ["-6", "6", "-54", "54"], ["-6", "6", "-54", "54"], "-6", "-6", "When a negative integer is divided by a positive integer, the result is negative: -18 ÷ 3 = -6.", "ಋಣಾತ್ಮಕ ಪೂರ್ಣಾಂಕವನ್ನು ಧನಾತ್ಮಕ ಪೂರ್ಣಾಂಕದಿಂದ ಭಾಗಿಸಿದಾಗ, ಫಲಿತಾಂಶವು ಋಣಾತ್ಮಕವಾಗಿರುತ್ತದೆ: -18 ÷ 3 = -6.")

add_multiple(1, "Which of the following expressions equal -10?", "ಕೆಳಗಿನ ಯಾವ ಅಭಿವ್ಯಕ್ತಿಗಳು -10 ಕ್ಕೆ ಸಮನಾಗಿವೆ?", ["-5 + (-5)", "-20 + 10", "5 - 15", "10 - 20"], ["-5 + (-5)", "-20 + 10", "5 - 15", "10 - 20"], ["-5 + (-5)", "-20 + 10", "5 - 15", "10 - 20"], ["-5 + (-5)", "-20 + 10", "5 - 15", "10 - 20"], "All of the expressions evaluate to -10.", "ಎಲ್ಲಾ ಅಭಿವ್ಯಕ್ತಿಗಳ ಮೌಲ್ಯವು -10 ಆಗಿದೆ.")

add_match(1, "Match the expression to its value:", "ಅಭಿವ್ಯಕ್ತಿಯನ್ನು ಅದರ ಮೌಲ್ಯದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "-3 + 4", "right": "1"}, {"left": "-3 - 4", "right": "-7"}, {"left": "3 - 4", "right": "-1"}, {"left": "3 + 4", "right": "7"}], [{"left": "-3 + 4", "right": "1"}, {"left": "-3 - 4", "right": "-7"}, {"left": "3 - 4", "right": "-1"}, {"left": "3 + 4", "right": "7"}], "Basic integer addition and subtraction rules apply.", "ಮೂಲ ಪೂರ್ಣಾಂಕಗಳ ಸಂಕಲನ ಮತ್ತು ವ್ಯವಕಲನದ ನಿಯಮಗಳು ಅನ್ವಯಿಸುತ್ತವೆ.")

# Medium (10)
# 5 single, 2 image_single, 1 image_multiple, 1 multiple, 1 match
add_single(2, "By how much does -3 exceed -7?", "-3, -7 ಗಿಂತ ಎಷ್ಟು ಹೆಚ್ಚಾಗಿದೆ?", ["4", "-4", "10", "-10"], ["4", "-4", "10", "-10"], "4", "4", "To find how much it exceeds, subtract the smaller from the larger: -3 - (-7) = -3 + 7 = 4.", "ಎಷ್ಟು ಹೆಚ್ಚಾಗಿದೆ ಎಂದು ತಿಳಿಯಲು, ದೊಡ್ಡದರಿಂದ ಚಿಕ್ಕದನ್ನು ಕಳೆಯಿರಿ: -3 - (-7) = -3 + 7 = 4.")
add_single(2, "What is the product of three negative integers and two positive integers?", "ಮೂರು ಋಣಾತ್ಮಕ ಪೂರ್ಣಾಂಕಗಳು ಮತ್ತು ಎರಡು ಧನಾತ್ಮಕ ಪೂರ್ಣಾಂಕಗಳ ಗುಣಲಬ್ಧದ ಚಿಹ್ನೆ ಏನು?", ["Always positive", "Always negative", "Can be zero", "Cannot be determined"], ["ಯಾವಾಗಲೂ ಧನಾತ್ಮಕ", "ಯಾವಾಗಲೂ ಋಣಾತ್ಮಕ", "ಶೂನ್ಯವಾಗಿರಬಹುದು", "ನಿರ್ಧರಿಸಲಾಗುವುದಿಲ್ಲ"], "Always negative", "ಯಾವಾಗಲೂ ಋಣಾತ್ಮಕ", "The product of an odd number of negative integers is always negative.", "ಬೆಸ ಸಂಖ್ಯೆಯ ಋಣಾತ್ಮಕ ಪೂರ್ಣಾಂಕಗಳ ಗುಣಲಬ್ಧವು ಯಾವಾಗಲೂ ಋಣಾತ್ಮಕವಾಗಿರುತ್ತದೆ.")
add_single(2, "Find the value of: [(-15) × (-3)] ÷ [(-9) ÷ 3]", "[(-15) × (-3)] ÷ [(-9) ÷ 3] ರ ಮೌಲ್ಯವನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.", ["15", "-15", "5", "-5"], ["15", "-15", "5", "-5"], "-15", "-15", "First part: -15 × -3 = 45. Second part: -9 ÷ 3 = -3. Then, 45 ÷ -3 = -15.", "ಮೊದಲ ಭಾಗ: -15 × -3 = 45. ಎರಡನೇ ಭಾಗ: -9 ÷ 3 = -3. ನಂತರ, 45 ÷ -3 = -15.")
add_single(2, "If a = -5, b = -6, and c = 10, find a × (b + c).", "a = -5, b = -6, ಮತ್ತು c = 10 ಆದರೆ, a × (b + c) ಅನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.", ["-20", "20", "80", "-80"], ["-20", "20", "80", "-80"], "-20", "-20", "According to BODMAS: b + c = -6 + 10 = 4. Then a × 4 = -5 × 4 = -20.", "BODMAS ಪ್ರಕಾರ: b + c = -6 + 10 = 4. ನಂತರ a × 4 = -5 × 4 = -20.")
add_single(2, "Which property is illustrated by the equation: (-2) × [3 + (-4)] = [(-2) × 3] + [(-2) × (-4)]?", "(-2) × [3 + (-4)] = [(-2) × 3] + [(-2) × (-4)] ಸಮೀಕರಣವು ಯಾವ ಗುಣಲಕ್ಷಣವನ್ನು ವಿವರಿಸುತ್ತದೆ?", ["Commutative property", "Associative property", "Distributive property", "Closure property"], ["ಪರಿವರ್ತನೀಯ ಗುಣ (Commutative)", "ಸಹವರ್ತನೀಯ ಗುಣ (Associative)", "ವಿಭಾಜಕ ಗುಣ (Distributive)", "ಸಂವೃತ ಗುಣ (Closure)"], "Distributive property", "ವಿಭಾಜಕ ಗುಣ (Distributive)", "This is the distributive property of multiplication over addition: a × (b + c) = (a × b) + (a × c).", "ಇದು ಸಂಕಲನದ ಮೇಲಿನ ಗುಣಾಕಾರದ ವಿಭಾಜಕ ಗುಣಲಕ್ಷಣವಾಗಿದೆ: a × (b + c) = (a × b) + (a × c).")

add_image_single(2, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 150">
  <path d="M 50,75 Q 100,25 150,75" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow)"/>
  <path d="M 150,75 Q 200,25 250,75" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="100" y="40" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">+4</text>
  <text x="200" y="40" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">-7</text>
  <line x1="20" y1="75" x2="280" y2="75" stroke="#2563EB" stroke-width="2" stroke-linecap="round"/>
  <circle cx="50" cy="75" r="4" fill="#059669"/>
  <text x="50" y="95" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">-2</text>
  <circle cx="150" cy="75" r="4" fill="#059669"/>
  <text x="150" y="95" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">2</text>
  <circle cx="250" cy="75" r="4" fill="#DC2626"/>
  <text x="250" y="95" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">?</text>
  <defs>
    <marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6" fill="#EA580C"/>
    </marker>
  </defs>
</svg>""", "Number line showing a jump of +4 from -2 to 2, and then a jump of -7 from 2.", "ಸಂಖ್ಯಾರೇಖೆಯು -2 ರಿಂದ 2 ಕ್ಕೆ +4 ರ ಜಿಗಿತವನ್ನು ಮತ್ತು ನಂತರ 2 ರಿಂದ -7 ರ ಜಿಗಿತವನ್ನು ತೋರಿಸುತ್ತದೆ.", "What is the final position on the number line after the two jumps?", "ಎರಡು ಜಿಗಿತಗಳ ನಂತರ ಸಂಖ್ಯಾರೇಖೆಯಲ್ಲಿನ ಅಂತಿಮ ಸ್ಥಾನ ಯಾವುದು?", ["-5", "5", "-9", "9"], ["-5", "5", "-9", "9"], "-5", "-5", "Starting at -2, we jump right by 4 (+4) reaching 2. Then jump left by 7 (-7) reaching 2 - 7 = -5.", "-2 ರಿಂದ ಪ್ರಾರಂಭಿಸಿ, ನಾವು ಬಲಕ್ಕೆ 4 ಜಿಗಿಯುತ್ತೇವೆ (+4) ಆಗ 2 ತಲುಪುತ್ತೇವೆ. ನಂತರ ಎಡಕ್ಕೆ 7 ಜಿಗಿಯುತ್ತೇವೆ (-7) ಆಗ 2 - 7 = -5 ನ್ನು ತಲುಪುತ್ತೇವೆ.")

add_image_single(2, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <rect x="50" y="50" width="200" height="100" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <line x1="50" y1="100" x2="250" y2="100" stroke="#2563EB" stroke-width="2"/>
  <line x1="150" y1="50" x2="150" y2="150" stroke="#2563EB" stroke-width="2"/>
  <text x="100" y="85" fill="#1F2937" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">-12</text>
  <text x="200" y="85" fill="#1F2937" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">x</text>
  <text x="100" y="135" fill="#1F2937" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">y</text>
  <text x="200" y="135" fill="#1F2937" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">48</text>
</svg>""", "A 2x2 grid where the product of rows and columns is constant.", "ಸಾಲುಗಳು ಮತ್ತು ಕಾಲಮ್‌ಗಳ ಗುಣಲಬ್ಧ ಸ್ಥಿರವಾಗಿರುವ 2x2 ಚೌಕ.", "If the product of integers in each row and column is identical, what is the value of x?", "ಪ್ರತಿ ಸಾಲು ಮತ್ತು ಕಾಲಮ್‌ನಲ್ಲಿರುವ ಪೂರ್ಣಾಂಕಗಳ ಗುಣಲಬ್ಧ ಒಂದೇ ಆಗಿದ್ದರೆ, x ನ ಮೌಲ್ಯವೇನು?", ["-4", "4", "12", "-12"], ["-4", "4", "12", "-12"], "-4", "-4", "Let the product be P. -12 * x = y * 48 = -12 * y = x * 48. From columns, -12 * y = P. From rows, x * 48 = P. Since x * 48 = -12 * y, solving yields x = -4 when y = 16. Product is 48. So -12 * (-4) = 48.", "ಸಾಲು ಮತ್ತು ಕಾಲಮ್‌ನ ಗುಣಲಬ್ಧ 48. ಆದ್ದರಿಂದ -12 * x = 48. x = 48 / -12 = -4.")

add_image_multiple(2, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <circle cx="150" cy="100" r="80" fill="none" stroke="#2563EB" stroke-width="2"/>
  <text x="150" y="60" fill="#DC2626" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">A: -2</text>
  <text x="110" y="120" fill="#DC2626" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">B: -8</text>
  <text x="190" y="120" fill="#DC2626" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">C: 4</text>
</svg>""", "A circle containing three values: A=-2, B=-8, C=4.", "ಮೂರು ಮೌಲ್ಯಗಳನ್ನು ಒಳಗೊಂಡಿರುವ ವೃತ್ತ: A=-2, B=-8, C=4.", "Which of the following statements are true about the values shown?", "ತೋರಿಸಿರುವ ಮೌಲ್ಯಗಳ ಬಗ್ಗೆ ಕೆಳಗಿನ ಯಾವ ಹೇಳಿಕೆಗಳು ಸರಿ?", ["A + B = -10", "A × C = -8", "B ÷ A = 4", "B > A"], ["A + B = -10", "A × C = -8", "B ÷ A = 4", "B > A"], ["A + B = -10", "A × C = -8", "B ÷ A = 4"], ["A + B = -10", "A × C = -8", "B ÷ A = 4"], "A + B = -2 + (-8) = -10. A × C = -2 × 4 = -8. B ÷ A = -8 ÷ -2 = 4. B > A is false because -8 is less than -2.", "A + B = -10. A × C = -8. B ÷ A = 4. -8 < -2 ಆಗಿರುವುದರಿಂದ B > A ಎಂಬುದು ತಪ್ಪು.")

add_multiple(2, "Which pairs of integers have a difference of -5? (Assuming form a - b)", "ಯಾವ ಪೂರ್ಣಾಂಕಗಳ ಜೋಡಿಯ ವ್ಯತ್ಯಾಸ -5 ಆಗಿದೆ? (a - b ರೂಪವನ್ನು ಊಹಿಸಿ)", ["(-2, 3)", "(3, 8)", "(10, 15)", "(-10, -5)"], ["(-2, 3)", "(3, 8)", "(10, 15)", "(-10, -5)"], ["(-2, 3)", "(3, 8)", "(10, 15)", "(-10, -5)"], ["(-2, 3)", "(3, 8)", "(10, 15)", "(-10, -5)"], "All these pairs result in -5: -2 - 3 = -5; 3 - 8 = -5; 10 - 15 = -5; -10 - (-5) = -5.", "ಈ ಎಲ್ಲಾ ಜೋಡಿಗಳ ಫಲಿತಾಂಶ -5: -2 - 3 = -5; 3 - 8 = -5; 10 - 15 = -5; -10 - (-5) = -5.")

add_match(2, "Match the property of integers with its general form:", "ಪೂರ್ಣಾಂಕಗಳ ಗುಣಲಕ್ಷಣಗಳನ್ನು ಅದರ ಸಾಮಾನ್ಯ ರೂಪದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "Commutative under Addition", "right": "a + b = b + a"}, {"left": "Associative under Addition", "right": "(a + b) + c = a + (b + c)"}, {"left": "Additive Identity", "right": "a + 0 = a"}, {"left": "Distributive Property", "right": "a × (b + c) = a × b + a × c"}], [{"left": "ಸಂಕಲನದ ಪರಿವರ್ತನೀಯ ಗುಣ", "right": "a + b = b + a"}, {"left": "ಸಂಕಲನದ ಸಹವರ್ತನೀಯ ಗುಣ", "right": "(a + b) + c = a + (b + c)"}, {"left": "ಸಂಕಲನದ ಅನನ್ಯತಾಂಶ", "right": "a + 0 = a"}, {"left": "ವಿಭಾಜಕ ಗುಣ", "right": "a × (b + c) = a × b + a × c"}], "These are standard properties of integers.", "ಇವು ಪೂರ್ಣಾಂಕಗಳ ಪ್ರಮಾಣಿತ ಗುಣಲಕ್ಷಣಗಳಾಗಿವೆ.")

# Hard (10)
# 4 single, 1 image_single, 1 image_multiple, 1 multiple, 3 match
add_single(3, "An elevator descends into a mine shaft at the rate of 6 m/min. If the descent starts from 10 m above the ground level, how long will it take to reach -350 m?", "ಒಂದು ಲಿಫ್ಟ್ ಗಣಿಯೊಳಗೆ 6 ಮೀ/ನಿಮಿಷ ದರದಲ್ಲಿ ಇಳಿಯುತ್ತದೆ. ಇದು ನೆಲಮಟ್ಟದಿಂದ 10 ಮೀ ಮೇಲಿನಿಂದ ಪ್ರಾರಂಭವಾದರೆ, -350 ಮೀ ತಲುಪಲು ಎಷ್ಟು ಸಮಯ ತೆಗೆದುಕೊಳ್ಳುತ್ತದೆ?", ["60 minutes", "50 minutes", "1 hour", "70 minutes"], ["60 ನಿಮಿಷ", "50 ನಿಮಿಷ", "1 ಗಂಟೆ", "70 ನಿಮಿಷ"], "1 hour", "1 ಗಂಟೆ", "Total distance = 10 - (-350) = 360 m. Time = Distance / Speed = 360 / 6 = 60 minutes = 1 hour.", "ಒಟ್ಟು ದೂರ = 10 - (-350) = 360 ಮೀ. ಸಮಯ = ದೂರ / ವೇಗ = 360 / 6 = 60 ನಿಮಿಷ = 1 ಗಂಟೆ.")
add_single(3, "A certain freezing process requires that room temperature be lowered from 40°C at the rate of 5°C every hour. What will be the room temperature 10 hours after the process begins?", "ಒಂದು ಫ್ರೀಜಿಂಗ್ ಪ್ರಕ್ರಿಯೆಯಲ್ಲಿ ಕೋಣೆಯ ಉಷ್ಣಾಂಶವನ್ನು 40°C ನಿಂದ ಪ್ರತಿ ಗಂಟೆಗೆ 5°C ದರದಲ್ಲಿ ಕಡಿಮೆ ಮಾಡಲಾಗುತ್ತದೆ. ಪ್ರಕ್ರಿಯೆ ಪ್ರಾರಂಭವಾದ 10 ಗಂಟೆಗಳ ನಂತರ ಕೋಣೆಯ ಉಷ್ಣಾಂಶ ಎಷ್ಟು ಇರುತ್ತದೆ?", ["-10°C", "10°C", "-50°C", "90°C"], ["-10°C", "10°C", "-50°C", "90°C"], "-10°C", "-10°C", "Temperature change = 10 × (-5) = -50°C. Final temperature = 40 + (-50) = -10°C.", "ಉಷ್ಣಾಂಶದ ಬದಲಾವಣೆ = 10 × (-5) = -50°C. ಅಂತಿಮ ಉಷ್ಣಾಂಶ = 40 + (-50) = -10°C.")
add_single(3, "In a class test containing 15 questions, 4 marks are given for every correct answer and (-2) marks are given for every incorrect answer. Gurpreet attempts all questions but only 9 of her answers are correct. What is her total score?", "15 ಪ್ರಶ್ನೆಗಳಿರುವ ಒಂದು ತರಗತಿ ಪರೀಕ್ಷೆಯಲ್ಲಿ, ಪ್ರತಿ ಸರಿಯಾದ ಉತ್ತರಕ್ಕೆ 4 ಅಂಕಗಳನ್ನು ಮತ್ತು ಪ್ರತಿ ತಪ್ಪಾದ ಉತ್ತರಕ್ಕೆ (-2) ಅಂಕಗಳನ್ನು ನೀಡಲಾಗುತ್ತದೆ. ಗುರುಪ್ರೀತ್ ಎಲ್ಲಾ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸುತ್ತಾಳೆ ಆದರೆ ಅವಳ 9 ಉತ್ತರಗಳು ಮಾತ್ರ ಸರಿಯಾಗಿವೆ. ಅವಳ ಒಟ್ಟು ಅಂಕ ಎಷ್ಟು?", ["36", "24", "26", "30"], ["36", "24", "26", "30"], "24", "24", "Marks for correct: 9 × 4 = 36. Incorrect: (15-9) = 6. Marks for incorrect: 6 × (-2) = -12. Total = 36 - 12 = 24.", "ಸರಿಯಾದ ಉತ್ತರಗಳಿಗೆ: 9 × 4 = 36. ತಪ್ಪಾದ ಉತ್ತರಗಳು: 6. ತಪ್ಪಾದ ಉತ್ತರಗಳಿಗೆ: 6 × (-2) = -12. ಒಟ್ಟು = 36 - 12 = 24.")
add_single(3, "Find the integer which when divided by -1 yields -89.", "-1 ರಿಂದ ಭಾಗಿಸಿದಾಗ -89 ನ್ನು ಕೊಡುವ ಪೂರ್ಣಾಂಕವನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.", ["89", "-89", "1", "-1"], ["89", "-89", "1", "-1"], "89", "89", "Let the integer be x. x ÷ (-1) = -89 => x = -89 × (-1) = 89.", "ಪೂರ್ಣಾಂಕ x ಆಗಿರಲಿ. x ÷ (-1) = -89 => x = -89 × (-1) = 89.")

add_image_single(3, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <polygon points="150,20 250,150 50,150" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <text x="150" y="45" fill="#DC2626" font-family="Arial, sans-serif" font-size="16" text-anchor="middle" font-weight="bold">-5</text>
  <text x="75" y="140" fill="#DC2626" font-family="Arial, sans-serif" font-size="16" text-anchor="middle" font-weight="bold">a</text>
  <text x="225" y="140" fill="#DC2626" font-family="Arial, sans-serif" font-size="16" text-anchor="middle" font-weight="bold">-4</text>
  <circle cx="150" cy="110" r="20" fill="white" stroke="#EA580C" stroke-width="2"/>
  <text x="150" y="115" fill="#1F2937" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">120</text>
</svg>""", "A triangle with vertices labeled -5, a, and -4. The center has the number 120.", "-5, a, ಮತ್ತು -4 ಎಂದು ಲೇಬಲ್ ಮಾಡಲಾದ ಶೃಂಗಗಳನ್ನು ಹೊಂದಿರುವ ತ್ರಿಕೋನ. ಕೇಂದ್ರದಲ್ಲಿ 120 ಎಂಬ ಸಂಖ್ಯೆ ಇದೆ.", "If the number in the center is the product of the numbers at the vertices, what is the value of a?", "ಕೇಂದ್ರದಲ್ಲಿರುವ ಸಂಖ್ಯೆಯು ಶೃಂಗಗಳಲ್ಲಿರುವ ಸಂಖ್ಯೆಗಳ ಗುಣಲಬ್ಧವಾಗಿದ್ದರೆ, a ನ ಮೌಲ್ಯವೇನು?", ["6", "-6", "10", "-10"], ["6", "-6", "10", "-10"], "6", "6", "Product of vertices = (-5) × a × (-4) = 20a. Given 20a = 120, so a = 6.", "ಶೃಂಗಗಳ ಗುಣಲಬ್ಧ = (-5) × a × (-4) = 20a. 20a = 120 ಎಂದು ನೀಡಲಾಗಿದೆ, ಆದ್ದರಿಂದ a = 6.")

add_image_multiple(3, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <rect x="30" y="50" width="80" height="80" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <text x="70" y="95" fill="#1F2937" font-family="Arial, sans-serif" font-size="20" text-anchor="middle">x</text>
  <text x="135" y="95" fill="#DC2626" font-family="Arial, sans-serif" font-size="20" text-anchor="middle">×</text>
  <rect x="160" y="50" width="80" height="80" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <text x="200" y="95" fill="#1F2937" font-family="Arial, sans-serif" font-size="20" text-anchor="middle">y</text>
  <text x="135" y="150" fill="#059669" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">Result is positive</text>
</svg>""", "Two boxes labeled x and y multiplied together. The result is positive.", "x ಮತ್ತು y ಎಂದು ಲೇಬಲ್ ಮಾಡಲಾದ ಎರಡು ಬಾಕ್ಸ್‌ಗಳನ್ನು ಗುಣಿಸಲಾಗಿದೆ. ಫಲಿತಾಂಶ ಧನಾತ್ಮಕವಾಗಿದೆ.", "If the product of integers x and y is positive, which of the following MUST be true?", "x ಮತ್ತು y ಪೂರ್ಣಾಂಕಗಳ ಗುಣಲಬ್ಧವು ಧನಾತ್ಮಕವಾಗಿದ್ದರೆ, ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಯಾವುದು ಸರಿ?", ["Both x and y are positive", "Both x and y are negative", "x and y have the same sign", "x and y are non-zero"], ["x ಮತ್ತು y ಎರಡೂ ಧನಾತ್ಮಕ", "x ಮತ್ತು y ಎರಡೂ ಋಣಾತ್ಮಕ", "x ಮತ್ತು y ಒಂದೇ ಚಿಹ್ನೆಯನ್ನು ಹೊಂದಿವೆ", "x ಮತ್ತು y ಶೂನ್ಯವಲ್ಲದ ಸಂಖ್ಯೆಗಳು"], ["x and y have the same sign", "x and y are non-zero"], ["x ಮತ್ತು y ಒಂದೇ ಚಿಹ್ನೆಯನ್ನು ಹೊಂದಿವೆ", "x ಮತ್ತು y ಶೂನ್ಯವಲ್ಲದ ಸಂಖ್ಯೆಗಳು"], "For a product to be strictly positive, neither can be zero, and they must both be positive OR both be negative (i.e., same sign).", "ಗುಣಲಬ್ಧವು ಕಟ್ಟುನಿಟ್ಟಾಗಿ ಧನಾತ್ಮಕವಾಗಿರಲು, ಯಾವುದೂ ಶೂನ್ಯವಾಗಿರಬಾರದು ಮತ್ತು ಅವೆರಡೂ ಧನಾತ್ಮಕ ಅಥವಾ ಋಣಾತ್ಮಕವಾಗಿರಬೇಕು (ಅಂದರೆ, ಒಂದೇ ಚಿಹ್ನೆ).")

add_multiple(3, "Which of the following expressions are equivalent to -24?", "ಕೆಳಗಿನ ಯಾವ ಅಭಿವ್ಯಕ್ತಿಗಳು -24 ಕ್ಕೆ ಸಮಾನವಾಗಿವೆ?", ["(-3) × 8", "4 × (-6)", "(-2) × (-3) × (-4)", "(-48) ÷ 2"], ["(-3) × 8", "4 × (-6)", "(-2) × (-3) × (-4)", "(-48) ÷ 2"], ["(-3) × 8", "4 × (-6)", "(-2) × (-3) × (-4)", "(-48) ÷ 2"], ["(-3) × 8", "4 × (-6)", "(-2) × (-3) × (-4)", "(-48) ÷ 2"], "All these expressions evaluate to -24.", "ಈ ಎಲ್ಲಾ ಅಭಿವ್ಯಕ್ತಿಗಳು -24 ನ್ನು ನೀಡುತ್ತವೆ.")

add_match(3, "Match the division statement to its quotient:", "ಭಾಗಾಕಾರದ ಹೇಳಿಕೆಯನ್ನು ಅದರ ಭಾಗಲಬ್ಧದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "(-50) ÷ 5", "right": "-10"}, {"left": "50 ÷ (-5)", "right": "-10"}, {"left": "(-50) ÷ (-5)", "right": "10"}, {"left": "0 ÷ (-50)", "right": "0"}], [{"left": "(-50) ÷ 5", "right": "-10"}, {"left": "50 ÷ (-5)", "right": "-10"}, {"left": "(-50) ÷ (-5)", "right": "10"}, {"left": "0 ÷ (-50)", "right": "0"}], "Division of integers follows the sign rules.", "ಪೂರ್ಣಾಂಕಗಳ ಭಾಗಾಕಾರವು ಚಿಹ್ನೆಯ ನಿಯಮಗಳನ್ನು ಅನುಸರಿಸುತ್ತದೆ.")

add_match(3, "Match the correct symbol to make the statement true:", "ಹೇಳಿಕೆಯನ್ನು ಸರಿಯಾಗಿಸಲು ಸರಿಯಾದ ಚಿಹ್ನೆಯನ್ನು ಹೊಂದಿಸಿ:", [{"left": "(-3) + (-6) ___ (-3) - (-6)", "right": "<"}, {"left": "(-21) - (-10) ___ (-31) + (-11)", "right": ">"}, {"left": "45 - (-11) ___ 57 + (-4)", "right": ">"}, {"left": "(-25) + 50 ___ 50 - 25", "right": "="}], [{"left": "(-3) + (-6) ___ (-3) - (-6)", "right": "<"}, {"left": "(-21) - (-10) ___ (-31) + (-11)", "right": ">"}, {"left": "45 - (-11) ___ 57 + (-4)", "right": ">"}, {"left": "(-25) + 50 ___ 50 - 25", "right": "="}], "Evaluate both sides: -9 < 3, -11 > -42, 56 > 53, 25 = 25.", "ಎರಡೂ ಬದಿಗಳನ್ನು ಮೌಲ್ಯೀಕರಿಸಿ: -9 < 3, -11 > -42, 56 > 53, 25 = 25.")

add_match(3, "Match the application problem to its answer:", "ಅನ್ವಯಿಕ ಸಮಸ್ಯೆಯನ್ನು ಅದರ ಉತ್ತರದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "Profit of ₹50 and Loss of ₹70", "right": "Net loss of ₹20 (-20)"}, {"left": "Submarine at -200m goes down 50m", "right": "-250m"}, {"left": "Temperature is -5°C, drops by 8°C", "right": "-13°C"}, {"left": "Bank balance ₹100, withdraw ₹150", "right": "-₹50 (overdrawn)"}], [{"left": "₹50 ಲಾಭ ಮತ್ತು ₹70 ನಷ್ಟ", "right": "ನಿವ್ವಳ ನಷ್ಟ ₹20 (-20)"}, {"left": "-200 ಮೀ ನಲ್ಲಿರುವ ಜಲಾಂತರ್ಗಾಮಿ 50 ಮೀ ಕೆಳಗೆ ಹೋಗುತ್ತದೆ", "right": "-250m"}, {"left": "ಉಷ್ಣಾಂಶವು -5°C ಇದೆ, 8°C ಯಷ್ಟು ಕಡಿಮೆಯಾಗುತ್ತದೆ", "right": "-13°C"}, {"left": "ಬ್ಯಾಂಕ್ ಬ್ಯಾಲೆನ್ಸ್ ₹100, ₹150 ಹಿಂಪಡೆಯಲಾಗಿದೆ", "right": "-₹50 (ಓವರ್ ಡ್ರಾನ್)"}], "These represent real-world applications of integer addition and subtraction.", "ಇವು ಪೂರ್ಣಾಂಕಗಳ ಸಂಕಲನ ಮತ್ತು ವ್ಯವಕಲನದ ನೈಜ-ಪ್ರಪಂಚದ ಅನ್ವಯಗಳನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತವೆ.")

with open('/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/maths/integers.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)
