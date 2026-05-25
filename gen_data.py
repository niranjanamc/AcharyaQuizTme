import json

questions = []
q = 1

def add_single(diff, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_data_{q:03d}", "type": "single", "difficulty": diff,
        "en": {"question": en_q, "options": en_opts, "answer": en_ans, "reasoning": en_reas},
        "kn": {"question": kn_q, "options": kn_opts, "answer": kn_ans, "reasoning": kn_reas}
    })
    q += 1

def add_multiple(diff, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_data_{q:03d}", "type": "multiple", "difficulty": diff,
        "en": {"question": en_q, "options": en_opts, "answer": en_ans, "reasoning": en_reas},
        "kn": {"question": kn_q, "options": kn_opts, "answer": kn_ans, "reasoning": kn_reas}
    })
    q += 1

def add_match(diff, en_q, kn_q, en_pairs, kn_pairs, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_data_{q:03d}", "type": "match", "difficulty": diff,
        "en": {"question": en_q, "pairs": en_pairs, "reasoning": en_reas},
        "kn": {"question": kn_q, "pairs": kn_pairs, "reasoning": kn_reas}
    })
    q += 1

def add_img_s(diff, svg, en_alt, kn_alt, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_data_{q:03d}", "type": "image_single", "difficulty": diff,
        "image": {"type": "svg", "svg": svg.strip(), "alt": {"en": en_alt, "kn": kn_alt}},
        "en": {"question": en_q, "options": en_opts, "answer": en_ans, "reasoning": en_reas},
        "kn": {"question": kn_q, "options": kn_opts, "answer": kn_ans, "reasoning": kn_reas}
    })
    q += 1

def add_img_m(diff, svg, en_alt, kn_alt, en_q, kn_q, en_opts, kn_opts, en_ans, kn_ans, en_reas, kn_reas):
    global q
    questions.append({
        "id": f"c7_math_data_{q:03d}", "type": "image_multiple", "difficulty": diff,
        "image": {"type": "svg", "svg": svg.strip(), "alt": {"en": en_alt, "kn": kn_alt}},
        "en": {"question": en_q, "options": en_opts, "answer": en_ans, "reasoning": en_reas},
        "kn": {"question": kn_q, "options": kn_opts, "answer": kn_ans, "reasoning": kn_reas}
    })
    q += 1

# Easy (10)
add_single(1, "What is the mean of the first 5 natural numbers?", "ಮೊದಲ 5 ಸ್ವಾಭಾವಿಕ ಸಂಖ್ಯೆಗಳ ಸರಾಸರಿ (mean) ಎಷ್ಟು?", ["3", "2.5", "4", "5"], ["3", "2.5", "4", "5"], "3", "3", "Mean = (1+2+3+4+5)/5 = 15/5 = 3.", "ಸರಾಸರಿ = (1+2+3+4+5)/5 = 15/5 = 3.")
add_single(1, "Find the mode of the given data: 2, 3, 2, 4, 5, 2, 4.", "ಕೊಟ್ಟಿರುವ ದತ್ತಾಂಶಗಳ ರೂಢಿಬೆಲೆ (mode) ಯನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ: 2, 3, 2, 4, 5, 2, 4.", ["2", "3", "4", "5"], ["2", "3", "4", "5"], "2", "2", "Mode is the observation that occurs most frequently. 2 occurs 3 times.", "ರೂಢಿಬೆಲೆಯು ಅತಿ ಹೆಚ್ಚು ಬಾರಿ ಸಂಭವಿಸುವ ದತ್ತಾಂಶವಾಗಿದೆ. 2 ಮೂರು ಬಾರಿ ಬರುತ್ತದೆ.")
add_single(1, "What is the range of the data: 12, 15, 20, 8, 25?", "12, 15, 20, 8, 25 ದತ್ತಾಂಶಗಳ ವ್ಯಾಪ್ತಿ (range) ಎಷ್ಟು?", ["17", "8", "25", "12"], ["17", "8", "25", "12"], "17", "17", "Range = Maximum value - Minimum value = 25 - 8 = 17.", "ವ್ಯಾಪ್ತಿ = ಗರಿಷ್ಠ ಮೌಲ್ಯ - ಕನಿಷ್ಠ ಮೌಲ್ಯ = 25 - 8 = 17.")
add_single(1, "When a die is thrown, what is the probability of getting a 5?", "ದಾಳವನ್ನು ಎಸೆದಾಗ 5 ಪಡೆಯುವ ಸಂಭವನೀಯತೆ (probability) ಎಷ್ಟು?", ["1/6", "5/6", "1/2", "1/5"], ["1/6", "5/6", "1/2", "1/5"], "1/6", "1/6", "A die has 6 faces (1, 2, 3, 4, 5, 6). The outcome '5' occurs exactly once.", "ದಾಳವು 6 ಮುಖಗಳನ್ನು (1, 2, 3, 4, 5, 6) ಹೊಂದಿದೆ. '5' ಕೇವಲ ಒಂದು ಬಾರಿ ಇರುತ್ತದೆ.")
add_single(1, "Which of the following values must be one of the observations in the data?", "ಈ ಕೆಳಗಿನ ಯಾವ ಮೌಲ್ಯವು ದತ್ತಾಂಶದಲ್ಲಿನ ವೀಕ್ಷಣೆಗಳಲ್ಲಿ ಒಂದಾಗಿರಬೇಕು?", ["Mode", "Mean", "Median", "Range"], ["ರೂಢಿಬೆಲೆ (Mode)", "ಸರಾಸರಿ (Mean)", "ಮಧ್ಯಾಂಕ (Median)", "ವ್ಯಾಪ್ತಿ (Range)"], "Mode", "ರೂಢಿಬೆಲೆ (Mode)", "The mode is always one of the numbers in a given data set.", "ರೂಢಿಬೆಲೆಯು ಯಾವಾಗಲೂ ದತ್ತಾಂಶದಲ್ಲಿನ ಸಂಖ್ಯೆಗಳಲ್ಲಿ ಒಂದಾಗಿರುತ್ತದೆ.")
add_single(1, "Find the median of the data: 5, 2, 8, 4, 7.", "5, 2, 8, 4, 7 ದತ್ತಾಂಶಗಳ ಮಧ್ಯಾಂಕ (median) ನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.", ["5", "4", "7", "8"], ["5", "4", "7", "8"], "5", "5", "Arrange in ascending order: 2, 4, 5, 7, 8. The middle value is 5.", "ಏರಿಕೆ ಕ್ರಮದಲ್ಲಿ ಜೋಡಿಸಿ: 2, 4, 5, 7, 8. ಮಧ್ಯದ ಮೌಲ್ಯ 5.")

