import json

questions = []
q = 1

def add_single(diff, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_frac_{q:03d}", "type": "single", "difficulty": diff,
        "en": {"question": en_q, "options": en_opts, "answer": en_ans, "reasoning": en_reas},
        "kn": {"question": kn_q, "options": kn_opts, "answer": kn_ans, "reasoning": kn_reas}
    })
    q += 1

def add_multiple(diff, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_frac_{q:03d}", "type": "multiple", "difficulty": diff,
        "en": {"question": en_q, "options": en_opts, "answer": en_ans, "reasoning": en_reas},
        "kn": {"question": kn_q, "options": kn_opts, "answer": kn_ans, "reasoning": kn_reas}
    })
    q += 1

def add_match(diff, en_q, kn_q, en_pairs, kn_pairs, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_frac_{q:03d}", "type": "match", "difficulty": diff,
        "en": {"question": en_q, "pairs": en_pairs, "reasoning": en_reas},
        "kn": {"question": kn_q, "pairs": kn_pairs, "reasoning": kn_reas}
    })
    q += 1

def add_img_s(diff, svg, en_alt, kn_alt, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_frac_{q:03d}", "type": "image_single", "difficulty": diff,
        "image": {"type": "svg", "svg": svg.strip(), "alt": {"en": en_alt, "kn": kn_alt}},
        "en": {"question": en_q, "options": en_opts, "answer": en_ans, "reasoning": en_reas},
        "kn": {"question": kn_q, "options": kn_opts, "answer": kn_ans, "reasoning": kn_reas}
    })
    q += 1

def add_img_m(diff, svg, en_alt, kn_alt, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_frac_{q:03d}", "type": "image_multiple", "difficulty": diff,
        "image": {"type": "svg", "svg": svg.strip(), "alt": {"en": en_alt, "kn": kn_alt}},
        "en": {"question": en_q, "options": en_opts, "answer": en_ans, "reasoning": en_reas},
        "kn": {"question": kn_q, "options": kn_opts, "answer": kn_ans, "reasoning": kn_reas}
    })
    q += 1

# Easy (10)
add_single(1, "What is 1/2 of 24?", "24 ರ 1/2 ಎಷ್ಟು?", ["12", "6", "48", "2"], ["12", "6", "48", "2"], "12", "12", "1/2 × 24 = 12.", "1/2 × 24 = 12.")
add_single(1, "Convert 0.75 to a fraction in its simplest form.", "0.75 ನ್ನು ಅದರ ಸರಳ ರೂಪದ ಭಿನ್ನರಾಶಿಗೆ ಪರಿವರ್ತಿಸಿ.", ["3/4", "1/2", "7/5", "1/4"], ["3/4", "1/2", "7/5", "1/4"], "3/4", "3/4", "0.75 = 75/100. Dividing numerator and denominator by 25 gives 3/4.", "0.75 = 75/100. ಅಂಶ ಮತ್ತು ಛೇದವನ್ನು 25 ರಿಂದ ಭಾಗಿಸಿದಾಗ 3/4 ಸಿಗುತ್ತದೆ.")
add_single(1, "Multiply 2.5 by 10.", "2.5 ನ್ನು 10 ರಿಂದ ಗುಣಿಸಿ.", ["25", "0.25", "250", "2.50"], ["25", "0.25", "250", "2.50"], "25", "25", "When multiplying by 10, the decimal point moves one place to the right.", "10 ರಿಂದ ಗುಣಿಸಿದಾಗ, ದಶಮಾಂಶ ಬಿಂದುವು ಒಂದು ಸ್ಥಾನ ಬಲಕ್ಕೆ ಚಲಿಸುತ್ತದೆ.")
add_single(1, "Which is greater: 0.5 or 0.05?", "ಯಾವುದು ದೊಡ್ಡದು: 0.5 ಅಥವಾ 0.05?", ["0.5", "0.05", "Both are equal", "Cannot be determined"], ["0.5", "0.05", "ಎರಡೂ ಸಮ", "ನಿರ್ಧರಿಸಲಾಗುವುದಿಲ್ಲ"], "0.5", "0.5", "0.5 has 5 in the tenths place, while 0.05 has 0 in the tenths place.", "0.5 ಹತ್ತನೇ ಸ್ಥಾನದಲ್ಲಿ 5 ನ್ನು ಹೊಂದಿದೆ, ಆದರೆ 0.05 ಹತ್ತನೇ ಸ್ಥಾನದಲ್ಲಿ 0 ನ್ನು ಹೊಂದಿದೆ.")
add_single(1, "What is 3/5 + 1/5?", "3/5 + 1/5 ಎಷ್ಟು?", ["4/5", "4/10", "2/5", "3/25"], ["4/5", "4/10", "2/5", "3/25"], "4/5", "4/5", "Since denominators are the same, just add the numerators: 3 + 1 = 4.", "ಛೇದಗಳು ಸಮಾನವಾಗಿರುವುದರಿಂದ, ಅಂಶಗಳನ್ನು ಸೇರಿಸಿ: 3 + 1 = 4.")
add_single(1, "Find the reciprocal of 7/9.", "7/9 ರ ವ್ಯುತ್ಕ್ರಮವನ್ನು (reciprocal) ಕಂಡುಹಿಡಿಯಿರಿ.", ["9/7", "7/9", "-7/9", "1/7"], ["9/7", "7/9", "-7/9", "1/7"], "9/7", "9/7", "The reciprocal is found by swapping the numerator and the denominator.", "ಅಂಶ ಮತ್ತು ಛೇದವನ್ನು ಬದಲಾಯಿಸುವ ಮೂಲಕ ವ್ಯುತ್ಕ್ರಮವನ್ನು ಕಂಡುಹಿಡಿಯಲಾಗುತ್ತದೆ.")

