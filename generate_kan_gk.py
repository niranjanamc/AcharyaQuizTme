import json
import random

def create_json(filename, data_list):
    questions = []
    for idx, (diff, q, ans, opts, reason) in enumerate(data_list):
        random.shuffle(opts)
        questions.append({
            "id": f"{filename.split('.')[0]}_{idx:03d}",
            "difficulty": diff,
            "question": q,
            "options": opts,
            "answer": ans,
            "reasoning": reason
        })
    with open(f'src/data/questions/{filename}', 'w') as f:
        json.dump(questions, f, indent=2)

kannada_data = [
    # Easy (Vocabulary)
    (1, "What does 'ನಾನು' (Naanu) mean in English?", "I", ["You", "He", "I", "We"], "'Naanu' is the first-person singular pronoun in Kannada."),
    (1, "Translate 'Book' to Kannada.", "ಪುಸ್ತಕ (Pustaka)", ["ಮನೆ (Mane)", "ಪುಸ್ತಕ (Pustaka)", "ಶಾಲೆ (Shaale)", "ಪೆನ್ನು (Pen)"], "'Pustaka' is the Kannada word for book."),
    (1, "What does 'ನೀರು' (Neeru) mean?", "Water", ["Milk", "Water", "Fire", "Earth"], "Water is called 'Neeru' in Kannada."),
    (1, "Translate 'Dog' to Kannada.", "ನಾಯಿ (Naayi)", ["ಬೆಕ್ಕು (Bekku)", "ಹಸು (Hasu)", "ನಾಯಿ (Naayi)", "ಪಕ್ಷಿ (Pakshi)"], "'Naayi' is Kannada for dog."),
    (1, "What is the Kannada word for 'House'?", "ಮನೆ (Mane)", ["ಶಾಲೆ (Shaale)", "ಮನೆ (Mane)", "ರಸ್ತೆ (Raste)", "ಮರ (Mara)"], "'Mane' means house or home."),
    (1, "Translate 'School' to Kannada.", "ಶಾಲೆ (Shaale)", ["ಮನೆ (Mane)", "ಶಾಲೆ (Shaale)", "ಊಟ (Oota)", "ಹಣ (Hana)"], "'Shaale' is where you go to study."),
    (1, "What does 'ಒಂದು' (Ondu) mean?", "One", ["Two", "Three", "Four", "One"], "'Ondu' is the number 1 in Kannada."),
    (1, "Translate 'Sun' to Kannada.", "ಸೂರ್ಯ (Soorya)", ["ಚಂದ್ರ (Chandra)", "ಸೂರ್ಯ (Soorya)", "ನಕ್ಷತ್ರ (Nakshatra)", "ಮೋಡ (Moda)"], "'Soorya' means Sun."),
    (1, "What does 'ಹಸು' (Hasu) mean?", "Cow", ["Dog", "Cat", "Cow", "Horse"], "A cow is called 'Hasu'."),
    (1, "Translate 'Tree' to Kannada.", "ಮರ (Mara)", ["ಗಿಡ (Gida)", "ಹೂವು (Hoovu)", "ಮರ (Mara)", "ಹಣ್ಣು (Hannu)"], "'Mara' refers to a tree."),
    (1, "What does 'ಎರಡು' (Eradu) mean?", "Two", ["One", "Two", "Three", "Ten"], "'Eradu' is the number 2."),
    (1, "What is the Kannada word for 'Milk'?", "ಹಾಲು (Haalu)", ["ನೀರು (Neeru)", "ಮಜ್ಜಿಗೆ (Majjige)", "ಹಾಲು (Haalu)", "ಮೊಸರು (Mosaru)"], "'Haalu' is milk."),
    (1, "Translate 'Cat' to Kannada.", "ಬೆಕ್ಕು (Bekku)", ["ನಾಯಿ (Naayi)", "ಇಲಿ (Ili)", "ಬೆಕ್ಕು (Bekku)", "ಮೊಲ (Mola)"], "'Bekku' is the word for a cat."),
    (1, "What does 'ಅಮ್ಮ' (Amma) mean?", "Mother", ["Father", "Sister", "Mother", "Brother"], "'Amma' is a common and affectionate term for mother."),
    (1, "Translate 'Father' to Kannada.", "ಅಪ್ಪ (Appa)", ["ಅಜ್ಜ (Ajja)", "ಅಪ್ಪ (Appa)", "ಅಣ್ಣ (Anna)", "ತಮ್ಮ (Thamma)"], "'Appa' is father in Kannada."),
    (1, "What is 'Food' in Kannada?", "ಊಟ (Oota)", ["ನೀರು (Neeru)", "ಹಣ್ಣು (Hannu)", "ಊಟ (Oota)", "ಹಾಲು (Haalu)"], "'Oota' generally refers to a meal or food."),
    (1, "What does 'ಮೂರು' (Mooru) mean?", "Three", ["Two", "Four", "Five", "Three"], "'Mooru' is the number 3."),

    # Medium (Simple phrases)
    (2, "How do you say 'How are you?' in Kannada?", "ಹೇಗಿದ್ದೀರಾ? (Hegiddira?)", ["ಏನು ಸಮಾಚಾರ? (Enu Samachara?)", "ಹೇಗಿದ್ದೀರಾ? (Hegiddira?)", "ಎಲ್ಲಿರುವಿರಿ? (Elliruviri?)", "ಯಾರು ನೀವು? (Yaaru Neevu?)"], "'Hegiddira?' is a polite way to ask how someone is doing."),
    (2, "Translate 'Come here' to Kannada.", "ಇಲ್ಲಿ ಬಾ (Illi Baa)", ["ಅಲ್ಲಿ ಹೋಗು (Alli Hogu)", "ಇಲ್ಲಿ ಬಾ (Illi Baa)", "ಕುಳಿತುಕೋ (Kulithuko)", "ನಿಲ್ಲು (Nillu)"], "Illi = Here, Baa = Come."),
    (2, "What does 'ನನ್ನ ಹೆಸರು' (Nanna hesaru) mean?", "My name is", ["His name is", "Your name is", "My name is", "Her name is"], "Nanna = My, Hesaru = Name."),
    (2, "Translate 'Good morning' to Kannada.", "ಶುಭೋದಯ (Shubhodaya)", ["ಶುಭ ರಾತ್ರಿ (Shubha Rathri)", "ಶುಭ ಸಂಜೆ (Shubha Sanje)", "ಶುಭೋದಯ (Shubhodaya)", "ನಮಸ್ಕಾರ (Namaskara)"], "Shubha = Good/Auspicious, Udaya = Morning/Rise."),
    (2, "What does 'ಊಟ ಆಯ್ತಾ?' (Oota aaytha?) mean?", "Did you have food?", ["What did you eat?", "Are you hungry?", "Did you have food?", "Where is the food?"], "A common casual greeting asking if you've eaten."),
    (2, "Translate 'I am going' to Kannada.", "ನಾನು ಹೋಗುತ್ತಿದ್ದೇನೆ (Naanu hoguttiddene)", ["ಅವನು ಹೋಗುತ್ತಿದ್ದಾನೆ (Avanu hoguttiddane)", "ನಾನು ಬರುತ್ತಿದ್ದೇನೆ (Naanu baruttiddene)", "ನಾನು ಹೋಗುತ್ತಿದ್ದೇನೆ (Naanu hoguttiddene)", "ನೀನು ಹೋಗು (Neenu hogu)"], "Naanu = I, Hoguttiddene = Am going."),
    (2, "What does 'ತುಂಬಾ ಧನ್ಯವಾದಗಳು' (Tumba Dhanyavadagalu) mean?", "Thank you very much", ["Sorry", "Please", "Thank you very much", "Welcome"], "Tumba = Very much/A lot, Dhanyavadagalu = Thanks."),
    (2, "Translate 'What is this?' to Kannada.", "ಇದು ಏನು? (Idu enu?)", ["ಅದು ಏನು? (Adu enu?)", "ಯಾರು ಅವರು? (Yaaru avaru?)", "ಇದು ಏನು? (Idu enu?)", "ಹೇಗೆ? (Hege?)"], "Idu = This, Enu = What."),
    (2, "What does 'ನನಗೆ ಗೊತ್ತಿಲ್ಲ' (Nanage gottilla) mean?", "I don't know", ["I know", "You don't know", "I don't know", "Tell me"], "Nanage = To me, Gottilla = Not known."),
    (2, "Translate 'Please sit' to Kannada (polite).", "ದಯವಿಟ್ಟು ಕುಳಿತುಕೊಳ್ಳಿ (Dayavittu kulithukolli)", ["ಬನ್ನಿ (Banni)", "ಹೋಗಿ (Hogi)", "ದಯವಿಟ್ಟು ಕುಳಿತುಕೊಳ್ಳಿ (Dayavittu kulithukolli)", "ನಿಲ್ಲು (Nillu)"], "Dayavittu = Please, Kulithukolli = Sit (respectful)."),
    (2, "What does 'ಬೇಗ ಬನ್ನಿ' (Bega banni) mean?", "Come quickly", ["Go slowly", "Come quickly", "Wait here", "Listen carefully"], "Bega = Fast/Quickly, Banni = Come (polite/plural)."),
    (2, "How do you say 'Yes' in Kannada?", "ಹೌದು (Houdu)", ["ಇಲ್ಲ (Illa)", "ಹೌದು (Houdu)", "ಯಾಕೆ (Yaake)", "ಹೇಗೆ (Hege)"], "'Houdu' is the standard word for Yes."),
    (2, "How do you say 'No' in Kannada?", "ಇಲ್ಲ (Illa)", ["ಹೌದು (Houdu)", "ಇಲ್ಲ (Illa)", "ಸರಿ (Sari)", "ಆಗಲಿ (Aagali)"], "'Illa' is used for No or Not there."),
    (2, "What does 'ಸರಿ' (Sari) mean?", "Okay / Right", ["Wrong", "Okay / Right", "Fast", "Slow"], "Sari is used frequently to mean Okay, alright, or correct."),
    (2, "Translate 'Water, please' to Kannada.", "ದಯವಿಟ್ಟು ನೀರು ಕೊಡಿ (Dayavittu neeru kodi)", ["ಊಟ ಕೊಡಿ (Oota kodi)", "ದಯವಿಟ್ಟು ನೀರು ಕೊಡಿ (Dayavittu neeru kodi)", "ನೀರು ಬೇಕು (Neeru beku)", "ಹಾಲು ಕೊಡಿ (Haalu kodi)"], "Neeru = Water, Kodi = Give (polite)."),
    (2, "What does 'ಯಾಕೆ?' (Yaake) mean?", "Why?", ["When?", "Where?", "Why?", "Who?"], "Yaake is the question word for Why."),
    (2, "What does 'ಎಲ್ಲಿ?' (Elli) mean?", "Where?", ["Why?", "How?", "Where?", "What?"], "Elli is the question word for Where."),

    # Hard (Grammar and complex words)
    (3, "Translate 'Tomorrow I will go to school' to Kannada.", "ನಾಳೆ ನಾನು ಶಾಲೆಗೆ ಹೋಗುತ್ತೇನೆ (Naale naanu shaalege hoguttene)", ["ನಿನ್ನೆ ನಾನು ಶಾಲೆಗೆ ಹೋದೆ (Ninne naanu shaalege hode)", "ಇಂದು ನಾನು ಶಾಲೆಯಲ್ಲಿ ಇದ್ದೇನೆ (Indu naanu shaleyalli iddene)", "ನಾಳೆ ನಾನು ಶಾಲೆಗೆ ಹೋಗುತ್ತೇನೆ (Naale naanu shaalege hoguttene)", "ನಾನು ಶಾಲೆಗೆ ಹೋಗಬೇಕು (Naanu shaalege hogabeku)"], "Naale = Tomorrow, Hoguttene = Will go (Future tense, 1st person)."),
    (3, "What does 'ಅವನು ಮರ ಹತ್ತುತ್ತಿದ್ದಾನೆ' (Avanu mara hattuttiddane) mean?", "He is climbing the tree", ["She is climbing the tree", "He is cutting the tree", "He is climbing the tree", "The bird is on the tree"], "Avanu = He, Mara = Tree, Hattuttiddane = Is climbing."),
    (3, "Identify the plural of 'ಪುಸ್ತಕ' (Pustaka).", "ಪುಸ್ತಕಗಳು (Pustakagalu)", ["ಪುಸ್ತಕಿ (Pustaki)", "ಪುಸ್ತಕಗಳು (Pustakagalu)", "ಪುಸ್ತಕರು (Pustakaru)", "ಪುಸ್ತಕದ (Pustakada)"], "Adding '-galu' makes non-living nouns plural in Kannada."),
    (3, "Translate 'He read the book' to Kannada.", "ಅವನು ಪುಸ್ತಕವನ್ನು ಓದಿದನು (Avanu pustakavannu odidanu)", ["ನಾನು ಪುಸ್ತಕ ಓದಿದೆ (Naanu pustaka odide)", "ಅವಳು ಪುಸ್ತಕ ಓದುತ್ತಿದ್ದಾಳೆ (Avalu pustaka oduttiddale)", "ಅವನು ಪುಸ್ತಕವನ್ನು ಓದಿದನು (Avanu pustakavannu odidanu)", "ಅವರು ಪುಸ್ತಕ ಓದುತ್ತಾರೆ (Avaru pustaka oduttare)"], "Odidanu indicates past tense for a 3rd person singular male."),
    (3, "What is the opposite of 'ದೊಡ್ಡ' (Dodda - Big)?", "ಸಣ್ಣ (Sanna - Small)", ["ಎತ್ತರ (Ettara - Tall)", "ಸಣ್ಣ (Sanna - Small)", "ದಪ್ಪ (Dappa - Fat)", "ಹೊಸ (Hosa - New)"], "Sanna (or Chikka) is the antonym of Dodda."),
    (3, "What is the meaning of the proverb: 'ಕೈ ಕೆಸರಾದರೆ ಬಾಯಿ ಮೊಸರು'?", "Hard work yields good results", ["Don't cry over spilled milk", "Hard work yields good results", "As you sow, so you reap", "Barking dogs seldom bite"], "Literally: If the hands get muddy, the mouth gets curds. It means hard work brings rewards."),
    (3, "Identify the correct tense: 'ಅವರು ನಾಳೆ ಬರುತ್ತಾರೆ' (Avaru naale baruttare)", "Future Tense", ["Past Tense", "Present Tense", "Future Tense", "Continuous Tense"], "Baruttare (Will come) combined with Naale (Tomorrow) indicates the future."),
    (3, "What does 'ಮಳೆ ಬರುತ್ತಿದೆ' (Male baruttide) mean?", "It is raining", ["It is sunny", "It will rain tomorrow", "It is raining", "The wind is blowing"], "Male = Rain, Baruttide = Is coming."),
    (3, "Translate 'What is the price of this?' to Kannada.", "ಇದರ ಬೆಲೆ ಎಷ್ಟು? (Idara bele eshtu?)", ["ಇದು ಎಷ್ಟು ದೂರ? (Idu eshtu doora?)", "ಇದರ ಬೆಲೆ ಎಷ್ಟು? (Idara bele eshtu?)", "ಇದು ಯಾಕೆ? (Idu yaake?)", "ಇದರ ಹೆಸರೇನು? (Idara hesarenu?)"], "Bele = Price/Cost, Eshtu = How much."),
    (3, "What is the opposite of 'ಹೊಸ' (Hosa - New)?", "ಹಳೆ (Hale - Old)", ["ಕಪ್ಪು (Kappu - Black)", "ಕೆಟ್ಟ (Ketta - Bad)", "ಹಳೆ (Hale - Old)", "ದೂರ (Doora - Far)"], "Hale refers to something old (not living things)."),
    (3, "Translate 'I like to play' to Kannada.", "ನನಗೆ ಆಟವಾಡಲು ಇಷ್ಟ (Nanage aatavaadalu ishta)", ["ನಾನು ಆಟವಾಡುತ್ತೇನೆ (Naanu aatavaaduttene)", "ಅವನಿಗೆ ಆಟ ಇಷ್ಟ (Avanige aata ishta)", "ನನಗೆ ಆಟವಾಡಲು ಇಷ್ಟ (Nanage aatavaadalu ishta)", "ನಾವು ಆಡೋಣ (Naavu aadona)"], "Nanage = To me, Ishta = Like/Favorite."),
    (3, "What does 'ಬೆಳಗ್ಗೆಯಿಂದ ಸಾಯಂಕಾಲದವರೆಗೆ' mean?", "From morning to evening", ["From night to morning", "From morning to evening", "Today and tomorrow", "Always"], "Belagge = Morning, -yinda = from, Saayankaala = Evening, -davarege = until."),
    (3, "What is the Kannada word for 'Library'?", "ಗ್ರಂಥಾಲಯ (Granthalaya)", ["ವಿದ್ಯಾಲಯ (Vidyalaya)", "ಕಾರ್ಯಾಲಯ (Karyalaya)", "ಗ್ರಂಥಾಲಯ (Granthalaya)", "ದೇವಾಲಯ (Devalaya)"], "Grantha = Book/Tome, Alaya = Place/House."),
    (3, "Which of these is a questioning word (Wh- word) in Kannada?", "ಯಾರು (Yaaru - Who)", ["ನಾನು (Naanu - I)", "ಯಾರು (Yaaru - Who)", "ಅವರು (Avaru - They)", "ಇದು (Idu - This)"], "Words starting with 'Ya' or 'E' are often question words in Kannada."),
    (3, "Translate 'I want to eat an apple' to Kannada.", "ನಾನು ಸೇಬು ತಿನ್ನಬೇಕು (Naanu sebu tinnabeku)", ["ನಾನು ಹಣ್ಣು ತಿಂದೆ (Naanu hannu tinde)", "ಅವನು ಸೇಬು ತಿಂದನು (Avanu sebu tindanu)", "ನಾನು ಸೇಬು ತಿನ್ನಬೇಕು (Naanu sebu tinnabeku)", "ನನಗೆ ಸೇಬು ಇಷ್ಟ (Nanage sebu ishta)"], "Sebu = Apple, Tinnabeku = Must/Want to eat."),
    (3, "Identify the grammatical error: 'ನಾನು ಹೋದೆನು' vs 'ನಾನು ಹೋದನು'", "ಹೋದನು is for 'He' (Avanu)", ["ಹೋದನು is for 'He' (Avanu)", "ಹೋದೆನು is future tense", "Both are correct", "ಹೋದನು is plural"], "The verb ending must match the subject. Naanu (I) takes -denu. Avanu (He) takes -danu.")
]