add_img_s(1, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <line x1="40" y1="20" x2="40" y2="160" stroke="#1F2937" stroke-width="2"/>
  <line x1="40" y1="160" x2="280" y2="160" stroke="#1F2937" stroke-width="2"/>
  <text x="25" y="165" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">0</text>
  <text x="25" y="115" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">5</text>
  <text x="25" y="65" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">10</text>
  <text x="25" y="15" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">15</text>
  <rect x="60" y="65" width="30" height="95" fill="#2563EB"/>
  <rect x="120" y="115" width="30" height="45" fill="#2563EB"/>
  <rect x="180" y="15" width="30" height="145" fill="#2563EB"/>
  <rect x="240" y="65" width="30" height="95" fill="#2563EB"/>
  <text x="75" y="180" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">Cat</text>
  <text x="135" y="180" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">Dog</text>
  <text x="195" y="180" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">Fish</text>
  <text x="255" y="180" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">Bird</text>
</svg>""", "Bar graph showing Cat=10, Dog=5, Fish=15, Bird=10.", "ಬೆಕ್ಕು=10, ನಾಯಿ=5, ಮೀನು=15, ಪಕ್ಷಿ=10 ಅನ್ನು ತೋರಿಸುವ ಸ್ತಂಭ ನಕ್ಷೆ.", "Which pet is the most popular according to the bar graph?", "ಸ್ತಂಭ ನಕ್ಷೆಯ ಪ್ರಕಾರ ಯಾವ ಸಾಕುಪ್ರಾಣಿ ಹೆಚ್ಚು ಜನಪ್ರಿಯವಾಗಿದೆ?", ["Fish", "Cat", "Bird", "Dog"], ["ಮೀನು", "ಬೆಕ್ಕು", "ಪಕ್ಷಿ", "ನಾಯಿ"], "Fish", "ಮೀನು", "The tallest bar is for Fish (15).", "ಅತಿ ಎತ್ತರದ ಸ್ತಂಭ ಮೀನಿಗೆ (15) ಸೇರಿದೆ.")

add_img_s(1, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
  <circle cx="100" cy="100" r="80" fill="none" stroke="#1F2937" stroke-width="2"/>
  <line x1="100" y1="20" x2="100" y2="180" stroke="#1F2937" stroke-width="2"/>
  <line x1="20" y1="100" x2="180" y2="100" stroke="#1F2937" stroke-width="2"/>
  <text x="60" y="65" fill="#DC2626" font-family="Arial, sans-serif" font-size="24" text-anchor="middle">R</text>
  <text x="140" y="65" fill="#DC2626" font-family="Arial, sans-serif" font-size="24" text-anchor="middle">B</text>
  <text x="60" y="145" fill="#DC2626" font-family="Arial, sans-serif" font-size="24" text-anchor="middle">G</text>
  <text x="140" y="145" fill="#DC2626" font-family="Arial, sans-serif" font-size="24" text-anchor="middle">R</text>
  <path d="M100,100 L120,40" fill="none" stroke="#2563EB" stroke-width="4" marker-end="url(#arrow)"/>
  <defs>
    <marker id="arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6" fill="#2563EB"/>
    </marker>
  </defs>
</svg>""", "A spinner with 4 equal sections labeled R, B, G, R.", "R, B, G, R ಎಂದು ಲೇಬಲ್ ಮಾಡಲಾದ 4 ಸಮಾನ ವಿಭಾಗಗಳಿರುವ ಸ್ಪಿನ್ನರ್.", "What is the probability of the spinner landing on 'R'?", "ಸ್ಪಿನ್ನರ್ 'R' ನಲ್ಲಿ ನಿಲ್ಲುವ ಸಂಭವನೀಯತೆ ಎಷ್ಟು?", ["2/4", "1/4", "3/4", "0"], ["2/4", "1/4", "3/4", "0"], "2/4", "2/4", "There are 4 sections in total, and 2 of them are 'R'. So, 2/4 (or 1/2).", "ಒಟ್ಟು 4 ವಿಭಾಗಗಳಿವೆ, ಮತ್ತು ಅವುಗಳಲ್ಲಿ 2 'R' ಆಗಿವೆ. ಆದ್ದರಿಂದ, 2/4 (ಅಥವಾ 1/2).")

add_multiple(1, "Which of the following events are 'Certain' to happen?", "ಈ ಕೆಳಗಿನ ಯಾವ ಘಟನೆಗಳು ಖಂಡಿತವಾಗಿ ಸಂಭವಿಸುತ್ತವೆ?", ["The sun coming up from the West", "A tossed coin landing heads up", "You are older today than yesterday", "A die will land on a number less than 7"], ["ಸೂರ್ಯ ಪಶ್ಚಿಮದಿಂದ ಹುಟ್ಟುವುದು", "ಚಿಮ್ಮಿದ ನಾಣ್ಯದ ತಲೆ ಭಾಗ ಮೇಲಕ್ಕೆ ಬರುವುದು", "ನಿನ್ನೆಗಿಂತ ಇಂದು ನಿಮ್ಮ ವಯಸ್ಸು ಹೆಚ್ಚಾಗಿದೆ", "ದಾಳವು 7 ಕ್ಕಿಂತ ಕಡಿಮೆ ಸಂಖ್ಯೆಯಲ್ಲಿ ನಿಲ್ಲುತ್ತದೆ"], ["You are older today than yesterday", "A die will land on a number less than 7"], ["ನಿನ್ನೆಗಿಂತ ಇಂದು ನಿಮ್ಮ ವಯಸ್ಸು ಹೆಚ್ಚಾಗಿದೆ", "ದಾಳವು 7 ಕ್ಕಿಂತ ಕಡಿಮೆ ಸಂಖ್ಯೆಯಲ್ಲಿ ನಿಲ್ಲುತ್ತದೆ"], "Being older today than yesterday and rolling < 7 on a standard die are facts.", "ನಿನ್ನೆಗಿಂತ ಇಂದು ವಯಸ್ಸು ಹೆಚ್ಚಾಗಿರುವುದು ಮತ್ತು ದಾಳದ ಮೇಲೆ < 7 ಬರುವುದು ಸತ್ಯದ ಸಂಗತಿಗಳು.")