add_img_s(1, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <circle cx="150" cy="100" r="80" fill="white" stroke="#2563EB" stroke-width="2"/>
  <path d="M150,100 L150,20 A80,80 0 0,1 230,100 Z" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <line x1="70" y1="100" x2="230" y2="100" stroke="#2563EB" stroke-width="2"/>
  <line x1="150" y1="20" x2="150" y2="180" stroke="#2563EB" stroke-width="2"/>
</svg>""", "A circle divided into 4 equal parts, with 1 part shaded.", "4 ಸಮಾನ ಭಾಗಗಳಾಗಿ ವಿಂಗಡಿಸಲಾದ ವೃತ್ತ, ಇದರಲ್ಲಿ 1 ಭಾಗವನ್ನು ಛಾಯೆಗೊಳಿಸಲಾಗಿದೆ.", "What fraction of the circle is shaded?", "ವೃತ್ತದ ಎಷ್ಟು ಭಾಗ ಛಾಯೆಗೊಳಿಸಲಾಗಿದೆ?", ["1/4", "1/2", "3/4", "1/3"], ["1/4", "1/2", "3/4", "1/3"], "1/4", "1/4", "The circle is divided into 4 equal quadrants, and 1 is shaded.", "ವೃತ್ತವನ್ನು 4 ಸಮಾನ ಚತುರ್ಭಾಗಗಳಾಗಿ ವಿಂಗಡಿಸಲಾಗಿದೆ, ಮತ್ತು 1 ಭಾಗ ಛಾಯೆಗೊಳಿಸಲಾಗಿದೆ.")

add_img_s(1, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 100">
  <rect x="20" y="30" width="200" height="40" fill="white" stroke="#2563EB" stroke-width="2"/>
  <rect x="20" y="30" width="120" height="40" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <line x1="60" y1="30" x2="60" y2="70" stroke="#2563EB" stroke-width="2"/>
  <line x1="100" y1="30" x2="100" y2="70" stroke="#2563EB" stroke-width="2"/>
  <line x1="140" y1="30" x2="140" y2="70" stroke="#2563EB" stroke-width="2"/>
  <line x1="180" y1="30" x2="180" y2="70" stroke="#2563EB" stroke-width="2"/>
</svg>""", "A rectangle divided into 5 equal parts, with 3 parts shaded.", "5 ಸಮಾನ ಭಾಗಗಳಾಗಿ ವಿಂಗಡಿಸಲಾದ ಆಯತ, 3 ಭಾಗಗಳನ್ನು ಛಾಯೆಗೊಳಿಸಲಾಗಿದೆ.", "Which decimal represents the shaded portion of the rectangle?", "ಆಯತದ ಛಾಯೆಗೊಳಿಸಿದ ಭಾಗವನ್ನು ಯಾವ ದಶಮಾಂಶ ಪ್ರತಿನಿಧಿಸುತ್ತದೆ?", ["0.6", "0.4", "0.3", "0.5"], ["0.6", "0.4", "0.3", "0.5"], "0.6", "0.6", "3 out of 5 parts are shaded, which is 3/5. 3/5 = 6/10 = 0.6.", "5 ರಲ್ಲಿ 3 ಭಾಗಗಳು ಛಾಯೆಗೊಳಿಸಲ್ಪಟ್ಟಿವೆ, ಅಂದರೆ 3/5. 3/5 = 6/10 = 0.6.")