gk_data = [
    # Easy
    (1, "Which is the tallest mountain in the world?", "Mount Everest", ["K2", "Mount Everest", "Mount Kilimanjaro", "Mount Fuji"], "Mount Everest is the highest peak above sea level."),
    (1, "How many continents are there on Earth?", "Seven", ["Five", "Six", "Seven", "Eight"], "The 7 continents are Asia, Africa, North America, South America, Antarctica, Europe, and Australia."),
    (1, "Which is the largest ocean?", "Pacific Ocean", ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "The Pacific Ocean covers more than 30% of the Earth's surface."),
    (1, "What is the fastest land animal?", "Cheetah", ["Lion", "Cheetah", "Horse", "Leopard"], "Cheetahs can run at speeds up to 120 km/h (75 mph)."),
    (1, "How many colors are there in a rainbow?", "Seven", ["Five", "Six", "Seven", "Eight"], "The colors spell out ROYGBIV (Red, Orange, Yellow, Green, Blue, Indigo, Violet)."),
    (1, "Which is the largest mammal?", "Blue Whale", ["Elephant", "Giraffe", "Blue Whale", "Shark"], "The Blue Whale is the largest animal known to have ever lived."),
    (1, "What do you call a baby dog?", "Puppy", ["Kitten", "Calf", "Cub", "Puppy"], "A baby dog is a puppy."),
    (1, "Which month has the fewest days?", "February", ["January", "February", "April", "November"], "February usually has 28 days, and 29 in a leap year."),
    (1, "What is the main language spoken in India?", "Hindi", ["English", "Hindi", "Bengali", "Telugu"], "While India has many languages, Hindi is the most widely spoken."),
    (1, "How many hours are in a day?", "24", ["12", "20", "24", "48"], "The Earth takes 24 hours to complete one rotation on its axis."),
    (1, "Which festival is known as the festival of colors?", "Holi", ["Diwali", "Holi", "Eid", "Christmas"], "Holi is celebrated by throwing colored powders and water."),
    (1, "What is the freezing point of water in Celsius?", "0 degrees", ["100 degrees", "50 degrees", "0 degrees", "-10 degrees"], "Water turns to ice at 0°C."),
    (1, "Which planet do we live on?", "Earth", ["Mars", "Venus", "Earth", "Jupiter"], "Earth is the third planet from the sun."),
    (1, "How many days are in a leap year?", "366", ["365", "366", "364", "360"], "A leap year adds one extra day in February."),
    (1, "Which bird cannot fly but can run very fast?", "Ostrich", ["Penguin", "Ostrich", "Eagle", "Kiwi"], "The ostrich is a large flightless bird from Africa."),
    (1, "What is the capital of Karnataka?", "Bengaluru", ["Mysuru", "Bengaluru", "Mangaluru", "Hubballi"], "Bengaluru (Bangalore) is the capital city of Karnataka."),
    (1, "What shape has three sides?", "Triangle", ["Square", "Circle", "Triangle", "Rectangle"], "A triangle is a polygon with three edges and three vertices."),

    # Medium
    (2, "Who invented the telephone?", "Alexander Graham Bell", ["Thomas Edison", "Nikola Tesla", "Alexander Graham Bell", "Albert Einstein"], "Bell was awarded the first US patent for the telephone in 1876."),
    (2, "Which country has the largest population?", "India", ["China", "India", "USA", "Russia"], "As of recent years, India has surpassed China to become the most populous country."),
    (2, "What is the currency of Japan?", "Yen", ["Yuan", "Won", "Yen", "Rupee"], "The Japanese Yen (JPY) is the official currency."),
    (2, "Which is the longest river in the world?", "The Nile", ["Amazon", "Yangtze", "The Nile", "Mississippi"], "The Nile in Africa is traditionally considered the longest river."),
    (2, "Who painted the Mona Lisa?", "Leonardo da Vinci", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"], "Da Vinci painted it during the Italian Renaissance."),
    (2, "What is the hardest rock?", "Diamond", ["Granite", "Marble", "Diamond", "Quartz"], "Diamonds score a 10 on the Mohs scale of hardness."),
    (2, "In which sport do you hit a shuttlecock?", "Badminton", ["Tennis", "Table Tennis", "Squash", "Badminton"], "Badminton is played using rackets to hit a shuttlecock across a net."),
    (2, "What is the capital of Australia?", "Canberra", ["Sydney", "Melbourne", "Canberra", "Perth"], "Canberra was chosen as a compromise between Sydney and Melbourne."),
    (2, "Who was the first person to step on the Moon?", "Neil Armstrong", ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "John Glenn"], "Armstrong walked on the moon during the Apollo 11 mission in 1969."),
    (2, "Which planet has the most visible rings?", "Saturn", ["Jupiter", "Saturn", "Uranus", "Neptune"], "Saturn's rings are made mostly of ice particles and rocky debris."),
    (2, "What is the largest desert in the world?", "Sahara", ["Gobi", "Kalahari", "Sahara", "Atacama"], "The Sahara is the largest hot desert, covering much of North Africa."),
    (2, "Who wrote 'Romeo and Juliet'?", "William Shakespeare", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "Shakespeare is a famous English playwright."),
    (2, "Which organ is responsible for purifying blood?", "Kidneys", ["Heart", "Lungs", "Kidneys", "Liver"], "The kidneys filter waste products from the blood."),
    (2, "What is the national game of India?", "Field Hockey", ["Cricket", "Football", "Field Hockey", "Kabaddi"], "India dominated field hockey in the early Olympic games."),
    (2, "What does HTTP stand for in website addresses?", "HyperText Transfer Protocol", ["HyperText Transfer Protocol", "HighText Transfer Process", "HyperTech Transfer Protocol", "HyperText Transmission Process"], "HTTP is the foundation of data communication for the World Wide Web."),
    (2, "Which gas do plants absorb from the atmosphere?", "Carbon Dioxide", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "Plants absorb CO2 for photosynthesis."),
    (2, "What is the national tree of India?", "Banyan Tree", ["Mango Tree", "Banyan Tree", "Peepal Tree", "Neem Tree"], "The Banyan tree represents eternal life due to its ever-expanding branches."),

    # Hard
    (3, "Who discovered Penicillin?", "Alexander Fleming", ["Louis Pasteur", "Alexander Fleming", "Marie Curie", "Isaac Newton"], "Fleming discovered the first antibiotic, penicillin, in 1928."),
    (3, "Which is the smallest country in the world?", "Vatican City", ["Monaco", "Nauru", "Vatican City", "San Marino"], "Vatican City is an independent city-state enclaved within Rome, Italy."),
    (3, "What is the chemical symbol for Iron?", "Fe", ["Ir", "Fe", "In", "I"], "The symbol 'Fe' comes from the Latin word 'ferrum'."),
    (3, "Who is known as the 'Missile Man of India'?", "A.P.J. Abdul Kalam", ["Homi Bhabha", "Vikram Sarabhai", "A.P.J. Abdul Kalam", "Satish Dhawan"], "Dr. Kalam was pivotal in India's civilian space and military missile programs."),
    (3, "Which ocean lies on the east coast of the United States?", "Atlantic Ocean", ["Pacific Ocean", "Indian Ocean", "Arctic Ocean", "Atlantic Ocean"], "The Atlantic separates the Americas from Europe and Africa."),
    (3, "What is the capital of Canada?", "Ottawa", ["Toronto", "Vancouver", "Montreal", "Ottawa"], "Ottawa is located in the province of Ontario."),
    (3, "Who developed the theory of relativity?", "Albert Einstein", ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Niels Bohr"], "Einstein's theory revolutionized modern physics (E=mc^2)."),
    (3, "Which continent is known as the 'Dark Continent'?", "Africa", ["Asia", "South America", "Africa", "Antarctica"], "It was historically called this because its interior was largely unknown to Europeans."),
    (3, "What is the currency of the United Kingdom?", "Pound Sterling", ["Euro", "Dollar", "Pound Sterling", "Franc"], "The Pound Sterling (£) is one of the oldest currencies still in use."),
    (3, "What is the deepest part of the world's oceans?", "Mariana Trench", ["Puerto Rico Trench", "Mariana Trench", "Java Trench", "Tonga Trench"], "The Mariana Trench reaches a depth of about 11,000 meters."),
    (3, "Who wrote the Indian national song 'Vande Mataram'?", "Bankim Chandra Chatterjee", ["Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Subhas Chandra Bose"], "It was featured in his novel 'Anandamath'."),
    (3, "Which planet rotates on its side?", "Uranus", ["Venus", "Neptune", "Uranus", "Saturn"], "Uranus has an axial tilt of 98 degrees, making it look like it's rolling."),
    (3, "What is the study of fossils called?", "Paleontology", ["Archaeology", "Geology", "Paleontology", "Anthropology"], "Paleontologists study fossils to understand the history of life on Earth."),
    (3, "What is the fear of heights called?", "Acrophobia", ["Arachnophobia", "Claustrophobia", "Acrophobia", "Hydrophobia"], "Acrophobia is an extreme or irrational fear of heights."),
    (3, "Who was the first woman in space?", "Valentina Tereshkova", ["Sally Ride", "Valentina Tereshkova", "Mae Jemison", "Kalpana Chawla"], "She flew aboard Vostok 6 in 1963."),
    (3, "Which element makes up diamonds and graphite?", "Carbon", ["Silicon", "Oxygen", "Carbon", "Calcium"], "Different structural arrangements of carbon atoms create diamonds or graphite.")
]

create_json('kannada.json', kannada_data)
create_json('gk.json', gk_data)

print("Generated kannada.json and gk.json")