add_match(1, "Match the statistical term with its definition:", "ಸಾಂಖ್ಯಿಕ ಪದವನ್ನು ಅದರ ವ್ಯಾಖ್ಯಾನದೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "Mean", "right": "Sum of observations / Number of observations"}, {"left": "Median", "right": "Middle observation when data is sorted"}, {"left": "Mode", "right": "Observation that occurs most often"}, {"left": "Range", "right": "Difference between highest and lowest value"}], [{"left": "ಸರಾಸರಿ (Mean)", "right": "ವೀಕ್ಷಣೆಗಳ ಮೊತ್ತ / ವೀಕ್ಷಣೆಗಳ ಸಂಖ್ಯೆ"}, {"left": "ಮಧ್ಯಾಂಕ (Median)", "right": "ದತ್ತಾಂಶವನ್ನು ವಿಂಗಡಿಸಿದಾಗ ಮಧ್ಯದ ವೀಕ್ಷಣೆ"}, {"left": "ರೂಢಿಬೆಲೆ (Mode)", "right": "ಹೆಚ್ಚು ಬಾರಿ ಸಂಭವಿಸುವ ವೀಕ್ಷಣೆ"}, {"left": "ವ್ಯಾಪ್ತಿ (Range)", "right": "ಗರಿಷ್ಠ ಮತ್ತು ಕನಿಷ್ಠ ಮೌಲ್ಯದ ನಡುವಿನ ವ್ಯತ್ಯಾಸ"}], "These are the core definitions of central tendency and spread.", "ಇವುಗಳು ಕೇಂದ್ರೀಯ ಪ್ರವೃತ್ತಿ ಮತ್ತು ವ್ಯಾಪ್ತಿಯ ಮೂಲ ವ್ಯಾಖ್ಯಾನಗಳಾಗಿವೆ.")


# Medium (10)
add_single(2, "The mean of 4, 6, x, 8, 10 is 7. Find the value of x.", "4, 6, x, 8, 10 ರ ಸರಾಸರಿ 7. x ನ ಮೌಲ್ಯವನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.", ["7", "6", "8", "9"], ["7", "6", "8", "9"], "7", "7", "(4 + 6 + x + 8 + 10) / 5 = 7 => 28 + x = 35 => x = 7.", "(4 + 6 + x + 8 + 10) / 5 = 7 => 28 + x = 35 => x = 7.")
add_single(2, "The marks (out of 100) obtained by a group of students in a science test are 85, 76, 90, 85, 39, 48, 56, 95, 81 and 75. Find the range.", "ವಿಜ್ಞಾನ ಪರೀಕ್ಷೆಯಲ್ಲಿ ವಿದ್ಯಾರ್ಥಿಗಳ ಗುಂಪು ಪಡೆದ ಅಂಕಗಳು 85, 76, 90, 85, 39, 48, 56, 95, 81 ಮತ್ತು 75. ವ್ಯಾಪ್ತಿಯನ್ನು (range) ಕಂಡುಹಿಡಿಯಿರಿ.", ["56", "95", "39", "45"], ["56", "95", "39", "45"], "56", "56", "Highest = 95. Lowest = 39. Range = 95 - 39 = 56.", "ಗರಿಷ್ಠ = 95. ಕನಿಷ್ಠ = 39. ವ್ಯಾಪ್ತಿ = 95 - 39 = 56.")
add_single(2, "A coin is flipped twice. What are all the possible outcomes?", "ಒಂದು ನಾಣ್ಯವನ್ನು ಎರಡು ಬಾರಿ ಚಿಮ್ಮಲಾಗುತ್ತದೆ. ಸಂಭಾವ್ಯ ಫಲಿತಾಂಶಗಳು ಯಾವುವು?", ["HH, TT", "HT, TH", "HH, HT, TH, TT", "H, T"], ["HH, TT", "HT, TH", "HH, HT, TH, TT", "H, T"], "HH, HT, TH, TT", "HH, HT, TH, TT", "Two flips yield 2 × 2 = 4 outcomes: HH, HT, TH, TT.", "ಎರಡು ಬಾರಿ ಚಿಮ್ಮಿದಾಗ 2 × 2 = 4 ಫಲಿತಾಂಶಗಳು ಬರುತ್ತವೆ: HH, HT, TH, TT.")
add_single(2, "Find the median of the data: 13, 16, 12, 14, 19, 12, 14, 13, 14", "13, 16, 12, 14, 19, 12, 14, 13, 14 ದತ್ತಾಂಶಗಳ ಮಧ್ಯಾಂಕವನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.", ["13", "14", "12", "16"], ["13", "14", "12", "16"], "14", "14", "Sorted: 12, 12, 13, 13, 14, 14, 14, 16, 19. The 5th value is 14.", "ವಿಂಗಡಿಸಿದಾಗ: 12, 12, 13, 13, 14, 14, 14, 16, 19. 5 ನೇ ಮೌಲ್ಯವು 14.")
add_single(2, "Is the median always one of the numbers in a data set?", "ಮಧ್ಯಾಂಕವು (median) ಯಾವಾಗಲೂ ದತ್ತಾಂಶದಲ್ಲಿನ ಸಂಖ್ಯೆಗಳಲ್ಲಿ ಒಂದಾಗಿರುತ್ತದೆಯೇ?", ["Yes, always", "No, if there is an even number of observations", "No, it's never in the data", "Only for grouped data"], ["ಹೌದು, ಯಾವಾಗಲೂ", "ಇಲ್ಲ, ವೀಕ್ಷಣೆಗಳ ಸಂಖ್ಯೆ ಸಮವಾಗಿದ್ದಾಗ", "ಇಲ್ಲ, ಇದು ಎಂದಿಗೂ ದತ್ತಾಂಶದಲ್ಲಿ ಇರುವುದಿಲ್ಲ", "ಗುಂಪು ದತ್ತಾಂಶಕ್ಕೆ ಮಾತ್ರ"], "No, if there is an even number of observations", "ಇಲ್ಲ, ವೀಕ್ಷಣೆಗಳ ಸಂಖ್ಯೆ ಸಮವಾಗಿದ್ದಾಗ", "If there are an even number of observations, the median is the average of the two middle numbers, which might not be in the set.", "ಸಮ ಸಂಖ್ಯೆಯ ವೀಕ್ಷಣೆಗಳಿದ್ದರೆ, ಮಧ್ಯಾಂಕವು ಮಧ್ಯದ ಎರಡು ಸಂಖ್ಯೆಗಳ ಸರಾಸರಿಯಾಗಿರುತ್ತದೆ, ಅದು ಸೆಟ್‌ನಲ್ಲಿ ಇರದಿರಬಹುದು.")

add_img_s(2, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <line x1="40" y1="20" x2="40" y2="160" stroke="#1F2937" stroke-width="2"/>
  <line x1="40" y1="160" x2="280" y2="160" stroke="#1F2937" stroke-width="2"/>
  <rect x="60" y="60" width="20" height="100" fill="#2563EB"/>
  <rect x="80" y="40" width="20" height="120" fill="#059669"/>
  <rect x="140" y="100" width="20" height="60" fill="#2563EB"/>
  <rect x="160" y="80" width="20" height="80" fill="#059669"/>
  <rect x="220" y="20" width="20" height="140" fill="#2563EB"/>
  <rect x="240" y="120" width="20" height="40" fill="#059669"/>
  <text x="75" y="180" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">Maths</text>
  <text x="155" y="180" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">Science</text>
  <text x="235" y="180" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">English</text>
  <!-- Legend -->
  <rect x="60" y="20" width="10" height="10" fill="#2563EB"/>
  <text x="75" y="29" fill="#1F2937" font-family="Arial, sans-serif" font-size="10">Term 1</text>
  <rect x="120" y="20" width="10" height="10" fill="#059669"/>
  <text x="135" y="29" fill="#1F2937" font-family="Arial, sans-serif" font-size="10">Term 2</text>
</svg>""", "Double bar graph showing Term 1 and Term 2 marks for Maths, Science, and English.", "ಗಣಿತ, ವಿಜ್ಞಾನ ಮತ್ತು ಇಂಗ್ಲಿಷ್‌ಗೆ ಟರ್ಮ್ 1 ಮತ್ತು ಟರ್ಮ್ 2 ಅಂಕಗಳನ್ನು ತೋರಿಸುವ ಡಬಲ್ ಬಾರ್ ಗ್ರಾಫ್.", "In which subject did the performance go down from Term 1 to Term 2?", "ಯಾವ ವಿಷಯದಲ್ಲಿ ಟರ್ಮ್ 1 ರಿಂದ ಟರ್ಮ್ 2 ಕ್ಕೆ ಸಾಧನೆ ಕಡಿಮೆಯಾಗಿದೆ?", ["Maths", "Science", "English", "None"], ["ಗಣಿತ", "ವಿಜ್ಞಾನ", "ಇಂಗ್ಲಿಷ್", "ಯಾವುದೂ ಅಲ್ಲ"], "English", "ಇಂಗ್ಲಿಷ್", "For English, the blue bar (Term 1) is taller than the green bar (Term 2).", "ಇಂಗ್ಲಿಷ್‌ಗೆ, ನೀಲಿ ಬಾರ್ (ಟರ್ಮ್ 1) ಹಸಿರು ಬಾರ್‌ಗಿಂತ (ಟರ್ಮ್ 2) ಎತ್ತರವಾಗಿದೆ.")

add_img_s(2, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 150">
  <rect x="20" y="50" width="40" height="40" rx="5" fill="white" stroke="#1F2937" stroke-width="2"/>
  <circle cx="40" cy="70" r="4" fill="#DC2626"/>
  <rect x="70" y="50" width="40" height="40" rx="5" fill="white" stroke="#1F2937" stroke-width="2"/>
  <circle cx="80" cy="60" r="4" fill="#DC2626"/>
  <circle cx="100" cy="80" r="4" fill="#DC2626"/>
  <rect x="120" y="50" width="40" height="40" rx="5" fill="white" stroke="#1F2937" stroke-width="2"/>
  <circle cx="130" cy="60" r="4" fill="#DC2626"/>
  <circle cx="140" cy="70" r="4" fill="#DC2626"/>
  <circle cx="150" cy="80" r="4" fill="#DC2626"/>
  <rect x="170" y="50" width="40" height="40" rx="5" fill="white" stroke="#1F2937" stroke-width="2"/>
  <circle cx="180" cy="60" r="4" fill="#DC2626"/>
  <circle cx="200" cy="60" r="4" fill="#DC2626"/>
  <circle cx="180" cy="80" r="4" fill="#DC2626"/>
  <circle cx="200" cy="80" r="4" fill="#DC2626"/>
  <rect x="220" y="50" width="40" height="40" rx="5" fill="white" stroke="#1F2937" stroke-width="2"/>
  <circle cx="230" cy="60" r="4" fill="#DC2626"/>
  <circle cx="250" cy="60" r="4" fill="#DC2626"/>
  <circle cx="240" cy="70" r="4" fill="#DC2626"/>
  <circle cx="230" cy="80" r="4" fill="#DC2626"/>
  <circle cx="250" cy="80" r="4" fill="#DC2626"/>
</svg>""", "Five dice showing 1, 2, 3, 4, 5 dots respectively.", "1, 2, 3, 4, 5 ಚುಕ್ಕೆಗಳನ್ನು ತೋರಿಸುವ ಐದು ದಾಳಗಳು.", "If these 5 numbers represent a data set, what is the mean of this data set?", "ಈ 5 ಸಂಖ್ಯೆಗಳು ದತ್ತಾಂಶ ಸೆಟ್ ಅನ್ನು ಪ್ರತಿನಿಧಿಸಿದರೆ, ಈ ದತ್ತಾಂಶ ಸೆಟ್ ನ ಸರಾಸರಿ ಎಷ್ಟು?", ["3", "15", "5", "4"], ["3", "15", "5", "4"], "3", "3", "(1+2+3+4+5)/5 = 15/5 = 3.", "(1+2+3+4+5)/5 = 15/5 = 3.")

add_img_m(2, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <rect x="50" y="50" width="200" height="100" fill="#DBEAFE" stroke="#2563EB" stroke-width="2"/>
  <line x1="50" y1="100" x2="250" y2="100" stroke="#2563EB" stroke-width="2"/>
  <line x1="150" y1="50" x2="150" y2="150" stroke="#2563EB" stroke-width="2"/>
  <text x="100" y="80" fill="#1F2937" font-family="Arial, sans-serif" font-size="20" text-anchor="middle">5</text>
  <text x="200" y="80" fill="#1F2937" font-family="Arial, sans-serif" font-size="20" text-anchor="middle">5</text>
  <text x="100" y="130" fill="#1F2937" font-family="Arial, sans-serif" font-size="20" text-anchor="middle">2</text>
  <text x="200" y="130" fill="#1F2937" font-family="Arial, sans-serif" font-size="20" text-anchor="middle">8</text>
</svg>""", "A set of four numbers: 5, 5, 2, 8.", "ನಾಲ್ಕು ಸಂಖ್ಯೆಗಳ ಸೆಟ್: 5, 5, 2, 8.", "Which of the following statistics equal 5 for this data set?", "ಈ ದತ್ತಾಂಶಕ್ಕಾಗಿ ಕೆಳಗಿನ ಯಾವ ಅಂಕಿಅಂಶವು 5 ಕ್ಕೆ ಸಮಾನವಾಗಿರುತ್ತದೆ?", ["Mean", "Median", "Mode", "Range"], ["ಸರಾಸರಿ (Mean)", "ಮಧ್ಯಾಂಕ (Median)", "ರೂಢಿಬೆಲೆ (Mode)", "ವ್ಯಾಪ್ತಿ (Range)"], ["Mean", "Median", "Mode"], ["ಸರಾಸರಿ (Mean)", "ಮಧ್ಯಾಂಕ (Median)", "ರೂಢಿಬೆಲೆ (Mode)"], "Mean: (5+5+2+8)/4=20/4=5. Median: sorted 2, 5, 5, 8; avg of 5, 5 is 5. Mode: 5. Range: 8-2=6.", "ಸರಾಸರಿ: 20/4=5. ಮಧ್ಯಾಂಕ: ಮಧ್ಯದ ಎರಡು 5 ರ ಸರಾಸರಿ 5. ರೂಢಿಬೆಲೆ: 5. ವ್ಯಾಪ್ತಿ: 8-2=6.")

add_multiple(2, "Which of the following probabilities are impossible?", "ಈ ಕೆಳಗಿನ ಯಾವ ಸಂಭವನೀಯತೆಗಳು ಅಸಾಧ್ಯ?", ["1.5", "-0.2", "0", "1"], ["1.5", "-0.2", "0", "1"], ["1.5", "-0.2"], ["1.5", "-0.2"], "Probability must always be between 0 and 1 inclusive.", "ಸಂಭವನೀಯತೆ ಯಾವಾಗಲೂ 0 ಮತ್ತು 1 ರ ನಡುವೆ ಇರಬೇಕು.")

add_match(2, "Match the event with its probability when a die is thrown:", "ದಾಳವನ್ನು ಎಸೆದಾಗ ಘಟನೆಯನ್ನು ಅದರ ಸಂಭವನೀಯತೆಯೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "Getting an even number", "right": "3/6 (or 1/2)"}, {"left": "Getting a 7", "right": "0"}, {"left": "Getting a number less than 7", "right": "1"}, {"left": "Getting a prime number", "right": "3/6 (or 1/2)"}], [{"left": "ಸಮ ಸಂಖ್ಯೆಯನ್ನು ಪಡೆಯುವುದು", "right": "3/6 (ಅಥವಾ 1/2)"}, {"left": "7 ಅನ್ನು ಪಡೆಯುವುದು", "right": "0"}, {"left": "7 ಕ್ಕಿಂತ ಕಡಿಮೆ ಸಂಖ್ಯೆಯನ್ನು ಪಡೆಯುವುದು", "right": "1"}, {"left": "ಅವಿಭಾಜ್ಯ ಸಂಖ್ಯೆಯನ್ನು ಪಡೆಯುವುದು", "right": "3/6 (ಅಥವಾ 1/2)"}], "Even: 2,4,6. Prime: 2,3,5. Total outcomes = 6.", "ಸಮ: 2,4,6. ಅವಿಭಾಜ್ಯ: 2,3,5. ಒಟ್ಟು ಫಲಿತಾಂಶಗಳು = 6.")


# Hard (10)
add_single(3, "The mean of 10 observations is 15. If one observation 15 is removed, what will be the new mean?", "10 ವೀಕ್ಷಣೆಗಳ ಸರಾಸರಿ 15. ಒಂದು ವೀಕ್ಷಣೆ 15 ಅನ್ನು ತೆಗೆದುಹಾಕಿದರೆ, ಹೊಸ ಸರಾಸರಿ ಏನಾಗುತ್ತದೆ?", ["15", "14", "16", "13.5"], ["15", "14", "16", "13.5"], "15", "15", "Total sum = 10 × 15 = 150. New sum = 150 - 15 = 135. New mean = 135 / 9 = 15.", "ಒಟ್ಟು ಮೊತ್ತ = 10 × 15 = 150. ಹೊಸ ಮೊತ್ತ = 150 - 15 = 135. ಹೊಸ ಸರಾಸರಿ = 135 / 9 = 15.")
add_single(3, "If a box contains 3 red, 2 blue, and 5 green marbles, what is the probability of NOT drawing a blue marble?", "ಒಂದು ಪೆಟ್ಟಿಗೆಯು 3 ಕೆಂಪು, 2 ನೀಲಿ ಮತ್ತು 5 ಹಸಿರು ಗೋಲಿಗಳನ್ನು ಹೊಂದಿದ್ದರೆ, ನೀಲಿ ಗೋಲಿಯನ್ನು ತೆಗೆಯದಿರುವ ಸಂಭವನೀಯತೆ ಎಷ್ಟು?", ["8/10", "2/10", "5/10", "3/10"], ["8/10", "2/10", "5/10", "3/10"], "8/10", "8/10", "Total = 10. Non-blue = 3 (red) + 5 (green) = 8. Probability = 8/10 or 4/5.", "ಒಟ್ಟು = 10. ನೀಲಿಯಲ್ಲದವು = 3 (ಕೆಂಪು) + 5 (ಹಸಿರು) = 8. ಸಂಭವನೀಯತೆ = 8/10.")
add_single(3, "The median of observations 11, 12, 14, x-1, x+1, 20, 22, 25 arranged in ascending order is 16. Find x.", "ಏರಿಕೆ ಕ್ರಮದಲ್ಲಿ ಜೋಡಿಸಲಾದ 11, 12, 14, x-1, x+1, 20, 22, 25 ವೀಕ್ಷಣೆಗಳ ಮಧ್ಯಾಂಕವು 16 ಆಗಿದೆ. x ಅನ್ನು ಕಂಡುಹಿಡಿಯಿರಿ.", ["16", "15", "17", "18"], ["16", "15", "17", "18"], "16", "16", "8 observations. Median is average of 4th and 5th: (x-1 + x+1)/2 = 2x/2 = x. So, x = 16.", "8 ವೀಕ್ಷಣೆಗಳು. ಮಧ್ಯಾಂಕವು 4 ಮತ್ತು 5 ನೇ ಸರಾಸರಿ: (x-1 + x+1)/2 = 2x/2 = x. ಆದ್ದರಿಂದ, x = 16.")
add_single(3, "Can a data set have more than one mode?", "ಒಂದು ದತ್ತಾಂಶವು ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು ರೂಢಿಬೆಲೆಯನ್ನು ಹೊಂದಿರಬಹುದೇ?", ["Yes", "No", "Only if mean equals median", "Only in grouped data"], ["ಹೌದು", "ಇಲ್ಲ", "ಸರಾಸರಿಯು ಮಧ್ಯಾಂಕಕ್ಕೆ ಸಮನಾಗಿದ್ದರೆ ಮಾತ್ರ", "ಗುಂಪು ದತ್ತಾಂಶದಲ್ಲಿ ಮಾತ್ರ"], "Yes", "ಹೌದು", "Yes, if two or more values have the same maximum frequency, the data is multimodal.", "ಹೌದು, ಎರಡು ಅಥವಾ ಅದಕ್ಕಿಂತ ಹೆಚ್ಚು ಮೌಲ್ಯಗಳು ಒಂದೇ ಗರಿಷ್ಠ ಆವರ್ತನವನ್ನು ಹೊಂದಿದ್ದರೆ, ದತ್ತಾಂಶವು ಬಹು-ಮೋಡಲ್ ಆಗಿರುತ್ತದೆ.")

add_img_s(3, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <circle cx="150" cy="100" r="80" fill="white" stroke="#1F2937" stroke-width="2"/>
  <path d="M150,100 L150,20 A80,80 0 0,1 230,100 Z" fill="#DC2626" stroke="#1F2937" stroke-width="1"/>
  <path d="M150,100 L230,100 A80,80 0 0,1 150,180 Z" fill="#2563EB" stroke="#1F2937" stroke-width="1"/>
  <path d="M150,100 L150,180 A80,80 0 0,1 70,100 Z" fill="#059669" stroke="#1F2937" stroke-width="1"/>
  <path d="M150,100 L70,100 A80,80 0 0,1 150,20 Z" fill="#EA580C" stroke="#1F2937" stroke-width="1"/>
  <text x="180" y="60" fill="white" font-family="Arial, sans-serif" font-size="20">1</text>
  <text x="180" y="150" fill="white" font-family="Arial, sans-serif" font-size="20">2</text>
  <text x="120" y="150" fill="white" font-family="Arial, sans-serif" font-size="20">3</text>
  <text x="120" y="60" fill="white" font-family="Arial, sans-serif" font-size="20">4</text>
</svg>""", "A spinner with 4 equal sections numbered 1 to 4.", "1 ರಿಂದ 4 ರವರೆಗೆ ಸಂಖ್ಯೆಯ 4 ಸಮಾನ ವಿಭಾಗಗಳಿರುವ ಸ್ಪಿನ್ನರ್.", "If this spinner is spun twice and the numbers are added, what is the probability that the sum is 5?", "ಈ ಸ್ಪಿನ್ನರ್ ಅನ್ನು ಎರಡು ಬಾರಿ ತಿರುಗಿಸಿ ಮತ್ತು ಸಂಖ್ಯೆಗಳನ್ನು ಸೇರಿಸಿದರೆ, ಮೊತ್ತ 5 ಆಗಿರುವ ಸಂಭವನೀಯತೆ ಎಷ್ಟು?", ["4/16 (or 1/4)", "5/16", "3/16", "1/8"], ["4/16 (ಅಥವಾ 1/4)", "5/16", "3/16", "1/8"], "4/16 (or 1/4)", "4/16 (ಅಥವಾ 1/4)", "Total outcomes = 4 × 4 = 16. Sum 5 outcomes: (1,4), (2,3), (3,2), (4,1) -> 4 outcomes. 4/16 = 1/4.", "ಒಟ್ಟು ಫಲಿತಾಂಶಗಳು = 4 × 4 = 16. ಮೊತ್ತ 5 ಬರುವ ಫಲಿತಾಂಶಗಳು: (1,4), (2,3), (3,2), (4,1) -> 4 ಫಲಿತಾಂಶಗಳು. 4/16 = 1/4.")

add_img_m(3, """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 200">
  <rect x="50" y="80" width="30" height="20" fill="#2563EB" stroke="white"/>
  <rect x="90" y="60" width="30" height="40" fill="#2563EB" stroke="white"/>
  <rect x="130" y="20" width="30" height="80" fill="#2563EB" stroke="white"/>
  <rect x="170" y="60" width="30" height="40" fill="#2563EB" stroke="white"/>
  <rect x="210" y="80" width="30" height="20" fill="#2563EB" stroke="white"/>
  <line x1="40" y1="100" x2="250" y2="100" stroke="#1F2937" stroke-width="2"/>
  <text x="65" y="120" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">1</text>
  <text x="105" y="120" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">2</text>
  <text x="145" y="120" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">3</text>
  <text x="185" y="120" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">4</text>
  <text x="225" y="120" fill="#1F2937" font-family="Arial, sans-serif" font-size="12" text-anchor="middle">5</text>
  <text x="30" y="90" fill="#1F2937" font-family="Arial, sans-serif" font-size="12">1</text>
  <text x="30" y="70" fill="#1F2937" font-family="Arial, sans-serif" font-size="12">2</text>
  <text x="30" y="30" fill="#1F2937" font-family="Arial, sans-serif" font-size="12">4</text>
</svg>""", "Bar graph representing frequency of values 1 to 5. Frequencies: 1, 2, 4, 2, 1.", "1 ರಿಂದ 5 ರವರೆಗಿನ ಮೌಲ್ಯಗಳ ಆವರ್ತನವನ್ನು ಪ್ರತಿನಿಧಿಸುವ ಸ್ತಂಭ ನಕ್ಷೆ. ಆವರ್ತನಗಳು: 1, 2, 4, 2, 1.", "For the data shown in the bar graph (frequencies: 1, 2, 4, 2, 1 for values 1, 2, 3, 4, 5 respectively), which of the following are true?", "ಸ್ತಂಭ ನಕ್ಷೆಯಲ್ಲಿ ತೋರಿಸಿರುವ ದತ್ತಾಂಶಕ್ಕಾಗಿ, ಕೆಳಗಿನವುಗಳಲ್ಲಿ ಯಾವುದು ಸರಿ?", ["The mean is 3", "The median is 3", "The mode is 3", "The range is 5"], ["ಸರಾಸರಿ 3", "ಮಧ್ಯಾಂಕ 3", "ರೂಢಿಬೆಲೆ 3", "ವ್ಯಾಪ್ತಿ 5"], ["The mean is 3", "The median is 3", "The mode is 3"], ["ಸರಾಸರಿ 3", "ಮಧ್ಯಾಂಕ 3", "ರೂಢಿಬೆಲೆ 3"], "Total items=10. Sum = (1*1)+(2*2)+(3*4)+(4*2)+(5*1) = 30. Mean=3. Median is avg of 5th and 6th (both 3). Mode is 3. Range is 5-1=4.", "ಒಟ್ಟು 10 ಐಟಂಗಳು. ಮೊತ್ತ = 30. ಸರಾಸರಿ = 3. ಮಧ್ಯಾಂಕ (5 ಮತ್ತು 6ನೇ ಮೌಲ್ಯ) = 3. ರೂಢಿಬೆಲೆ = 3. ವ್ಯಾಪ್ತಿ = 5-1 = 4.")

add_multiple(3, "Which of these changes will DEFINITELY change the mean of a data set?", "ದತ್ತಾಂಶದಲ್ಲಿನ ಯಾವ ಬದಲಾವಣೆಗಳು ಖಂಡಿತವಾಗಿಯೂ ಸರಾಸರಿಯನ್ನು ಬದಲಾಯಿಸುತ್ತವೆ?", ["Adding 5 to every observation", "Multiplying every observation by 2 (if mean ≠ 0)", "Removing the mode", "Removing an observation equal to the mean"], ["ಪ್ರತಿಯೊಂದು ವೀಕ್ಷಣೆಗೆ 5 ಅನ್ನು ಸೇರಿಸುವುದು", "ಪ್ರತಿ ವೀಕ್ಷಣೆಯನ್ನು 2 ರಿಂದ ಗುಣಿಸುವುದು (ಸರಾಸರಿ ≠ 0 ಆಗಿದ್ದರೆ)", "ರೂಢಿಬೆಲೆಯನ್ನು ತೆಗೆದುಹಾಕುವುದು", "ಸರಾಸರಿಗೆ ಸಮಾನವಾದ ವೀಕ್ಷಣೆಯನ್ನು ತೆಗೆದುಹಾಕುವುದು"], ["Adding 5 to every observation", "Multiplying every observation by 2 (if mean ≠ 0)"], ["ಪ್ರತಿಯೊಂದು ವೀಕ್ಷಣೆಗೆ 5 ಅನ್ನು ಸೇರಿಸುವುದು", "ಪ್ರತಿ ವೀಕ್ಷಣೆಯನ್ನು 2 ರಿಂದ ಗುಣಿಸುವುದು (ಸರಾಸರಿ ≠ 0 ಆಗಿದ್ದರೆ)"], "Adding a constant increases the mean by that constant. Removing an observation equal to the mean keeps the mean unchanged.", "ಸ್ಥಿರಾಂಕವನ್ನು ಸೇರಿಸುವುದರಿಂದ ಸರಾಸರಿ ಅದೇ ಸ್ಥಿರಾಂಕದಷ್ಟು ಹೆಚ್ಚಾಗುತ್ತದೆ. ಸರಾಸರಿಗೆ ಸಮನಾದ ವೀಕ್ಷಣೆಯನ್ನು ತೆಗೆಯುವುದರಿಂದ ಸರಾಸರಿ ಬದಲಾಗುವುದಿಲ್ಲ.")

add_match(3, "Match the scenario with its probability:", "ಸನ್ನಿವೇಶವನ್ನು ಅದರ ಸಂಭವನೀಯತೆಯೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "Drawing a Queen from a deck of 52 cards", "right": "4/52 (1/13)"}, {"left": "Drawing a Red card from a deck of 52 cards", "right": "26/52 (1/2)"}, {"left": "Rolling a sum of 2 with two dice", "right": "1/36"}, {"left": "Rolling a sum of 7 with two dice", "right": "6/36 (1/6)"}], [{"left": "52 ಇಸ್ಪೀಟ್ ಎಲೆಗಳಿಂದ ರಾಣಿಯನ್ನು ತೆಗೆಯುವುದು", "right": "4/52 (1/13)"}, {"left": "52 ಇಸ್ಪೀಟ್ ಎಲೆಗಳಿಂದ ಕೆಂಪು ಎಲೆಯನ್ನು ತೆಗೆಯುವುದು", "right": "26/52 (1/2)"}, {"left": "ಎರಡು ದಾಳಗಳೊಂದಿಗೆ 2 ರ ಮೊತ್ತವನ್ನು ಪಡೆಯುವುದು", "right": "1/36"}, {"left": "ಎರಡು ದಾಳಗಳೊಂದಿಗೆ 7 ರ ಮೊತ್ತವನ್ನು ಪಡೆಯುವುದು", "right": "6/36 (1/6)"}], "There are 4 Queens and 26 Red cards. Two dice have 36 outcomes.", "4 ರಾಣಿಗಳು ಮತ್ತು 26 ಕೆಂಪು ಕಾರ್ಡ್‌ಗಳಿವೆ. ಎರಡು ದಾಳಗಳು 36 ಫಲಿತಾಂಶಗಳನ್ನು ಹೊಂದಿವೆ.")

add_match(3, "Determine the effect on Mean and Median when an outlier (a very large number) is added to the data:", "ದತ್ತಾಂಶಕ್ಕೆ ಅತಿ ದೊಡ್ಡ ಸಂಖ್ಯೆಯನ್ನು (outlier) ಸೇರಿಸಿದಾಗ ಸರಾಸರಿ ಮತ್ತು ಮಧ್ಯಾಂಕದ ಮೇಲಿನ ಪರಿಣಾಮವನ್ನು ಹೊಂದಿಸಿ:", [{"left": "Mean", "right": "Increases significantly"}, {"left": "Median", "right": "Changes slightly or remains same"}, {"left": "Mode", "right": "Usually remains unchanged"}, {"left": "Range", "right": "Increases significantly"}], [{"left": "ಸರಾಸರಿ", "right": "ಗಮನಾರ್ಹವಾಗಿ ಹೆಚ್ಚಾಗುತ್ತದೆ"}, {"left": "ಮಧ್ಯಾಂಕ", "right": "ಸ್ವಲ್ಪ ಬದಲಾಗುತ್ತದೆ ಅಥವಾ ಹಾಗೆಯೇ ಇರುತ್ತದೆ"}, {"left": "ರೂಢಿಬೆಲೆ", "right": "ಸಾಮಾನ್ಯವಾಗಿ ಬದಲಾಗದೆ ಉಳಿಯುತ್ತದೆ"}, {"left": "ವ್ಯಾಪ್ತಿ", "right": "ಗಮನಾರ್ಹವಾಗಿ ಹೆಚ್ಚಾಗುತ್ತದೆ"}], "The mean is sensitive to extreme values, while the median is robust.", "ಸರಾಸರಿಯು ವಿಪರೀತ ಮೌಲ್ಯಗಳಿಗೆ ಸೂಕ್ಷ್ಮವಾಗಿರುತ್ತದೆ, ಆದರೆ ಮಧ್ಯಾಂಕವು ಬಲವಾಗಿರುತ್ತದೆ.")

add_match(3, "Match the dataset with its Mean:", "ದತ್ತಾಂಶವನ್ನು ಅದರ ಸರಾಸರಿಯೊಂದಿಗೆ ಹೊಂದಿಸಿ:", [{"left": "2, 4, 6, 8, 10", "right": "6"}, {"left": "10, 20, 30", "right": "20"}, {"left": "1, 2, 3, 4, 5, 6, 7", "right": "4"}, {"left": "100, 100, 100", "right": "100"}], [{"left": "2, 4, 6, 8, 10", "right": "6"}, {"left": "10, 20, 30", "right": "20"}, {"left": "1, 2, 3, 4, 5, 6, 7", "right": "4"}, {"left": "100, 100, 100", "right": "100"}], "For a sequence with a constant difference (arithmetic progression), the mean is the middle value.", "ಸ್ಥಿರ ವ್ಯತ್ಯಾಸವನ್ನು ಹೊಂದಿರುವ ಅನುಕ್ರಮಕ್ಕಾಗಿ (ಅಂಕಗಣಿತದ ಪ್ರಗತಿ), ಸರಾಸರಿಯು ಮಧ್ಯಮ ಮೌಲ್ಯವಾಗಿರುತ್ತದೆ.")


with open('/Users/murthy/.gemini/antigravity/scratch/time-tuk-game/src/data/questions/class_7/maths/data_handling.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)