add_multiple(1, "Which of the following fractions are equivalent to 1/2?", "ಕೆಳಗಿನ ಯಾವ ಭಿನ್ನರಾಶಿಗಳು 1/2 ಕ್ಕೆ ಸಮಾನವಾಗಿವೆ?", ["2/4", "3/6", "4/8", "5/12"], ["2/4", "3/6", "4/8", "5/12"], ["2/4", "3/6", "4/8"], ["2/4", "3/6", "4/8"], "2/4, 3/6, and 4/8 all simplify to 1/2. 5/12 does not.", "2/4, 3/6 ಮತ್ತು 4/8 ಎಲ್ಲವನ್ನೂ ಸರಳೀಕರಿಸಿದಾಗ 1/2 ಆಗುತ್ತದೆ. 5/12 ಆಗುವುದಿಲ್ಲ.")

add_match(1, "Match the decimal operation with its result:", "ದಶಮಾಂಶದ ಲೆಕ್ಕವನ್ನು ಅದರ ಫಲಿತಾಂಶದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "2.5 × 10", "right": "25"}, {"left": "2.5 ÷ 10", "right": "0.25"}, {"left": "0.25 × 100", "right": "25"}, {"left": "250 ÷ 100", "right": "2.5"}], [{"left": "2.5 × 10", "right": "25"}, {"left": "2.5 ÷ 10", "right": "0.25"}, {"left": "0.25 × 100", "right": "25"}, {"left": "250 ÷ 100", "right": "2.5"}], "Multiplication shifts the decimal right; division shifts it left.", "ಗುಣಾಕಾರವು ದಶಮಾಂಶವನ್ನು ಬಲಕ್ಕೆ ಬದಲಾಯಿಸುತ್ತದೆ; ಭಾಗಾಕಾರವು ಅದನ್ನು ಎಡಕ್ಕೆ ಬದಲಾಯಿಸುತ್ತದೆ.")


# Medium (10)
add_single(2, "Find the value of 2/3 × 3 1/2.", "2/3 × 3 1/2 ರ ಮೌಲ್ಯವನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.", ["7/3", "14/6", "7/2", "3/2"], ["7/3", "14/6", "7/2", "3/2"], "7/3", "7/3", "First convert mixed number to improper fraction: 3 1/2 = 7/2. Then (2/3) × (7/2) = 14/6 = 7/3.", "ಮಿಶ್ರ ಭಿನ್ನರಾಶಿಯನ್ನು ವಿಷಮ ಭಿನ್ನರಾಶಿಗೆ ಪರಿವರ್ತಿಸಿ: 3 1/2 = 7/2. ನಂತರ (2/3) × (7/2) = 14/6 = 7/3.")
add_single(2, "Calculate: 1.05 × 1.2", "ಲೆಕ್ಕ ಹಾಕಿ: 1.05 × 1.2", ["1.26", "12.6", "1.260", "0.126"], ["1.26", "12.6", "1.260", "0.126"], "1.26", "1.26", "105 × 12 = 1260. Total decimal places = 2 + 1 = 3. So, 1.260 or 1.26.", "105 × 12 = 1260. ಒಟ್ಟು ದಶಮಾಂಶ ಸ್ಥಾನಗಳು = 2 + 1 = 3. ಆದ್ದರಿಂದ, 1.260 ಅಥವಾ 1.26.")
add_single(2, "Divide 7/8 by 1/4.", "7/8 ನ್ನು 1/4 ರಿಂದ ಭಾಗಿಸಿ.", ["7/2", "7/32", "2/7", "14/4"], ["7/2", "7/32", "2/7", "14/4"], "7/2", "7/2", "Dividing by a fraction is multiplying by its reciprocal: 7/8 × 4/1 = 28/8 = 7/2.", "ಭಿನ್ನರಾಶಿಯಿಂದ ಭಾಗಿಸುವುದು ಅದರ ವ್ಯುತ್ಕ್ರಮದಿಂದ ಗುಣಿಸುವುದಾಗಿದೆ: 7/8 × 4/1 = 28/8 = 7/2.")
add_single(2, "A car covers a distance of 89.1 km in 2.2 hours. What is the average distance covered by it in 1 hour?", "ಒಂದು ಕಾರು 2.2 ಗಂಟೆಗಳಲ್ಲಿ 89.1 ಕಿ.ಮೀ ದೂರವನ್ನು ಕ್ರಮಿಸುತ್ತದೆ. 1 ಗಂಟೆಯಲ್ಲಿ ಅದು ಕ್ರಮಿಸಿದ ಸರಾಸರಿ ದೂರ ಎಷ್ಟು?", ["40.5 km", "40.05 km", "41.5 km", "45 km"], ["40.5 ಕಿ.ಮೀ", "40.05 ಕಿ.ಮೀ", "41.5 ಕಿ.ಮೀ", "45 ಕಿ.ಮೀ"], "40.5 km", "40.5 ಕಿ.ಮೀ", "Distance = 89.1 / 2.2 = 891 / 22 = 40.5 km.", "ದೂರ = 89.1 / 2.2 = 891 / 22 = 40.5 ಕಿ.ಮೀ.")
add_single(2, "Which of the following is equivalent to (3/4) of 16?", "ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಯಾವುದು 16 ರ (3/4) ಭಾಗಕ್ಕೆ ಸಮನಾಗಿದೆ?", ["12", "8", "24", "4"], ["12", "8", "24", "4"], "12", "12", "3/4 × 16 = 3 × 4 = 12.", "3/4 × 16 = 3 × 4 = 12.")

add_img_s(2, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <rect x="50" y="50" width="100" height="100" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <rect x="150" y="50" width="100" height="100" fill="white" stroke="#2563EB" stroke-width="2"/>
  <line x1="50" y1="100" x2="150" y2="100" stroke="#2563EB" stroke-width="2"/>
  <rect x="50" y="50" width="100" height="50" fill="#059669" stroke="#2563EB" stroke-width="2"/>
</svg>""", "Two large squares representing 1 whole each. The first square is completely shaded, except half of it is double-shaded green.", "1 ಪೂರ್ಣವನ್ನು ಪ್ರತಿನಿಧಿಸುವ ಎರಡು ದೊಡ್ಡ ಚೌಕಗಳು. ಮೊದಲ ಚೌಕವನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಛಾಯೆಗೊಳಿಸಲಾಗಿದೆ, ಮತ್ತು ಅದರ ಅರ್ಧದಷ್ಟು ಹಸಿರು ಬಣ್ಣವನ್ನು ಹೊಂದಿದೆ.", "If the two squares together represent the number 2, what fraction is double-shaded (green) out of the whole figure?", "ಎರಡು ಚೌಕಗಳು ಒಟ್ಟಾಗಿ ಸಂಖ್ಯೆ 2 ನ್ನು ಪ್ರತಿನಿಧಿಸಿದರೆ, ಇಡೀ ಚಿತ್ರದಲ್ಲಿ ಯಾವ ಭಿನ್ನರಾಶಿಯು ಡಬಲ್-ಶೇಡ್ (ಹಸಿರು) ಆಗಿದೆ?", ["1/4", "1/2", "3/4", "1/8"], ["1/4", "1/2", "3/4", "1/8"], "1/4", "1/4", "The whole figure consists of 2 squares. The green part is half of one square, which is 1/4 of the total two squares.", "ಇಡೀ ಚಿತ್ರವು 2 ಚೌಕಗಳನ್ನು ಒಳಗೊಂಡಿದೆ. ಹಸಿರು ಭಾಗವು ಒಂದು ಚೌಕದ ಅರ್ಧದಷ್ಟಿದೆ, ಅಂದರೆ ಒಟ್ಟು ಎರಡು ಚೌಕಗಳಲ್ಲಿ 1/4 ಭಾಗ.")

add_img_s(2, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 150">
  <line x1="20" y1="75" x2="280" y2="75" stroke="#2563EB" stroke-width="2"/>
  <circle cx="100" cy="75" r="5" fill="#DC2626"/>
  <text x="100" y="100" fill="#1F2937" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">2.3</text>
  <circle cx="200" cy="75" r="5" fill="#DC2626"/>
  <text x="200" y="100" fill="#1F2937" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">2.4</text>
  <circle cx="150" cy="75" r="5" fill="#059669"/>
  <text x="150" y="60" fill="#059669" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">X</text>
</svg>""", "Number line showing points 2.3 and 2.4, with X exactly in the middle.", "2.3 ಮತ್ತು 2.4 ಬಿಂದುಗಳನ್ನು ತೋರಿಸುವ ಸಂಖ್ಯಾ ರೇಖೆ, X ನಿಖರವಾಗಿ ಮಧ್ಯದಲ್ಲಿದೆ.", "What is the value of X on the number line?", "ಸಂಖ್ಯಾರೇಖೆಯಲ್ಲಿ X ನ ಮೌಲ್ಯವೇನು?", ["2.35", "2.30", "2.45", "2.31"], ["2.35", "2.30", "2.45", "2.31"], "2.35", "2.35", "X is exactly halfway between 2.30 and 2.40, which is 2.35.", "X ನಿಖರವಾಗಿ 2.30 ಮತ್ತು 2.40 ರ ಮಧ್ಯದಲ್ಲಿದೆ, ಅಂದರೆ 2.35.")

add_img_m(2, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <rect x="50" y="50" width="200" height="40" fill="none" stroke="#2563EB" stroke-width="2"/>
  <rect x="50" y="50" width="150" height="40" fill="#DBEAFE" stroke="#2563EB" stroke-width="1"/>
  <line x1="100" y1="50" x2="100" y2="90" stroke="#2563EB" stroke-width="1"/>
  <line x1="150" y1="50" x2="150" y2="90" stroke="#2563EB" stroke-width="1"/>
  <line x1="200" y1="50" x2="200" y2="90" stroke="#2563EB" stroke-width="1"/>
</svg>""", "A bar divided into 4 parts. 3 parts are shaded.", "4 ಭಾಗಗಳಾಗಿ ವಿಂಗಡಿಸಲಾದ ಪಟ್ಟಿ. 3 ಭಾಗಗಳನ್ನು ಛಾಯೆಗೊಳಿಸಲಾಗಿದೆ.", "Which of the following correctly represent the shaded portion?", "ಛಾಯೆಗೊಳಿಸಿದ ಭಾಗವನ್ನು ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಯಾವುದು ಸರಿಯಾಗಿ ಪ್ರತಿನಿಧಿಸುತ್ತದೆ?", ["3/4", "75%", "0.75", "1/4"], ["3/4", "75%", "0.75", "1/4"], ["3/4", "75%", "0.75"], ["3/4", "75%", "0.75"], "3 out of 4 parts are shaded. 3/4 = 0.75 = 75%.", "4 ರಲ್ಲಿ 3 ಭಾಗಗಳನ್ನು ಛಾಯೆಗೊಳಿಸಲಾಗಿದೆ. 3/4 = 0.75 = 75%.")

add_multiple(2, "Which of these are proper fractions?", "ಇವುಗಳಲ್ಲಿ ಯಾವುದು ಸಮ ಭಿನ್ನರಾಶಿಗಳು (proper fractions)?", ["3/5", "7/4", "1/2", "9/10"], ["3/5", "7/4", "1/2", "9/10"], ["3/5", "1/2", "9/10"], ["3/5", "1/2", "9/10"], "A proper fraction has a numerator smaller than its denominator. 7/4 is an improper fraction.", "ಸಮ ಭಿನ್ನರಾಶಿಯು ಅದರ ಛೇದಕ್ಕಿಂತ ಚಿಕ್ಕದಾದ ಅಂಶವನ್ನು ಹೊಂದಿರುತ್ತದೆ. 7/4 ವಿಷಮ ಭಿನ್ನರಾಶಿಯಾಗಿದೆ.")

add_match(2, "Match the multiplication expression with its product:", "ಗುಣಾಕಾರದ ಅಭಿವ್ಯಕ್ತಿಯನ್ನು ಅದರ ಗುಣಲಬ್ಧದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "1/2 × 1/3", "right": "1/6"}, {"left": "2/5 × 5/2", "right": "1"}, {"left": "3/4 × 2/3", "right": "1/2"}, {"left": "1/4 × 1/4", "right": "1/16"}], [{"left": "1/2 × 1/3", "right": "1/6"}, {"left": "2/5 × 5/2", "right": "1"}, {"left": "3/4 × 2/3", "right": "1/2"}, {"left": "1/4 × 1/4", "right": "1/16"}], "Multiply numerators together and denominators together, then simplify.", "ಅಂಶಗಳನ್ನು ಮತ್ತು ಛೇದಗಳನ್ನು ಗುಣಿಸಿ, ನಂತರ ಸರಳೀಕರಿಸಿ.")


# Hard (10)
add_single(3, "Simplify: (2 1/5) ÷ (1 1/10)", "ಸರಳೀಕರಿಸಿ: (2 1/5) ÷ (1 1/10)", ["2", "1/2", "11/5", "4/5"], ["2", "1/2", "11/5", "4/5"], "2", "2", "Convert to improper fractions: 11/5 ÷ 11/10 = 11/5 × 10/11 = 2.", "ವಿಷಮ ಭಿನ್ನರಾಶಿಗಳಿಗೆ ಪರಿವರ್ತಿಸಿ: 11/5 ÷ 11/10 = 11/5 × 10/11 = 2.")
add_single(3, "A rectangular park is 20.5 m long and 15.2 m wide. What is its area?", "ಒಂದು ಆಯತಾಕಾರದ ಉದ್ಯಾನವು 20.5 ಮೀ ಉದ್ದ ಮತ್ತು 15.2 ಮೀ ಅಗಲವಿದೆ. ಅದರ ವಿಸ್ತೀರ್ಣ ಎಷ್ಟು?", ["311.6 m²", "311.06 m²", "31.16 m²", "300.6 m²"], ["311.6 m²", "311.06 m²", "31.16 m²", "300.6 m²"], "311.6 m²", "311.6 m²", "Area = length × width = 20.5 × 15.2 = 311.6 m².", "ವಿಸ್ತೀರ್ಣ = ಉದ್ದ × ಅಗಲ = 20.5 × 15.2 = 311.6 m².")
add_single(3, "Sushant reads 1/3 part of a book in 1 hour. How much part of the book will he read in 2 1/5 hours?", "ಸುಶಾಂತ್ ಒಂದು ಗಂಟೆಯಲ್ಲಿ ಪುಸ್ತಕದ 1/3 ಭಾಗವನ್ನು ಓದುತ್ತಾನೆ. 2 1/5 ಗಂಟೆಗಳಲ್ಲಿ ಅವನು ಪುಸ್ತಕದ ಎಷ್ಟು ಭಾಗವನ್ನು ಓದುತ್ತಾನೆ?", ["11/15", "5/11", "2/15", "3/11"], ["11/15", "5/11", "2/15", "3/11"], "11/15", "11/15", "Part read = 1/3 × (11/5) = 11/15.", "ಓದಿದ ಭಾಗ = 1/3 × (11/5) = 11/15.")
add_single(3, "Find the value of 25.5 ÷ 0.5", "25.5 ÷ 0.5 ರ ಮೌಲ್ಯವನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ", ["51", "5.1", "510", "0.51"], ["51", "5.1", "510", "0.51"], "51", "51", "25.5 / 0.5 = 255 / 5 = 51.", "25.5 / 0.5 = 255 / 5 = 51.")

add_img_s(3, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <polygon points="50,150 250,150 150,50" fill="none" stroke="#2563EB" stroke-width="2"/>
  <line x1="150" y1="50" x2="150" y2="150" stroke="#EA580C" stroke-width="2" stroke-dasharray="5,3"/>
  <text x="150" y="170" fill="#DC2626" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">Base = 5.4 cm</text>
  <text x="110" y="105" fill="#059669" font-family="Arial, sans-serif" font-size="14" text-anchor="middle">h = 3.5 cm</text>
  <path d="M 150,140 L 160,140 L 160,150" fill="none" stroke="#EA580C" stroke-width="1.5"/>
</svg>""", "A triangle with base 5.4 cm and height 3.5 cm.", "5.4 ಸೆಂ.ಮೀ ಪಾದ ಮತ್ತು 3.5 ಸೆಂ.ಮೀ ಎತ್ತರವಿರುವ ತ್ರಿಕೋನ.", "Find the area of the triangle shown in the figure.", "ಚಿತ್ರದಲ್ಲಿ ತೋರಿಸಿರುವ ತ್ರಿಕೋನದ ವಿಸ್ತೀರ್ಣವನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.", ["9.45 cm²", "18.9 cm²", "8.9 cm²", "9.45 cm"], ["9.45 cm²", "18.9 cm²", "8.9 cm²", "9.45 cm"], "9.45 cm²", "9.45 cm²", "Area = 1/2 × base × height = 1/2 × 5.4 × 3.5 = 2.7 × 3.5 = 9.45 cm².", "ವಿಸ್ತೀರ್ಣ = 1/2 × ಪಾದ × ಎತ್ತರ = 1/2 × 5.4 × 3.5 = 2.7 × 3.5 = 9.45 cm².")

add_img_m(3, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <circle cx="100" cy="100" r="50" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <line x1="50" y1="100" x2="150" y2="100" stroke="#2563EB" stroke-width="2"/>
  <line x1="100" y1="50" x2="100" y2="150" stroke="#2563EB" stroke-width="2"/>
  <circle cx="200" cy="100" r="50" fill="none" stroke="#2563EB" stroke-width="2"/>
  <path d="M200,100 L200,50 A50,50 0 0,1 250,100 Z" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <line x1="150" y1="100" x2="250" y2="100" stroke="#2563EB" stroke-width="2"/>
  <line x1="200" y1="50" x2="200" y2="150" stroke="#2563EB" stroke-width="2"/>
</svg>""", "Two circles. The first is fully shaded (4/4). The second has 1/4 shaded.", "ಎರಡು ವೃತ್ತಗಳು. ಮೊದಲನೆಯದು ಸಂಪೂರ್ಣವಾಗಿ ಛಾಯೆಗೊಳಿಸಲ್ಪಟ್ಟಿದೆ (4/4). ಎರಡನೆಯದು 1/4 ಛಾಯೆಗೊಳಿಸಲ್ಪಟ್ಟಿದೆ.", "Which of the following represent the total shaded area of both circles combined?", "ಎರಡೂ ವೃತ್ತಗಳ ಒಟ್ಟು ಛಾಯೆಗೊಳಿಸಿದ ಪ್ರದೇಶವನ್ನು ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಯಾವುದು ಪ್ರತಿನಿಧಿಸುತ್ತದೆ?", ["1 1/4", "5/4", "1.25", "3/4"], ["1 1/4", "5/4", "1.25", "3/4"], ["1 1/4", "5/4", "1.25"], ["1 1/4", "5/4", "1.25"], "One full circle (1) plus one quarter of a circle (1/4) equals 1 1/4, which is also 5/4 or 1.25.", "ಒಂದು ಪೂರ್ಣ ವೃತ್ತ (1) ಮತ್ತು ಕಾಲು ವೃತ್ತ (1/4) ಸೇರಿ 1 1/4 ಆಗುತ್ತದೆ, ಇದು 5/4 ಅಥವಾ 1.25 ಗೆ ಸಮ.")

add_multiple(3, "Which of the following expressions yield a result greater than 1?", "ಕೆಳಗಿನ ಯಾವ ಅಭಿವ್ಯಕ್ತಿಗಳು 1 ಕ್ಕಿಂತ ಹೆಚ್ಚಿನ ಫಲಿತಾಂಶವನ್ನು ನೀಡುತ್ತವೆ?", ["3/2 × 4/5", "5/4 ÷ 1/2", "0.8 × 1.5", "1/3 ÷ 1/2"], ["3/2 × 4/5", "5/4 ÷ 1/2", "0.8 × 1.5", "1/3 ÷ 1/2"], ["3/2 × 4/5", "5/4 ÷ 1/2", "0.8 × 1.5"], ["3/2 × 4/5", "5/4 ÷ 1/2", "0.8 × 1.5"], "3/2 × 4/5 = 12/10 = 1.2; 5/4 ÷ 1/2 = 5/2 = 2.5; 0.8 × 1.5 = 1.2; 1/3 ÷ 1/2 = 2/3 (less than 1).", "3/2 × 4/5 = 1.2; 5/4 ÷ 1/2 = 2.5; 0.8 × 1.5 = 1.2; 1/3 ÷ 1/2 = 2/3 (1 ಕ್ಕಿಂತ ಕಡಿಮೆ).")

add_match(3, "Match the fraction division with its correct result:", "ಭಿನ್ನರಾಶಿ ಭಾಗಾಕಾರವನ್ನು ಅದರ ಸರಿಯಾದ ಫಲಿತಾಂಶದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "3/5 ÷ 1/2", "right": "6/5"}, {"left": "1/2 ÷ 3/5", "right": "5/6"}, {"left": "2 1/2 ÷ 3/5", "right": "25/6"}, {"left": "3/5 ÷ 2 1/2", "right": "6/25"}], [{"left": "3/5 ÷ 1/2", "right": "6/5"}, {"left": "1/2 ÷ 3/5", "right": "5/6"}, {"left": "2 1/2 ÷ 3/5", "right": "25/6"}, {"left": "3/5 ÷ 2 1/2", "right": "6/25"}], "To divide by a fraction, multiply by its reciprocal.", "ಭಿನ್ನರಾಶಿಯಿಂದ ಭಾಗಿಸಲು, ಅದರ ವ್ಯುತ್ಕ್ರಮದಿಂದ ಗುಣಿಸಿ.")

add_match(3, "Match the word problem statement to the appropriate mathematical operation:", "ಪದ ಸಮಸ್ಯೆಯ ಹೇಳಿಕೆಯನ್ನು ಸೂಕ್ತವಾದ ಗಣಿತದ ಲೆಕ್ಕಾಚಾರದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "Half of 3/4 kg", "right": "1/2 × 3/4"}, {"left": "How many 1/2 kg pieces in 3/4 kg?", "right": "3/4 ÷ 1/2"}, {"left": "Add half kg and 3/4 kg", "right": "1/2 + 3/4"}, {"left": "Difference between 3/4 kg and half kg", "right": "3/4 - 1/2"}], [{"left": "3/4 ಕೆಜಿಯ ಅರ್ಧ", "right": "1/2 × 3/4"}, {"left": "3/4 ಕೆಜಿಯಲ್ಲಿ ಎಷ್ಟು 1/2 ಕೆಜಿ ತುಂಡುಗಳಿವೆ?", "right": "3/4 ÷ 1/2"}, {"left": "ಅರ್ಧ ಕೆಜಿ ಮತ್ತು 3/4 ಕೆಜಿ ಸೇರಿಸಿ", "right": "1/2 + 3/4"}, {"left": "3/4 ಕೆಜಿ ಮತ್ತು ಅರ್ಧ ಕೆಜಿಯ ನಡುವಿನ ವ್ಯತ್ಯಾಸ", "right": "3/4 - 1/2"}], "Translating words into math operators: 'of' means multiply, 'how many in' means divide.", "ಪದಗಳನ್ನು ಗಣಿತಕ್ಕೆ ಅನುವಾದಿಸುವುದು: 'ಅರ್ಧ' ಎಂದರೆ ಗುಣಾಕಾರ, 'ಎಷ್ಟು ಇವೆ' ಎಂದರೆ ಭಾಗಾಕಾರ.")

add_match(3, "Match the decimal with its fraction in simplest form:", "ದಶಮಾಂಶವನ್ನು ಅದರ ಸರಳ ರೂಪದ ಭಿನ್ನರಾಶಿಯೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "0.125", "right": "1/8"}, {"left": "0.375", "right": "3/8"}, {"left": "0.625", "right": "5/8"}, {"left": "0.875", "right": "7/8"}], [{"left": "0.125", "right": "1/8"}, {"left": "0.375", "right": "3/8"}, {"left": "0.625", "right": "5/8"}, {"left": "0.875", "right": "7/8"}], "125/1000 simplifies to 1/8. The rest are multiples of 1/8.", "125/1000 ಸರಳೀಕರಿಸಿದಾಗ 1/8 ಆಗುತ್ತದೆ. ಉಳಿದವು 1/8 ರ ಗುಣಕಗಳಾಗಿವೆ.")


with open('/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/maths/fractions_decimals.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)
