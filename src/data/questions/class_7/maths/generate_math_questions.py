import json
import os

OUT_DIR = '/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/maths/'

def build_q(id_prefix, idx, q_type, diff, en_q, en_opts, en_ans, en_res, kn_q, kn_opts, kn_ans, kn_res, img=None):
    q = {
        "id": f"{id_prefix}{idx:03d}",
        "type": q_type,
        "difficulty": diff,
        "en": {
            "question": en_q,
            "reasoning": en_res
        },
        "kn": {
            "question": kn_q,
            "reasoning": kn_res
        }
    }
    if q_type == 'match':
        q["en"]["pairs"] = en_opts
        q["kn"]["pairs"] = kn_opts
    else:
        q["en"]["options"] = en_opts
        q["kn"]["options"] = kn_opts
        q["en"]["answer"] = en_ans
        q["kn"]["answer"] = kn_ans

    if img:
        q["image"] = img
    return q

def generate_exponents():
    qs = []
    prefix = "c7_math_exp_"
    
    # 1-15: Single
    qs.append(build_q(prefix, 1, "single", 1, "What is the base in the expression 5^3?", ["3", "5", "15", "8"], "5", "In a^n, 'a' is the base. So in 5^3, the base is 5.", "5^3 ಅಭಿವ್ಯಕ್ತಿಯಲ್ಲಿ ಆಧಾರ (base) ಯಾವುದು?", ["3", "5", "15", "8"], "5", "a^n ನಲ್ಲಿ, 'a' ಆಧಾರ. ಆದ್ದರಿಂದ 5^3 ರಲ್ಲಿ ಆಧಾರ 5 ಆಗಿದೆ."))
    qs.append(build_q(prefix, 2, "single", 1, "What is the exponent in 2^7?", ["2", "7", "14", "9"], "7", "In a^n, 'n' is the exponent.", "2^7 ರಲ್ಲಿ ಘಾತಾಂಕ (exponent) ಯಾವುದು?", ["2", "7", "14", "9"], "7", "a^n ನಲ್ಲಿ, 'n' ಘಾತಾಂಕ."))
    qs.append(build_q(prefix, 3, "single", 1, "What is the value of 2^3?", ["6", "5", "8", "9"], "8", "2^3 = 2 * 2 * 2 = 8.", "2^3 ರ ಬೆಲೆ ಎಷ್ಟು?", ["6", "5", "8", "9"], "8", "2^3 = 2 * 2 * 2 = 8."))
    qs.append(build_q(prefix, 4, "single", 1, "What is the value of 3^2?", ["6", "9", "5", "8"], "9", "3^2 = 3 * 3 = 9.", "3^2 ರ ಬೆಲೆ ಎಷ್ಟು?", ["6", "9", "5", "8"], "9", "3^2 = 3 * 3 = 9."))
    qs.append(build_q(prefix, 5, "single", 1, "Which is greater, 2^3 or 3^2?", ["2^3", "3^2", "Both are equal", "Cannot be determined"], "3^2", "2^3 = 8 and 3^2 = 9. So 3^2 is greater.", "2^3 ಅಥವಾ 3^2, ಇವುಗಳಲ್ಲಿ ಯಾವುದು ದೊಡ್ಡದು?", ["2^3", "3^2", "ಎರಡೂ ಸಮ", "ನಿರ್ಧರಿಸಲಾಗುವುದಿಲ್ಲ"], "3^2", "2^3 = 8 ಮತ್ತು 3^2 = 9. ಆದ್ದರಿಂದ 3^2 ದೊಡ್ಡದು."))
    qs.append(build_q(prefix, 6, "single", 1, "What is the value of (-1)^5?", ["1", "-1", "5", "-5"], "-1", "(-1) raised to an odd power is -1.", "(-1)^5 ರ ಬೆಲೆ ಎಷ್ಟು?", ["1", "-1", "5", "-5"], "-1", "(-1) ರ ಬೆಸ ಘಾತವು -1 ಆಗಿರುತ್ತದೆ."))
    qs.append(build_q(prefix, 7, "single", 1, "What is the value of (-1)^4?", ["1", "-1", "4", "-4"], "1", "(-1) raised to an even power is 1.", "(-1)^4 ರ ಬೆಲೆ ಎಷ್ಟು?", ["1", "-1", "4", "-4"], "1", "(-1) ರ ಸಮ ಘಾತವು 1 ಆಗಿರುತ್ತದೆ."))
    qs.append(build_q(prefix, 8, "single", 2, "Simplify: a^m * a^n", ["a^(m*n)", "a^(m+n)", "a^(m-n)", "a^(m/n)"], "a^(m+n)", "When multiplying powers with the same base, add the exponents.", "ಸಂಕ್ಷೇಪಿಸಿ: a^m * a^n", ["a^(m*n)", "a^(m+n)", "a^(m-n)", "a^(m/n)"], "a^(m+n)", "ಒಂದೇ ಆಧಾರವಿರುವ ಘಾತಗಳನ್ನು ಗುಣಿಸುವಾಗ, ಘಾತಾಂಕಗಳನ್ನು ಕೂಡಿಸಬೇಕು."))
    qs.append(build_q(prefix, 9, "single", 2, "Simplify: a^m / a^n", ["a^(m*n)", "a^(m+n)", "a^(m-n)", "a^(m/n)"], "a^(m-n)", "When dividing powers with the same base, subtract the exponents.", "ಸಂಕ್ಷೇಪಿಸಿ: a^m / a^n", ["a^(m*n)", "a^(m+n)", "a^(m-n)", "a^(m/n)"], "a^(m-n)", "ಒಂದೇ ಆಧಾರವಿರುವ ಘಾತಗಳನ್ನು ಭಾಗಿಸುವಾಗ, ಘಾತಾಂಕಗಳನ್ನು ಕಳೆಯಬೇಕು."))
    qs.append(build_q(prefix, 10, "single", 2, "Simplify: (a^m)^n", ["a^(m*n)", "a^(m+n)", "a^(m-n)", "a^(m/n)"], "a^(m*n)", "For power of a power, multiply the exponents.", "ಸಂಕ್ಷೇಪಿಸಿ: (a^m)^n", ["a^(m*n)", "a^(m+n)", "a^(m-n)", "a^(m/n)"], "a^(m*n)", "ಘಾತದ ಘಾತಕ್ಕೆ, ಘಾತಾಂಕಗಳನ್ನು ಗುಣಿಸಬೇಕು."))
    qs.append(build_q(prefix, 11, "single", 2, "What is the value of 5^0?", ["5", "0", "1", "-5"], "1", "Any non-zero number raised to the power of 0 is 1.", "5^0 ರ ಬೆಲೆ ಎಷ್ಟು?", ["5", "0", "1", "-5"], "1", "ಶೂನ್ಯವಲ್ಲದ ಯಾವುದೇ ಸಂಖ್ಯೆಯ 0 ನೇ ಘಾತವು 1 ಆಗಿರುತ್ತದೆ."))
    qs.append(build_q(prefix, 12, "single", 2, "Simplify: 2^3 * 2^2", ["2^6", "2^5", "4^5", "4^6"], "2^5", "2^3 * 2^2 = 2^(3+2) = 2^5.", "ಸಂಕ್ಷೇಪಿಸಿ: 2^3 * 2^2", ["2^6", "2^5", "4^5", "4^6"], "2^5", "2^3 * 2^2 = 2^(3+2) = 2^5."))
    qs.append(build_q(prefix, 13, "single", 3, "Express 64 as a power of 2.", ["2^4", "2^5", "2^6", "2^7"], "2^6", "64 = 2 * 2 * 2 * 2 * 2 * 2 = 2^6.", "64 ನ್ನು 2 ರ ಘಾತವಾಗಿ ಬರೆಯಿರಿ.", ["2^4", "2^5", "2^6", "2^7"], "2^6", "64 = 2 * 2 * 2 * 2 * 2 * 2 = 2^6."))
    qs.append(build_q(prefix, 14, "single", 3, "Simplify: (2^3 * 2^4) / 2^5", ["2^2", "2^3", "2^4", "2^5"], "2^2", "(2^3 * 2^4) = 2^7. Then 2^7 / 2^5 = 2^2.", "ಸಂಕ್ಷೇಪಿಸಿ: (2^3 * 2^4) / 2^5", ["2^2", "2^3", "2^4", "2^5"], "2^2", "(2^3 * 2^4) = 2^7. ನಂತರ 2^7 / 2^5 = 2^2."))
    qs.append(build_q(prefix, 15, "single", 3, "Find x if 3^x = 81", ["2", "3", "4", "5"], "4", "81 = 3 * 3 * 3 * 3 = 3^4. So x = 4.", "3^x = 81 ಆದರೆ, x ನ ಬೆಲೆ ಕಂಡುಹಿಡಿಯಿರಿ", ["2", "3", "4", "5"], "4", "81 = 3 * 3 * 3 * 3 = 3^4. ಆದ್ದರಿಂದ x = 4."))

    # 16-20: Image Single
    img16 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 200'><rect x='50' y='20' width='160' height='160' fill='#DBEAFE' stroke='#2563EB' stroke-width='2'/><text x='130' y='15' fill='#DC2626' font-family='Arial, sans-serif' font-size='14' text-anchor='middle'>3 cm</text><text x='225' y='100' fill='#DC2626' font-family='Arial, sans-serif' font-size='14' text-anchor='middle'>3 cm</text></svg>", "alt": {"en": "Square with side 3 cm", "kn": "3 ಸೆಂ.ಮೀ. ಬಾಹುವಿರುವ ಚೌಕ"}}
    qs.append(build_q(prefix, 16, "image_single", 2, "What is the area of this square expressed as a power?", ["3^1 cm²", "3^2 cm²", "3^3 cm²", "6 cm²"], "3^2 cm²", "Area of a square = side * side = 3 * 3 = 3^2.", "ಈ ಚೌಕದ ವಿಸ್ತೀರ್ಣವನ್ನು ಘಾತವಾಗಿ ಹೇಗೆ ವ್ಯಕ್ತಪಡಿಸುತ್ತೀರಿ?", ["3^1 cm²", "3^2 cm²", "3^3 cm²", "6 cm²"], "3^2 cm²", "ಚೌಕದ ವಿಸ್ತೀರ್ಣ = ಬಾಹು * ಬಾಹು = 3 * 3 = 3^2.", img16))

    img17 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 200'><rect x='60' y='60' width='100' height='100' fill='none' stroke='#2563EB' stroke-width='2'/><rect x='90' y='30' width='100' height='100' fill='none' stroke='#2563EB' stroke-width='2'/><line x1='60' y1='60' x2='90' y2='30' stroke='#2563EB' stroke-width='2'/><line x1='160' y1='60' x2='190' y2='30' stroke='#2563EB' stroke-width='2'/><line x1='60' y1='160' x2='90' y2='130' stroke='#2563EB' stroke-width='2'/><line x1='160' y1='160' x2='190' y2='130' stroke='#2563EB' stroke-width='2'/><text x='110' y='180' fill='#DC2626' font-family='Arial, sans-serif' font-size='14' text-anchor='middle'>2 cm</text></svg>", "alt": {"en": "Cube with side 2 cm", "kn": "2 ಸೆಂ.ಮೀ. ಅಂಚಿನ ಘನ"}}
    qs.append(build_q(prefix, 17, "image_single", 2, "What is the volume of this cube expressed as a power?", ["2^1 cm³", "2^2 cm³", "2^3 cm³", "2^4 cm³"], "2^3 cm³", "Volume of a cube = side * side * side = 2 * 2 * 2 = 2^3.", "ಈ ಘನದ ಗಾತ್ರವನ್ನು ಘಾತವಾಗಿ ಹೇಗೆ ವ್ಯಕ್ತಪಡಿಸುತ್ತೀರಿ?", ["2^1 cm³", "2^2 cm³", "2^3 cm³", "2^4 cm³"], "2^3 cm³", "ಘನದ ಗಾತ್ರ = ಬಾಹು * ಬಾಹು * ಬಾಹು = 2 * 2 * 2 = 2^3.", img17))

    img18 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 200'><line x1='20' y1='100' x2='280' y2='100' stroke='#2563EB' stroke-width='2'/><circle cx='50' cy='100' r='5' fill='#DC2626'/><text x='50' y='125' fill='#1F2937' font-family='Arial, sans-serif' font-size='14' text-anchor='middle'>10^1</text><circle cx='150' cy='100' r='5' fill='#DC2626'/><text x='150' y='125' fill='#1F2937' font-family='Arial, sans-serif' font-size='14' text-anchor='middle'>10^2</text><circle cx='250' cy='100' r='5' fill='#DC2626'/><text x='250' y='125' fill='#1F2937' font-family='Arial, sans-serif' font-size='14' text-anchor='middle'>10^3</text></svg>", "alt": {"en": "Number line with powers of 10", "kn": "10 ರ ಘಾತಗಳಿರುವ ಸಂಖ್ಯಾ ರೇಖೆ"}}
    qs.append(build_q(prefix, 18, "image_single", 1, "Which point on the number line represents 100?", ["10^1", "10^2", "10^3", "None"], "10^2", "10^2 = 10 * 10 = 100.", "ಸಂಖ್ಯಾ ರೇಖೆಯ ಮೇಲಿರುವ ಯಾವ ಬಿಂದು 100 ನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತದೆ?", ["10^1", "10^2", "10^3", "ಯಾವುದೂ ಅಲ್ಲ"], "10^2", "10^2 = 10 * 10 = 100.", img18))

    img19 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 200'><text x='150' y='100' fill='#059669' font-family='Arial, sans-serif' font-size='36' text-anchor='middle'>1,00,000</text></svg>", "alt": {"en": "Number 1,00,000", "kn": "ಸಂಖ್ಯೆ 1,00,000"}}
    qs.append(build_q(prefix, 19, "image_single", 2, "How is this number written as a power of 10?", ["10^3", "10^4", "10^5", "10^6"], "10^5", "1,00,000 has 5 zeros, so it is 10^5.", "ಈ ಸಂಖ್ಯೆಯನ್ನು 10 ರ ಘಾತವಾಗಿ ಹೇಗೆ ಬರೆಯಲಾಗುತ್ತದೆ?", ["10^3", "10^4", "10^5", "10^6"], "10^5", "1,00,000 ನಲ್ಲಿ 5 ಸೊನ್ನೆಗಳಿವೆ, ಆದ್ದರಿಂದ ಇದು 10^5.", img19))

    img20 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 200'><circle cx='150' cy='30' r='8' fill='#2563EB'/><line x1='150' y1='38' x2='100' y2='80' stroke='#2563EB' stroke-width='2'/><line x1='150' y1='38' x2='200' y2='80' stroke='#2563EB' stroke-width='2'/><circle cx='100' cy='88' r='8' fill='#059669'/><circle cx='200' cy='88' r='8' fill='#059669'/><line x1='100' y1='96' x2='70' y2='140' stroke='#2563EB' stroke-width='2'/><line x1='100' y1='96' x2='130' y2='140' stroke='#2563EB' stroke-width='2'/><line x1='200' y1='96' x2='170' y2='140' stroke='#2563EB' stroke-width='2'/><line x1='200' y1='96' x2='230' y2='140' stroke='#2563EB' stroke-width='2'/><circle cx='70' cy='148' r='8' fill='#DC2626'/><circle cx='130' cy='148' r='8' fill='#DC2626'/><circle cx='170' cy='148' r='8' fill='#DC2626'/><circle cx='230' cy='148' r='8' fill='#DC2626'/></svg>", "alt": {"en": "Branching diagram", "kn": "ಶಾಖೆಯ ನಕ್ಷೆ"}}
    qs.append(build_q(prefix, 20, "image_single", 3, "How many red circles are at the bottom row, expressed as a power?", ["2^1", "2^2", "2^3", "2^4"], "2^2", "There are 4 red circles. 4 = 2 * 2 = 2^2.", "ಕೆಳಗಿನ ಸಾಲಿನಲ್ಲಿರುವ ಕೆಂಪು ವೃತ್ತಗಳ ಸಂಖ್ಯೆಯನ್ನು ಘಾತವಾಗಿ ಹೇಗೆ ವ್ಯಕ್ತಪಡಿಸುತ್ತೀರಿ?", ["2^1", "2^2", "2^3", "2^4"], "2^2", "4 ಕೆಂಪು ವೃತ್ತಗಳಿವೆ. 4 = 2 * 2 = 2^2.", img20))

    # 21-25: Multiple
    qs.append(build_q(prefix, 21, "multiple", 2, "Which of the following expressions are equal to 64?", ["2^6", "4^3", "8^2", "3^4"], ["2^6", "4^3", "8^2"], "2^6=64, 4^3=64, 8^2=64. But 3^4=81.", "ಕೆಳಗಿನ ಯಾವ ಅಭಿವ್ಯಕ್ತಿಗಳು 64 ಕ್ಕೆ ಸಮನಾಗಿವೆ?", ["2^6", "4^3", "8^2", "3^4"], ["2^6", "4^3", "8^2"], "2^6=64, 4^3=64, 8^2=64. ಆದರೆ 3^4=81."))
    qs.append(build_q(prefix, 22, "multiple", 2, "Which of these evaluate to 1?", ["5^0", "100^0", "(-1)^2", "(-1)^3"], ["5^0", "100^0", "(-1)^2"], "Anything to power 0 is 1. (-1)^2 = 1. (-1)^3 = -1.", "ಇವುಗಳಲ್ಲಿ ಯಾವುದರ ಬೆಲೆ 1 ಆಗಿರುತ್ತದೆ?", ["5^0", "100^0", "(-1)^2", "(-1)^3"], ["5^0", "100^0", "(-1)^2"], "0 ನೇ ಘಾತದ ಬೆಲೆ 1. (-1)^2 = 1. (-1)^3 = -1."))
    qs.append(build_q(prefix, 23, "multiple", 3, "Which of the following are in correct standard form?", ["1.2 * 10^4", "0.5 * 10^3", "2.5 * 10^0", "34 * 10^2"], ["1.2 * 10^4", "2.5 * 10^0"], "Standard form is k * 10^n where 1 ≤ k < 10.", "ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಯಾವುದು ಸರಿಯಾದ ಪ್ರಾತಿನಿಧಿಕ ರೂಪದಲ್ಲಿದೆ (standard form)?", ["1.2 * 10^4", "0.5 * 10^3", "2.5 * 10^0", "34 * 10^2"], ["1.2 * 10^4", "2.5 * 10^0"], "ಪ್ರಾತಿನಿಧಿಕ ರೂಪ ಎಂದರೆ k * 10^n, ಇಲ್ಲಿ 1 ≤ k < 10."))
    qs.append(build_q(prefix, 24, "multiple", 3, "Select the true statements about exponents:", ["a^m * a^n = a^(m+n)", "(a^m)^n = a^(m+n)", "a^m / a^n = a^(m-n)", "a^0 = 0"], ["a^m * a^n = a^(m+n)", "a^m / a^n = a^(m-n)"], "Laws of exponents: multiplying adds exponents, dividing subtracts them.", "ಘಾತಾಂಕಗಳ ಬಗ್ಗೆ ಸರಿಯಾದ ಹೇಳಿಕೆಗಳನ್ನು ಆರಿಸಿ:", ["a^m * a^n = a^(m+n)", "(a^m)^n = a^(m+n)", "a^m / a^n = a^(m-n)", "a^0 = 0"], ["a^m * a^n = a^(m+n)", "a^m / a^n = a^(m-n)"], "ಘಾತಾಂಕಗಳ ನಿಯಮಗಳು: ಗುಣಿಸುವಾಗ ಘಾತಾಂಕಗಳನ್ನು ಕೂಡಿಸಬೇಕು, ಭಾಗಿಸುವಾಗ ಕಳೆಯಬೇಕು."))
    qs.append(build_q(prefix, 25, "multiple", 3, "Which expressions are equivalent to (2^3)^2?", ["2^6", "64", "4^3", "2^5"], ["2^6", "64", "4^3"], "(2^3)^2 = 2^6 = 64. 4^3 is also 64.", "ಯಾವ ಅಭಿವ್ಯಕ್ತಿಗಳು (2^3)^2 ಕ್ಕೆ ಸಮನಾಗಿವೆ?", ["2^6", "64", "4^3", "2^5"], ["2^6", "64", "4^3"], "(2^3)^2 = 2^6 = 64. 4^3 ಕೂಡ 64."))

    # 26-30: Match
    pairs_26_en = [{"left": "2^3", "right": "8"}, {"left": "3^2", "right": "9"}, {"left": "4^2", "right": "16"}, {"left": "5^2", "right": "25"}]
    qs.append(build_q(prefix, 26, "match", 1, "Match the exponential form to its value.", pairs_26_en, None, "Evaluated powers correctly.", "ಘಾತ ರೂಪವನ್ನು ಅದರ ಬೆಲೆಯೊಂದಿಗೆ ಹೊಂದಿಸಿ.", pairs_26_en, None, "ಘಾತಗಳ ಸರಿಯಾದ ಬೆಲೆಗಳು."))

    pairs_27_en = [{"left": "a^m * a^n", "right": "a^(m+n)"}, {"left": "a^m / a^n", "right": "a^(m-n)"}, {"left": "(a^m)^n", "right": "a^(m*n)"}, {"left": "a^0", "right": "1"}]
    qs.append(build_q(prefix, 27, "match", 2, "Match the laws of exponents.", pairs_27_en, None, "Standard rules of exponents.", "ಘಾತಾಂಕಗಳ ನಿಯಮಗಳನ್ನು ಹೊಂದಿಸಿ.", pairs_27_en, None, "ಘಾತಾಂಕಗಳ ಸಾಮಾನ್ಯ ನಿಯಮಗಳು."))

    pairs_28_en = [{"left": "1500", "right": "1.5 * 10^3"}, {"left": "150", "right": "1.5 * 10^2"}, {"left": "15000", "right": "1.5 * 10^4"}, {"left": "15", "right": "1.5 * 10^1"}]
    qs.append(build_q(prefix, 28, "match", 3, "Match numbers to their standard forms.", pairs_28_en, None, "Scientific notation correctly formats numbers.", "ಸಂಖ್ಯೆಗಳನ್ನು ಅವುಗಳ ಪ್ರಾತಿನಿಧಿಕ ರೂಪದೊಂದಿಗೆ ಹೊಂದಿಸಿ.", pairs_28_en, None, "ವೈಜ್ಞಾನಿಕ ನಮೂನೆಯು ಸಂಖ್ಯೆಗಳನ್ನು ಸರಿಯಾಗಿ ರೂಪಿಸುತ್ತದೆ."))

    pairs_29_en = [{"left": "(-1)^2", "right": "1"}, {"left": "(-1)^3", "right": "-1"}, {"left": "(-2)^2", "right": "4"}, {"left": "(-2)^3", "right": "-8"}]
    qs.append(build_q(prefix, 29, "match", 2, "Match the powers of negative bases.", pairs_29_en, None, "Even powers result in positive, odd powers in negative.", "ಋಣಾತ್ಮಕ ಆಧಾರಗಳ ಘಾತಗಳನ್ನು ಹೊಂದಿಸಿ.", pairs_29_en, None, "ಸಮ ಘಾತಗಳು ಧನಾತ್ಮಕ, ಬೆಸ ಘಾತಗಳು ಋಣಾತ್ಮಕ."))

    pairs_30_en = [{"left": "2 * 2 * 2", "right": "2^3"}, {"left": "a * a", "right": "a^2"}, {"left": "b * b * b", "right": "b^3"}, {"left": "10 * 10", "right": "10^2"}]
    qs.append(build_q(prefix, 30, "match", 1, "Match the expanded form to its power.", pairs_30_en, None, "Repeated multiplication is written as exponents.", "ವಿಸ್ತೃತ ರೂಪವನ್ನು ಅದರ ಘಾತಕ್ಕೆ ಹೊಂದಿಸಿ.", pairs_30_en, None, "ಪುನರಾವರ್ತಿತ ಗುಣಾಕಾರವನ್ನು ಘಾತಾಂಕಗಳಾಗಿ ಬರೆಯಲಾಗುತ್ತದೆ."))

    return qs

def generate_symmetry():
    qs = []
    prefix = "c7_math_symm_"
    
    qs.append(build_q(prefix, 1, "single", 1, "How many lines of symmetry does a square have?", ["2", "3", "4", "Infinite"], "4", "A square has 4 lines of symmetry.", "ಚೌಕವು ಎಷ್ಟು ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ?", ["2", "3", "4", "ಅನಂತ"], "4", "ಚೌಕವು 4 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 2, "single", 1, "How many lines of symmetry does an equilateral triangle have?", ["1", "2", "3", "0"], "3", "An equilateral triangle has 3 lines of symmetry.", "ಸಮಬಾಹು ತ್ರಿಕೋನವು ಎಷ್ಟು ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ?", ["1", "2", "3", "0"], "3", "ಸಮಬಾಹು ತ್ರಿಕೋನವು 3 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 3, "single", 1, "How many lines of symmetry does a circle have?", ["1", "2", "4", "Infinite"], "Infinite", "A circle has infinite lines of symmetry.", "ವೃತ್ತವು ಎಷ್ಟು ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ?", ["1", "2", "4", "ಅನಂತ"], "Infinite", "ವೃತ್ತವು ಅನಂತ ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 4, "single", 1, "How many lines of symmetry does the letter 'A' have?", ["0", "1", "2", "3"], "1", "The letter 'A' has 1 vertical line of symmetry.", "'A' ಅಕ್ಷರವು ಎಷ್ಟು ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ?", ["0", "1", "2", "3"], "1", "'A' ಅಕ್ಷರವು 1 ಲಂಬ ಸಮ್ಮಿತಿ ರೇಖೆಯನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 5, "single", 2, "How many lines of symmetry does the letter 'H' have?", ["0", "1", "2", "4"], "2", "The letter 'H' has 2 lines of symmetry (horizontal and vertical).", "'H' ಅಕ್ಷರವು ಎಷ್ಟು ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ?", ["0", "1", "2", "4"], "2", "'H' ಅಕ್ಷರವು 2 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ (ಅಡ್ಡ ಮತ್ತು ಲಂಬ)."))
    qs.append(build_q(prefix, 6, "single", 2, "What is the order of rotational symmetry for a square?", ["1", "2", "3", "4"], "4", "A square looks identical 4 times in a full 360° turn.", "ಚೌಕದ ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ (rotational symmetry) ಕ್ರಮಾಂಕ ಎಷ್ಟು?", ["1", "2", "3", "4"], "4", "ಚೌಕವು 360° ತಿರುಗುವಿಕೆಯಲ್ಲಿ 4 ಬಾರಿ ಒಂದೇ ರೀತಿ ಕಾಣುತ್ತದೆ."))
    qs.append(build_q(prefix, 7, "single", 2, "What is the order of rotational symmetry for an equilateral triangle?", ["1", "2", "3", "4"], "3", "An equilateral triangle has an order of rotational symmetry of 3.", "ಸಮಬಾಹು ತ್ರಿಕೋನದ ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕ ಎಷ್ಟು?", ["1", "2", "3", "4"], "3", "ಸಮಬಾಹು ತ್ರಿಕೋನವು ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕ 3 ನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 8, "single", 3, "What is the order of rotational symmetry for a circle?", ["1", "4", "Infinite", "0"], "Infinite", "A circle has infinite rotational symmetry.", "ವೃತ್ತದ ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕ ಎಷ್ಟು?", ["1", "4", "ಅನಂತ", "0"], "Infinite", "ವೃತ್ತವು ಅನಂತ ಭ್ರಮಣ ಸಮ್ಮಿತಿಯನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 9, "single", 3, "What is the order of rotational symmetry for the letter 'S'?", ["0", "1", "2", "4"], "2", "The letter 'S' looks the same upside down, so its order is 2.", "'S' ಅಕ್ಷರದ ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕ ಎಷ್ಟು?", ["0", "1", "2", "4"], "2", "'S' ಅಕ್ಷರವು ತಲೆಕೆಳಗಾಗಿದ್ದರೂ ಒಂದೇ ರೀತಿ ಕಾಣುತ್ತದೆ, ಆದ್ದರಿಂದ ಅದರ ಕ್ರಮಾಂಕ 2."))
    qs.append(build_q(prefix, 10, "single", 2, "What is the angle of rotation for a square?", ["60°", "90°", "120°", "180°"], "90°", "360° / 4 = 90°.", "ಚೌಕದ ಭ್ರಮಣ ಕೋನ ಎಷ್ಟು?", ["60°", "90°", "120°", "180°"], "90°", "360° / 4 = 90°."))
    qs.append(build_q(prefix, 11, "single", 3, "What is the angle of rotation for an equilateral triangle?", ["60°", "90°", "120°", "180°"], "120°", "360° / 3 = 120°.", "ಸಮಬಾಹು ತ್ರಿಕೋನದ ಭ್ರಮಣ ಕೋನ ಎಷ್ಟು?", ["60°", "90°", "120°", "180°"], "120°", "360° / 3 = 120°."))
    qs.append(build_q(prefix, 12, "single", 2, "How many lines of symmetry does the letter 'Z' have?", ["0", "1", "2", "3"], "0", "The letter 'Z' has no lines of symmetry.", "'Z' ಅಕ್ಷರವು ಎಷ್ಟು ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ?", ["0", "1", "2", "3"], "0", "'Z' ಅಕ್ಷರವು ಯಾವುದೇ ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿಲ್ಲ."))
    qs.append(build_q(prefix, 13, "single", 2, "How many lines of symmetry does a rhombus have?", ["1", "2", "3", "4"], "2", "A rhombus has 2 lines of symmetry (along its diagonals).", "ವಜ್ರಾಕೃತಿಯು (rhombus) ಎಷ್ಟು ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ?", ["1", "2", "3", "4"], "2", "ವಜ್ರಾಕೃತಿಯು 2 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ (ಅದರ ಕರ್ಣಗಳ ಉದ್ದಕ್ಕೂ)."))
    qs.append(build_q(prefix, 14, "single", 2, "What is the order of rotational symmetry of a rhombus?", ["1", "2", "3", "4"], "2", "A rhombus has rotational symmetry of order 2.", "ವಜ್ರಾಕೃತಿಯ ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕ ಎಷ್ಟು?", ["1", "2", "3", "4"], "2", "ವಜ್ರಾಕೃತಿಯು ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕ 2 ನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 15, "single", 2, "What is the order of rotational symmetry of a rectangle?", ["1", "2", "3", "4"], "2", "A rectangle has rotational symmetry of order 2.", "ಆಯತದ ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕ ಎಷ್ಟು?", ["1", "2", "3", "4"], "2", "ಆಯತವು ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕ 2 ನ್ನು ಹೊಂದಿದೆ."))

    img16 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 200'><rect x='50' y='50' width='200' height='100' fill='#DBEAFE' stroke='#2563EB' stroke-width='2'/><line x1='150' y1='30' x2='150' y2='170' stroke='#DC2626' stroke-width='2' stroke-dasharray='5,5'/><line x1='30' y1='100' x2='270' y2='100' stroke='#DC2626' stroke-width='2' stroke-dasharray='5,5'/></svg>", "alt": {"en": "Rectangle with two lines of symmetry", "kn": "ಎರಡು ಸಮ್ಮಿತಿ ರೇಖೆಗಳಿರುವ ಆಯತ"}}
    qs.append(build_q(prefix, 16, "image_single", 1, "How many lines of symmetry are shown in this rectangle?", ["1", "2", "3", "4"], "2", "The dashed lines show the 2 lines of symmetry.", "ಈ ಆಯತದಲ್ಲಿ ಎಷ್ಟು ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ತೋರಿಸಲಾಗಿದೆ?", ["1", "2", "3", "4"], "2", "ಚುಕ್ಕೆ-ರೇಖೆಗಳು 2 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ತೋರಿಸುತ್ತವೆ.", img16))

    img17 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 300'><path d='M150,20 L180,100 L260,100 L195,150 L220,230 L150,180 L80,230 L105,150 L40,100 L120,100 Z' fill='#DBEAFE' stroke='#2563EB' stroke-width='2'/></svg>", "alt": {"en": "Five-pointed star", "kn": "ಐದು-ತುದಿಗಳ ನಕ್ಷತ್ರ"}}
    qs.append(build_q(prefix, 17, "image_single", 3, "What is the order of rotational symmetry for this star?", ["3", "4", "5", "6"], "5", "A 5-pointed star has rotational symmetry of order 5.", "ಈ ನಕ್ಷತ್ರದ ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕ ಎಷ್ಟು?", ["3", "4", "5", "6"], "5", "5-ತುದಿಗಳ ನಕ್ಷತ್ರವು 5 ನೇ ಕ್ರಮಾಂಕದ ಭ್ರಮಣ ಸಮ್ಮಿತಿಯನ್ನು ಹೊಂದಿದೆ.", img17))

    img18 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 200'><polygon points='150,30 50,170 250,170' fill='#DBEAFE' stroke='#2563EB' stroke-width='2'/><line x1='150' y1='10' x2='150' y2='190' stroke='#DC2626' stroke-width='2' stroke-dasharray='5,5'/></svg>", "alt": {"en": "Isosceles triangle with one line of symmetry", "kn": "ಒಂದು ಸಮ್ಮಿತಿ ರೇಖೆಯಿರುವ ಸಮದ್ವಿಬಾಹು ತ್ರಿಕೋನ"}}
    qs.append(build_q(prefix, 18, "image_single", 1, "How many lines of symmetry does this isosceles triangle have?", ["1", "2", "3", "0"], "1", "An isosceles triangle has only 1 line of symmetry.", "ಈ ಸಮದ್ವಿಬಾಹು ತ್ರಿಕೋನವು ಎಷ್ಟು ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ?", ["1", "2", "3", "0"], "1", "ಸಮದ್ವಿಬಾಹು ತ್ರಿಕೋನವು ಕೇವಲ 1 ಸಮ್ಮಿತಿ ರೇಖೆಯನ್ನು ಹೊಂದಿದೆ.", img18))

    img19 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 300'><polygon points='150,30 250,80 250,180 150,230 50,180 50,80' fill='#DBEAFE' stroke='#2563EB' stroke-width='2'/></svg>", "alt": {"en": "Regular hexagon", "kn": "ನಿಯಮಿತ ಷಡ್ಭುಜಾಕೃತಿ"}}
    qs.append(build_q(prefix, 19, "image_single", 2, "How many lines of symmetry does a regular hexagon have?", ["3", "4", "5", "6"], "6", "A regular hexagon has 6 lines of symmetry.", "ನಿಯಮಿತ ಷಡ್ಭುಜಾಕೃತಿಯು ಎಷ್ಟು ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ?", ["3", "4", "5", "6"], "6", "ನಿಯಮಿತ ಷಡ್ಭುಜಾಕೃತಿಯು 6 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ.", img19))

    img20 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 300'><path d='M150,150 L200,50 L250,50 L200,150 L250,250 L200,250 L150,150 L100,250 L50,250 L100,150 L50,50 L100,50 Z' fill='#DBEAFE' stroke='#2563EB' stroke-width='2'/></svg>", "alt": {"en": "Pinwheel shape", "kn": "ಗಾಳಿಚಕ್ರದ ಆಕಾರ"}}
    qs.append(build_q(prefix, 20, "image_single", 3, "What is the order of rotational symmetry for this shape?", ["1", "2", "3", "4"], "2", "This 'X' like shape looks the same 2 times in a full turn.", "ಈ ಆಕಾರದ ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕ ಎಷ್ಟು?", ["1", "2", "3", "4"], "2", "ಈ 'X' ತರಹದ ಆಕಾರವು ಪೂರ್ಣ ತಿರುಗುವಿಕೆಯಲ್ಲಿ 2 ಬಾರಿ ಒಂದೇ ರೀತಿ ಕಾಣುತ್ತದೆ.", img20))

    qs.append(build_q(prefix, 21, "multiple", 2, "Which of these letters have exactly 2 lines of symmetry?", ["H", "I", "A", "M"], ["H", "I"], "H and I both have horizontal and vertical lines of symmetry.", "ಈ ಯಾವ ಅಕ್ಷರಗಳು ನಿಖರವಾಗಿ 2 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿವೆ?", ["H", "I", "A", "M"], ["H", "I"], "H ಮತ್ತು I ಎರಡೂ ಅಡ್ಡ ಮತ್ತು ಲಂಬ ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿವೆ."))
    qs.append(build_q(prefix, 22, "multiple", 3, "Which of these shapes have BOTH line symmetry and rotational symmetry?", ["Square", "Circle", "Rectangle", "Parallelogram"], ["Square", "Circle", "Rectangle"], "Parallelogram has rotational symmetry but no line symmetry.", "ಯಾವ ಆಕಾರಗಳು ರೇಖಾ ಸಮ್ಮಿತಿ ಮತ್ತು ಭ್ರಮಣ ಸಮ್ಮಿತಿ ಎರಡನ್ನೂ ಹೊಂದಿವೆ?", ["ಚೌಕ", "ವೃತ್ತ", "ಆಯತ", "ಸಮಾನಾಂತರ ಚತುರ್ಭುಜ"], ["ಚೌಕ", "ವೃತ್ತ", "ಆಯತ"], "ಸಮಾನಾಂತರ ಚತುರ್ಭುಜವು ಭ್ರಮಣ ಸಮ್ಮಿತಿಯನ್ನು ಹೊಂದಿದೆ ಆದರೆ ರೇಖಾ ಸಮ್ಮಿತಿ ಹೊಂದಿಲ್ಲ."))
    qs.append(build_q(prefix, 23, "multiple", 3, "Which letters have an order of rotational symmetry of 2?", ["N", "S", "Z", "A"], ["N", "S", "Z"], "N, S, and Z look the same upside down (order 2).", "ಯಾವ ಅಕ್ಷರಗಳು ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕ 2 ನ್ನು ಹೊಂದಿವೆ?", ["N", "S", "Z", "A"], ["N", "S", "Z"], "N, S, ಮತ್ತು Z ತಲೆಕೆಳಗಾಗಿದ್ದರೂ ಒಂದೇ ರೀತಿ ಕಾಣುತ್ತವೆ (ಕ್ರಮಾಂಕ 2)."))
    qs.append(build_q(prefix, 24, "multiple", 3, "Which of these shapes have NO lines of symmetry?", ["Parallelogram", "Scalene triangle", "Letter Z", "Rectangle"], ["Parallelogram", "Scalene triangle", "Letter Z"], "Parallelogram, scalene triangle, and Z have 0 lines of symmetry.", "ಯಾವ ಆಕಾರಗಳು ಯಾವುದೇ ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿಲ್ಲ?", ["ಸಮಾನಾಂತರ ಚತುರ್ಭುಜ", "ಅಸಮಬಾಹು ತ್ರಿಕೋನ", "'Z' ಅಕ್ಷರ", "ಆಯತ"], ["ಸಮಾನಾಂತರ ಚತುರ್ಭುಜ", "ಅಸಮಬಾಹು ತ್ರಿಕೋನ", "'Z' ಅಕ್ಷರ"], "ಸಮಾನಾಂತರ ಚತುರ್ಭುಜ, ಅಸಮಬಾಹು ತ್ರಿಕೋನ, ಮತ್ತು Z ಗೆ 0 ಸಮ್ಮಿತಿ ರೇಖೆಗಳಿವೆ."))
    qs.append(build_q(prefix, 25, "multiple", 2, "Select the true statements about symmetry:", ["A circle has infinite lines of symmetry.", "A square has 4 lines of symmetry.", "A rectangle has 4 lines of symmetry.", "A regular pentagon has 5 lines of symmetry."], ["A circle has infinite lines of symmetry.", "A square has 4 lines of symmetry.", "A regular pentagon has 5 lines of symmetry."], "A rectangle only has 2 lines of symmetry, not 4.", "ಸಮ್ಮಿತಿಯ ಬಗ್ಗೆ ಸರಿಯಾದ ಹೇಳಿಕೆಗಳನ್ನು ಆರಿಸಿ:", ["ವೃತ್ತವು ಅನಂತ ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ.", "ಚೌಕವು 4 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ.", "ಆಯತವು 4 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ.", "ನಿಯಮಿತ ಪಂಚಭುಜಾಕೃತಿಯು 5 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ."], ["ವೃತ್ತವು ಅನಂತ ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ.", "ಚೌಕವು 4 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ.", "ನಿಯಮಿತ ಪಂಚಭುಜಾಕೃತಿಯು 5 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ."], "ಆಯತವು ಕೇವಲ 2 ಸಮ್ಮಿತಿ ರೇಖೆಗಳನ್ನು ಹೊಂದಿದೆ, 4 ಅಲ್ಲ."))

    pairs_26_en = [{"left": "Square", "right": "4"}, {"left": "Rectangle", "right": "2"}, {"left": "Equilateral Triangle", "right": "3"}, {"left": "Isosceles Triangle", "right": "1"}]
    pairs_26_kn = [{"left": "ಚೌಕ", "right": "4"}, {"left": "ಆಯತ", "right": "2"}, {"left": "ಸಮಬಾಹು ತ್ರಿಕೋನ", "right": "3"}, {"left": "ಸಮದ್ವಿಬಾಹು ತ್ರಿಕೋನ", "right": "1"}]
    qs.append(build_q(prefix, 26, "match", 1, "Match the shape to its number of lines of symmetry.", pairs_26_en, None, "Basic shapes and their lines of symmetry.", "ಆಕಾರವನ್ನು ಅದರ ಸಮ್ಮಿತಿ ರೇಖೆಗಳ ಸಂಖ್ಯೆಯೊಂದಿಗೆ ಹೊಂದಿಸಿ.", pairs_26_kn, None, "ಮೂಲ ಆಕಾರಗಳು ಮತ್ತು ಅವುಗಳ ಸಮ್ಮಿತಿ ರೇಖೆಗಳು."))

    pairs_27_en = [{"left": "A", "right": "1"}, {"left": "H", "right": "2"}, {"left": "Z", "right": "0"}, {"left": "O", "right": "Infinite (or >2)"}]
    qs.append(build_q(prefix, 27, "match", 2, "Match the letter to its number of lines of symmetry.", pairs_27_en, None, "Alphabets and their symmetry.", "ಅಕ್ಷರವನ್ನು ಅದರ ಸಮ್ಮಿತಿ ರೇಖೆಗಳ ಸಂಖ್ಯೆಯೊಂದಿಗೆ ಹೊಂದಿಸಿ.", pairs_27_en, None, "ಅಕ್ಷರಗಳು ಮತ್ತು ಅವುಗಳ ಸಮ್ಮಿತಿ."))

    pairs_28_en = [{"left": "Square", "right": "4"}, {"left": "Hexagon", "right": "6"}, {"left": "Rhombus", "right": "2"}, {"left": "Equilateral Triangle", "right": "3"}]
    pairs_28_kn = [{"left": "ಚೌಕ", "right": "4"}, {"left": "ಷಡ್ಭುಜಾಕೃತಿ", "right": "6"}, {"left": "ವಜ್ರಾಕೃತಿ", "right": "2"}, {"left": "ಸಮಬಾಹು ತ್ರಿಕೋನ", "right": "3"}]
    qs.append(build_q(prefix, 28, "match", 3, "Match the shape to its order of rotational symmetry.", pairs_28_en, None, "Rotational symmetry depends on the regular sides.", "ಆಕಾರವನ್ನು ಅದರ ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕದೊಂದಿಗೆ ಹೊಂದಿಸಿ.", pairs_28_kn, None, "ಭ್ರಮಣ ಸಮ್ಮಿತಿಯು ನಿಯಮಿತ ಬಾಹುಗಳನ್ನು ಅವಲಂಬಿಸಿದೆ."))

    pairs_29_en = [{"left": "Square", "right": "90°"}, {"left": "Equilateral Triangle", "right": "120°"}, {"left": "Hexagon", "right": "60°"}, {"left": "Rectangle", "right": "180°"}]
    pairs_29_kn = [{"left": "ಚೌಕ", "right": "90°"}, {"left": "ಸಮಬಾಹು ತ್ರಿಕೋನ", "right": "120°"}, {"left": "ಷಡ್ಭುಜಾಕೃತಿ", "right": "60°"}, {"left": "ಆಯತ", "right": "180°"}]
    qs.append(build_q(prefix, 29, "match", 3, "Match the shape to its angle of rotation.", pairs_29_en, None, "Angle = 360° / order of rotational symmetry.", "ಆಕಾರವನ್ನು ಅದರ ಭ್ರಮಣ ಕೋನದೊಂದಿಗೆ ಹೊಂದಿಸಿ.", pairs_29_kn, None, "ಕೋನ = 360° / ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕ."))

    pairs_30_en = [{"left": "Equilateral Triangle", "right": "3"}, {"left": "Square", "right": "4"}, {"left": "Regular Pentagon", "right": "5"}, {"left": "Regular Hexagon", "right": "6"}]
    pairs_30_kn = [{"left": "ಸಮಬಾಹು ತ್ರಿಕೋನ", "right": "3"}, {"left": "ಚೌಕ", "right": "4"}, {"left": "ನಿಯಮಿತ ಪಂಚಭುಜಾಕೃತಿ", "right": "5"}, {"left": "ನಿಯಮಿತ ಷಡ್ಭುಜಾಕೃತಿ", "right": "6"}]
    qs.append(build_q(prefix, 30, "match", 2, "Match the regular polygon to its order of rotational symmetry.", pairs_30_en, None, "A regular polygon with n sides has order n.", "ನಿಯಮಿತ ಬಹುಭುಜಾಕೃತಿಯನ್ನು ಅದರ ಭ್ರಮಣ ಸಮ್ಮಿತಿಯ ಕ್ರಮಾಂಕದೊಂದಿಗೆ ಹೊಂದಿಸಿ.", pairs_30_kn, None, "n ಬಾಹುಗಳಿರುವ ನಿಯಮಿತ ಬಹುಭುಜಾಕೃತಿಯ ಕ್ರಮಾಂಕ n."))

    return qs

def generate_solid():
    qs = []
    prefix = "c7_math_solid_"
    
    qs.append(build_q(prefix, 1, "single", 1, "How many faces does a cube have?", ["4", "6", "8", "12"], "6", "A cube has 6 square faces.", "ಘನಾಕೃತಿಯು (cube) ಎಷ್ಟು ಮುಖಗಳನ್ನು ಹೊಂದಿದೆ?", ["4", "6", "8", "12"], "6", "ಘನಾಕೃತಿಯು 6 ಚೌಕಾಕಾರದ ಮುಖಗಳನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 2, "single", 1, "How many edges does a cube have?", ["6", "8", "12", "16"], "12", "A cube has 12 edges.", "ಘನಾಕೃತಿಯು ಎಷ್ಟು ಅಂಚುಗಳನ್ನು ಹೊಂದಿದೆ?", ["6", "8", "12", "16"], "12", "ಘನಾಕೃತಿಯು 12 ಅಂಚುಗಳನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 3, "single", 1, "How many vertices does a cube have?", ["6", "8", "12", "4"], "8", "A cube has 8 vertices (corners).", "ಘನಾಕೃತಿಯು ಎಷ್ಟು ಶೃಂಗಗಳನ್ನು (vertices) ಹೊಂದಿದೆ?", ["6", "8", "12", "4"], "8", "ಘನಾಕೃತಿಯು 8 ಶೃಂಗಗಳನ್ನು (ಮೂಲೆಗಳನ್ನು) ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 4, "single", 1, "How many faces does a cuboid have?", ["4", "6", "8", "12"], "6", "A cuboid has 6 rectangular faces.", "ಆಯತ ಘನಾಕೃತಿಯು (cuboid) ಎಷ್ಟು ಮುಖಗಳನ್ನು ಹೊಂದಿದೆ?", ["4", "6", "8", "12"], "6", "ಆಯತ ಘನಾಕೃತಿಯು 6 ಆಯತಾಕಾರದ ಮುಖಗಳನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 5, "single", 2, "How many vertices does a triangular pyramid have?", ["3", "4", "5", "6"], "4", "A triangular pyramid has 4 vertices.", "ತ್ರಿಕೋನ ಪಿರಮಿಡ್ ಎಷ್ಟು ಶೃಂಗಗಳನ್ನು ಹೊಂದಿದೆ?", ["3", "4", "5", "6"], "4", "ತ್ರಿಕೋನ ಪಿರಮಿಡ್ 4 ಶೃಂಗಗಳನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 6, "single", 2, "How many faces does a triangular pyramid have?", ["3", "4", "5", "6"], "4", "It has 1 base and 3 triangular side faces (total 4).", "ತ್ರಿಕೋನ ಪಿರಮಿಡ್ ಎಷ್ಟು ಮುಖಗಳನ್ನು ಹೊಂದಿದೆ?", ["3", "4", "5", "6"], "4", "ಇದು 1 ಪಾದ ಮತ್ತು 3 ತ್ರಿಕೋನ ಪಾರ್ಶ್ವ ಮುಖಗಳನ್ನು ಹೊಂದಿದೆ (ಒಟ್ಟು 4)."))
    qs.append(build_q(prefix, 7, "single", 2, "How many edges does a triangular pyramid have?", ["4", "5", "6", "8"], "6", "A triangular pyramid has 6 edges.", "ತ್ರಿಕೋನ ಪಿರಮಿಡ್ ಎಷ್ಟು ಅಂಚುಗಳನ್ನು ಹೊಂದಿದೆ?", ["4", "5", "6", "8"], "6", "ತ್ರಿಕೋನ ಪಿರಮಿಡ್ 6 ಅಂಚುಗಳನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 8, "single", 2, "How many faces does a triangular prism have?", ["3", "4", "5", "6"], "5", "It has 2 triangular bases and 3 rectangular faces.", "ತ್ರಿಕೋನ ಪಟ್ಟಕವು (prism) ಎಷ್ಟು ಮುಖಗಳನ್ನು ಹೊಂದಿದೆ?", ["3", "4", "5", "6"], "5", "ಇದು 2 ತ್ರಿಕೋನ ಪಾದಗಳನ್ನು ಮತ್ತು 3 ಆಯತಾಕಾರದ ಮುಖಗಳನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 9, "single", 3, "How many vertices does a triangular prism have?", ["4", "5", "6", "8"], "6", "A triangular prism has 6 vertices.", "ತ್ರಿಕೋನ ಪಟ್ಟಕವು ಎಷ್ಟು ಶೃಂಗಗಳನ್ನು ಹೊಂದಿದೆ?", ["4", "5", "6", "8"], "6", "ತ್ರಿಕೋನ ಪಟ್ಟಕವು 6 ಶೃಂಗಗಳನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 10, "single", 3, "How many edges does a triangular prism have?", ["6", "8", "9", "12"], "9", "A triangular prism has 9 edges.", "ತ್ರಿಕೋನ ಪಟ್ಟಕವು ಎಷ್ಟು ಅಂಚುಗಳನ್ನು ಹೊಂದಿದೆ?", ["6", "8", "9", "12"], "9", "ತ್ರಿಕೋನ ಪಟ್ಟಕವು 9 ಅಂಚುಗಳನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 11, "single", 1, "How many edges does a sphere have?", ["0", "1", "2", "Infinite"], "0", "A sphere has no edges or vertices.", "ಗೋಳವು (sphere) ಎಷ್ಟು ಅಂಚುಗಳನ್ನು ಹೊಂದಿದೆ?", ["0", "1", "2", "ಅನಂತ"], "0", "ಗೋಳವು ಯಾವುದೇ ಅಂಚುಗಳು ಅಥವಾ ಶೃಂಗಗಳನ್ನು ಹೊಂದಿಲ್ಲ."))
    qs.append(build_q(prefix, 12, "single", 1, "How many vertices does a cone have?", ["0", "1", "2", "3"], "1", "A cone has 1 vertex at the top.", "ಶಂಕುವು (cone) ಎಷ್ಟು ಶೃಂಗಗಳನ್ನು ಹೊಂದಿದೆ?", ["0", "1", "2", "3"], "1", "ಶಂಕುವು ಮೇಲ್ಭಾಗದಲ್ಲಿ 1 ಶೃಂಗವನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 13, "single", 2, "How many faces does a cylinder have?", ["1", "2", "3", "4"], "3", "A cylinder has 2 flat faces and 1 curved face.", "ಸಿಲಿಂಡರ್ ಎಷ್ಟು ಮುಖಗಳನ್ನು ಹೊಂದಿದೆ?", ["1", "2", "3", "4"], "3", "ಸಿಲಿಂಡರ್ 2 ಸಮತಟ್ಟಾದ ಮುಖಗಳನ್ನು ಮತ್ತು 1 ವಕ್ರ ಮುಖವನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 14, "single", 3, "What is Euler's formula for polyhedrons?", ["F + V = E + 2", "F + E = V + 2", "V + E = F + 2", "F + V = E - 2"], "F + V = E + 2", "Euler's formula states Faces + Vertices = Edges + 2.", "ಪಾಲಿಹೆಡ್ರಾನ್‌ಗಳಿಗಾಗಿ ಯೂಲರ್‌ನ ಸೂತ್ರ (Euler's formula) ಯಾವುದು?", ["F + V = E + 2", "F + E = V + 2", "V + E = F + 2", "F + V = E - 2"], "F + V = E + 2", "ಯೂಲರ್‌ನ ಸೂತ್ರವು ಮುಖಗಳು + ಶೃಂಗಗಳು = ಅಂಚುಗಳು + 2 ಎಂದು ಹೇಳುತ್ತದೆ."))
    qs.append(build_q(prefix, 15, "single", 3, "If a polyhedron has 5 faces and 6 vertices, how many edges does it have?", ["8", "9", "10", "11"], "9", "F+V = E+2 -> 5+6 = E+2 -> 11 = E+2 -> E=9.", "ಒಂದು ಬಹುಮುಖಿಯು 5 ಮುಖಗಳು ಮತ್ತು 6 ಶೃಂಗಗಳನ್ನು ಹೊಂದಿದ್ದರೆ, ಅದು ಎಷ್ಟು ಅಂಚುಗಳನ್ನು ಹೊಂದಿದೆ?", ["8", "9", "10", "11"], "9", "F+V = E+2 -> 5+6 = E+2 -> 11 = E+2 -> E=9."))

    img16 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 300'><rect x='50' y='100' width='100' height='100' fill='none' stroke='#2563EB' stroke-width='2'/><rect x='100' y='50' width='100' height='100' fill='none' stroke='#2563EB' stroke-width='2'/><line x1='50' y1='100' x2='100' y2='50' stroke='#2563EB' stroke-width='2'/><line x1='150' y1='100' x2='200' y2='50' stroke='#2563EB' stroke-width='2'/><line x1='50' y1='200' x2='100' y2='150' stroke='#2563EB' stroke-width='2'/><line x1='150' y1='200' x2='200' y2='150' stroke='#2563EB' stroke-width='2'/></svg>", "alt": {"en": "Cube", "kn": "ಘನಾಕೃತಿ"}}
    qs.append(build_q(prefix, 16, "image_single", 1, "How many vertices are there in this 3D shape?", ["4", "6", "8", "12"], "8", "A cube has 8 vertices.", "ಈ 3D ಆಕಾರದಲ್ಲಿ ಎಷ್ಟು ಶೃಂಗಗಳಿವೆ?", ["4", "6", "8", "12"], "8", "ಘನಾಕೃತಿಯು 8 ಶೃಂಗಗಳನ್ನು ಹೊಂದಿದೆ.", img16))

    img17 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 200'><rect x='50' y='80' width='150' height='80' fill='none' stroke='#2563EB' stroke-width='2'/><rect x='80' y='40' width='150' height='80' fill='none' stroke='#2563EB' stroke-width='2'/><line x1='50' y1='80' x2='80' y2='40' stroke='#2563EB' stroke-width='2'/><line x1='200' y1='80' x2='230' y2='40' stroke='#2563EB' stroke-width='2'/><line x1='50' y1='160' x2='80' y2='120' stroke='#2563EB' stroke-width='2'/><line x1='200' y1='160' x2='230' y2='120' stroke='#2563EB' stroke-width='2'/></svg>", "alt": {"en": "Cuboid", "kn": "ಆಯತ ಘನಾಕೃತಿ"}}
    qs.append(build_q(prefix, 17, "image_single", 2, "How many edges does this shape have?", ["8", "10", "12", "16"], "12", "A cuboid has 12 edges.", "ಈ ಆಕಾರವು ಎಷ್ಟು ಅಂಚುಗಳನ್ನು ಹೊಂದಿದೆ?", ["8", "10", "12", "16"], "12", "ಆಯತ ಘನಾಕೃತಿಯು 12 ಅಂಚುಗಳನ್ನು ಹೊಂದಿದೆ.", img17))

    img18 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 300'><polygon points='150,50 80,200 220,200' fill='none' stroke='#2563EB' stroke-width='2'/><line x1='150' y1='50' x2='150' y2='200' stroke='#2563EB' stroke-width='2'/><polygon points='80,200 220,200 150,230' fill='none' stroke='#2563EB' stroke-width='2'/></svg>", "alt": {"en": "Pyramid", "kn": "ಪಿರಮಿಡ್"}}
    qs.append(build_q(prefix, 18, "image_single", 2, "If the base of this pyramid is a square, how many total faces does it have?", ["4", "5", "6", "8"], "5", "1 square base + 4 triangular sides = 5 faces.", "ಈ ಪಿರಮಿಡ್‌ನ ಪಾದವು ಚೌಕಾಕಾರವಾಗಿದ್ದರೆ, ಅದು ಒಟ್ಟು ಎಷ್ಟು ಮುಖಗಳನ್ನು ಹೊಂದಿದೆ?", ["4", "5", "6", "8"], "5", "1 ಚೌಕಾಕಾರದ ಪಾದ + 4 ತ್ರಿಕೋನ ಪಾರ್ಶ್ವಗಳು = 5 ಮುಖಗಳು.", img18))

    img19 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 300'><rect x='100' y='50' width='50' height='50' fill='none' stroke='#2563EB' stroke-width='2'/><rect x='100' y='100' width='50' height='50' fill='none' stroke='#2563EB' stroke-width='2'/><rect x='100' y='150' width='50' height='50' fill='none' stroke='#2563EB' stroke-width='2'/><rect x='100' y='200' width='50' height='50' fill='none' stroke='#2563EB' stroke-width='2'/><rect x='50' y='100' width='50' height='50' fill='none' stroke='#2563EB' stroke-width='2'/><rect x='150' y='100' width='50' height='50' fill='none' stroke='#2563EB' stroke-width='2'/></svg>", "alt": {"en": "Net of a cube", "kn": "ಘನಾಕೃತಿಯ ಜಾಲ"}}
    qs.append(build_q(prefix, 19, "image_single", 2, "Which 3D shape does this net form when folded?", ["Cuboid", "Cube", "Square Pyramid", "Prism"], "Cube", "A net of 6 identical squares forms a cube.", "ಈ ಜಾಲವನ್ನು ಮಡಿಸಿದಾಗ ಯಾವ 3D ಆಕಾರ ರೂಪುಗೊಳ್ಳುತ್ತದೆ?", ["ಆಯತ ಘನಾಕೃತಿ", "ಘನಾಕೃತಿ", "ಚೌಕ ಪಿರಮಿಡ್", "ಪಟ್ಟಕ"], "ಘನಾಕೃತಿ", "6 ಒಂದೇ ರೀತಿಯ ಚೌಕಗಳ ಜಾಲವು ಘನಾಕೃತಿಯನ್ನು ರೂಪಿಸುತ್ತದೆ.", img19))

    img20 = {"type": "svg", "svg": "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 300'><rect x='100' y='100' width='100' height='100' fill='none' stroke='#2563EB' stroke-width='2'/><circle cx='150' cy='60' r='40' fill='none' stroke='#2563EB' stroke-width='2'/><circle cx='150' cy='240' r='40' fill='none' stroke='#2563EB' stroke-width='2'/></svg>", "alt": {"en": "Net of a cylinder", "kn": "ಸಿಲಿಂಡರ್‌ನ ಜಾಲ"}}
    qs.append(build_q(prefix, 20, "image_single", 2, "Which 3D shape does this net form when folded?", ["Cone", "Sphere", "Cylinder", "Prism"], "Cylinder", "A rectangle and two circles form a cylinder.", "ಈ ಜಾಲವನ್ನು ಮಡಿಸಿದಾಗ ಯಾವ 3D ಆಕಾರ ರೂಪುಗೊಳ್ಳುತ್ತದೆ?", ["ಶಂಕು", "ಗೋಳ", "ಸಿಲಿಂಡರ್", "ಪಟ್ಟಕ"], "ಸಿಲಿಂಡರ್", "ಒಂದು ಆಯತ ಮತ್ತು ಎರಡು ವೃತ್ತಗಳು ಸಿಲಿಂಡರ್ ಅನ್ನು ರೂಪಿಸುತ್ತವೆ.", img20))

    qs.append(build_q(prefix, 21, "multiple", 2, "Which of the following are polyhedrons?", ["Cube", "Prism", "Pyramid", "Sphere"], ["Cube", "Prism", "Pyramid"], "A sphere has curved surfaces, so it is not a polyhedron.", "ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಯಾವುದು ಪಾಲಿಹೆಡ್ರಾನ್‌ಗಳು (ಬಹುಮುಖಿಗಳು)?", ["ಘನಾಕೃತಿ", "ಪಟ್ಟಕ", "ಪಿರಮಿಡ್", "ಗೋಳ"], ["ಘನಾಕೃತಿ", "ಪಟ್ಟಕ", "ಪಿರಮಿಡ್"], "ಗೋಳವು ವಕ್ರ ಮೇಲ್ಮೈಗಳನ್ನು ಹೊಂದಿದೆ, ಆದ್ದರಿಂದ ಇದು ಬಹುಮುಖಿಯಲ್ಲ."))
    qs.append(build_q(prefix, 22, "multiple", 3, "Which of these 3D shapes have exactly 6 faces?", ["Cube", "Cuboid", "Hexagonal pyramid", "Triangular prism"], ["Cube", "Cuboid"], "A cube and a cuboid both have 6 faces. A hexagonal pyramid has 7 faces.", "ಯಾವ 3D ಆಕಾರಗಳು ನಿಖರವಾಗಿ 6 ಮುಖಗಳನ್ನು ಹೊಂದಿವೆ?", ["ಘನಾಕೃತಿ", "ಆಯತ ಘನಾಕೃತಿ", "ಷಡ್ಭುಜಾಕೃತಿಯ ಪಿರಮಿಡ್", "ತ್ರಿಕೋನ ಪಟ್ಟಕ"], ["ಘನಾಕೃತಿ", "ಆಯತ ಘನಾಕೃತಿ"], "ಘನಾಕೃತಿ ಮತ್ತು ಆಯತ ಘನಾಕೃತಿ ಎರಡೂ 6 ಮುಖಗಳನ್ನು ಹೊಂದಿವೆ."))
    qs.append(build_q(prefix, 23, "multiple", 1, "Which of these are 2D shapes?", ["Square", "Circle", "Rectangle", "Cube"], ["Square", "Circle", "Rectangle"], "A cube is a 3D shape.", "ಇವುಗಳಲ್ಲಿ ಯಾವುದು 2D (ದ್ವಿ-ಆಯಾಮದ) ಆಕಾರಗಳು?", ["ಚೌಕ", "ವೃತ್ತ", "ಆಯತ", "ಘನಾಕೃತಿ"], ["ಚೌಕ", "ವೃತ್ತ", "ಆಯತ"], "ಘನಾಕೃತಿಯು 3D ಆಕಾರವಾಗಿದೆ."))
    qs.append(build_q(prefix, 24, "multiple", 2, "Which of these 3D shapes have curved surfaces?", ["Cylinder", "Cone", "Sphere", "Cube"], ["Cylinder", "Cone", "Sphere"], "A cube only has flat surfaces.", "ಯಾವ 3D ಆಕಾರಗಳು ವಕ್ರ ಮೇಲ್ಮೈಗಳನ್ನು ಹೊಂದಿವೆ?", ["ಸಿಲಿಂಡರ್", "ಶಂಕು", "ಗೋಳ", "ಘನಾಕೃತಿ"], ["ಸಿಲಿಂಡರ್", "ಶಂಕು", "ಗೋಳ"], "ಘನಾಕೃತಿಯು ಕೇವಲ ಸಮತಟ್ಟಾದ ಮೇಲ್ಮೈಗಳನ್ನು ಹೊಂದಿದೆ."))
    qs.append(build_q(prefix, 25, "multiple", 3, "Select the true statements about Euler's formula:", ["It applies to polyhedrons.", "F + V = E + 2", "V + E = F + 2", "A cube satisfies this formula (6+8=12+2)."], ["It applies to polyhedrons.", "F + V = E + 2", "A cube satisfies this formula (6+8=12+2)."], "Euler's formula is F + V = E + 2.", "ಯೂಲರ್‌ನ ಸೂತ್ರದ ಬಗ್ಗೆ ಸರಿಯಾದ ಹೇಳಿಕೆಗಳನ್ನು ಆರಿಸಿ:", ["ಇದು ಪಾಲಿಹೆಡ್ರಾನ್‌ಗಳಿಗೆ ಅನ್ವಯಿಸುತ್ತದೆ.", "F + V = E + 2", "V + E = F + 2", "ಘನಾಕೃತಿಯು ಈ ಸೂತ್ರವನ್ನು ಪೂರೈಸುತ್ತದೆ (6+8=12+2)."], ["ಇದು ಪಾಲಿಹೆಡ್ರಾನ್‌ಗಳಿಗೆ ಅನ್ವಯಿಸುತ್ತದೆ.", "F + V = E + 2", "ಘನಾಕೃತಿಯು ಈ ಸೂತ್ರವನ್ನು ಪೂರೈಸುತ್ತದೆ (6+8=12+2)."], "ಯೂಲರ್‌ನ ಸೂತ್ರವು F + V = E + 2 ಆಗಿದೆ."))

    pairs_26_en = [{"left": "Cube", "right": "6 Faces"}, {"left": "Triangular Pyramid", "right": "4 Faces"}, {"left": "Square Pyramid", "right": "5 Faces"}, {"left": "Triangular Prism", "right": "5 Faces"}]
    pairs_26_kn = [{"left": "ಘನಾಕೃತಿ", "right": "6 ಮುಖಗಳು"}, {"left": "ತ್ರಿಕೋನ ಪಿರಮಿಡ್", "right": "4 ಮುಖಗಳು"}, {"left": "ಚೌಕ ಪಿರಮಿಡ್", "right": "5 ಮುಖಗಳು"}, {"left": "ತ್ರಿಕೋನ ಪಟ್ಟಕ", "right": "5 ಮುಖಗಳು"}]
    qs.append(build_q(prefix, 26, "match", 1, "Match the shape to its number of faces.", pairs_26_en, None, "Properties of 3D shapes.", "ಆಕಾರವನ್ನು ಅದರ ಮುಖಗಳ ಸಂಖ್ಯೆಯೊಂದಿಗೆ ಹೊಂದಿಸಿ.", pairs_26_kn, None, "3D ಆಕಾರಗಳ ಗುಣಲಕ್ಷಣಗಳು."))

    pairs_27_en = [{"left": "Cube", "right": "12 Edges"}, {"left": "Triangular Pyramid", "right": "6 Edges"}, {"left": "Square Pyramid", "right": "8 Edges"}, {"left": "Triangular Prism", "right": "9 Edges"}]
    pairs_27_kn = [{"left": "ಘನಾಕೃತಿ", "right": "12 ಅಂಚುಗಳು"}, {"left": "ತ್ರಿಕೋನ ಪಿರಮಿಡ್", "right": "6 ಅಂಚುಗಳು"}, {"left": "ಚೌಕ ಪಿರಮಿಡ್", "right": "8 ಅಂಚುಗಳು"}, {"left": "ತ್ರಿಕೋನ ಪಟ್ಟಕ", "right": "9 ಅಂಚುಗಳು"}]
    qs.append(build_q(prefix, 27, "match", 2, "Match the shape to its number of edges.", pairs_27_en, None, "Properties of 3D shapes.", "ಆಕಾರವನ್ನು ಅದರ ಅಂಚುಗಳ ಸಂಖ್ಯೆಯೊಂದಿಗೆ ಹೊಂದಿಸಿ.", pairs_27_kn, None, "3D ಆಕಾರಗಳ ಗುಣಲಕ್ಷಣಗಳು."))

    pairs_28_en = [{"left": "Cube", "right": "8 Vertices"}, {"left": "Triangular Pyramid", "right": "4 Vertices"}, {"left": "Square Pyramid", "right": "5 Vertices"}, {"left": "Triangular Prism", "right": "6 Vertices"}]
    pairs_28_kn = [{"left": "ಘನಾಕೃತಿ", "right": "8 ಶೃಂಗಗಳು"}, {"left": "ತ್ರಿಕೋನ ಪಿರಮಿಡ್", "right": "4 ಶೃಂಗಗಳು"}, {"left": "ಚೌಕ ಪಿರಮಿಡ್", "right": "5 ಶೃಂಗಗಳು"}, {"left": "ತ್ರಿಕೋನ ಪಟ್ಟಕ", "right": "6 ಶೃಂಗಗಳು"}]
    qs.append(build_q(prefix, 28, "match", 2, "Match the shape to its number of vertices.", pairs_28_en, None, "Properties of 3D shapes.", "ಆಕಾರವನ್ನು ಅದರ ಶೃಂಗಗಳ ಸಂಖ್ಯೆಯೊಂದಿಗೆ ಹೊಂದಿಸಿ.", pairs_28_kn, None, "3D ಆಕಾರಗಳ ಗುಣಲಕ್ಷಣಗಳು."))

    pairs_29_en = [{"left": "Square", "right": "Cube"}, {"left": "Rectangle", "right": "Cuboid"}, {"left": "Circle", "right": "Sphere"}, {"left": "Triangle", "right": "Pyramid (Faces)"}]
    pairs_29_kn = [{"left": "ಚೌಕ", "right": "ಘನಾಕೃತಿ"}, {"left": "ಆಯತ", "right": "ಆಯತ ಘನಾಕೃತಿ"}, {"left": "ವೃತ್ತ", "right": "ಗೋಳ"}, {"left": "ತ್ರಿಕೋನ", "right": "ಪಿರಮಿಡ್ (ಮುಖಗಳು)"}]
    qs.append(build_q(prefix, 29, "match", 1, "Match the 2D shape to the 3D shape related to it.", pairs_29_en, None, "Base 2D shape that forms the 3D shape.", "2D ಆಕಾರವನ್ನು ಅದಕ್ಕೆ ಸಂಬಂಧಿಸಿದ 3D ಆಕಾರದೊಂದಿಗೆ ಹೊಂದಿಸಿ.", pairs_29_kn, None, "3D ಆಕಾರವನ್ನು ರೂಪಿಸುವ ಮೂಲ 2D ಆಕಾರ."))

    pairs_30_en = [{"left": "F=4, V=4", "right": "E=6"}, {"left": "F=6, V=8", "right": "E=12"}, {"left": "F=5, V=5", "right": "E=8"}, {"left": "F=5, V=6", "right": "E=9"}]
    qs.append(build_q(prefix, 30, "match", 3, "Match the values using Euler's Formula (F+V = E+2).", pairs_30_en, None, "Calculation using Euler's formula.", "ಯೂಲರ್‌ನ ಸೂತ್ರವನ್ನು ಬಳಸಿ ಮೌಲ್ಯಗಳನ್ನು ಹೊಂದಿಸಿ (F+V = E+2).", pairs_30_en, None, "ಯೂಲರ್‌ನ ಸೂತ್ರವನ್ನು ಬಳಸಿದ ಲೆಕ್ಕಾಚಾರ."))

    return qs

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, 'exponents_powers.json'), 'w', encoding='utf-8') as f:
        json.dump(generate_exponents(), f, indent=2, ensure_ascii=False)
    with open(os.path.join(OUT_DIR, 'symmetry.json'), 'w', encoding='utf-8') as f:
        json.dump(generate_symmetry(), f, indent=2, ensure_ascii=False)
    with open(os.path.join(OUT_DIR, 'solid_shapes.json'), 'w', encoding='utf-8') as f:
        json.dump(generate_solid(), f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()
