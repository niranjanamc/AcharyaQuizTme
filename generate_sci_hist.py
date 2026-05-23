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

science_data = [
    # Easy
    (1, "What gas do humans breathe in to survive?", "Oxygen", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "Our bodies need oxygen from the air to create energy."),
    (1, "What is the center of our solar system?", "The Sun", ["Earth", "The Sun", "The Moon", "Jupiter"], "The Sun is a star at the center, and all planets orbit around it."),
    (1, "Which of these is a liquid?", "Water", ["Ice", "Water", "Steam", "Wood"], "Water flows and takes the shape of its container, making it a liquid."),
    (1, "What do bees collect from flowers?", "Nectar", ["Leaves", "Nectar", "Roots", "Branches"], "Bees drink nectar and turn it into honey in their hives."),
    (1, "What part of the plant holds it in the soil?", "Roots", ["Stem", "Leaves", "Roots", "Flowers"], "Roots anchor the plant and absorb water and nutrients from the soil."),
    (1, "What is the Earth's only natural satellite?", "The Moon", ["The Sun", "The Moon", "Mars", "Venus"], "The Moon orbits the Earth and is our only natural satellite."),
    (1, "Which animal is known as the King of the Jungle?", "Lion", ["Elephant", "Lion", "Tiger", "Bear"], "Lions are often called the King of the Jungle due to their strength and mane."),
    (1, "What color are most leaves in summer?", "Green", ["Red", "Yellow", "Green", "Brown"], "Leaves are green because of chlorophyll, which helps them make food."),
    (1, "How many legs does a spider have?", "Eight", ["Six", "Eight", "Ten", "Four"], "Spiders are arachnids, meaning they have eight legs."),
    (1, "What boils at 100 degrees Celsius?", "Water", ["Milk", "Water", "Juice", "Oil"], "Water reaches its boiling point at 100°C (212°F)."),
    (1, "What shape is the Earth?", "Sphere", ["Flat", "Square", "Sphere", "Triangle"], "The Earth is roughly a sphere, like a giant ball."),
    (1, "What gives us light during the day?", "The Sun", ["The Moon", "Stars", "The Sun", "Fire"], "The Sun is our closest star and provides daylight."),
    (1, "Which sense do you use your eyes for?", "Sight", ["Smell", "Touch", "Sight", "Hearing"], "Eyes detect light and allow us to see the world."),
    (1, "What do we call frozen water?", "Ice", ["Steam", "Cloud", "Ice", "Rain"], "When water gets very cold, it freezes into solid ice."),
    (1, "Which animal gives us milk?", "Cow", ["Dog", "Cow", "Hen", "Horse"], "Cows are farm animals that produce milk for us to drink."),
    (1, "What type of animal is a frog?", "Amphibian", ["Reptile", "Mammal", "Amphibian", "Bird"], "Frogs live both in water and on land, making them amphibians."),
    (1, "What is the main source of energy for the Earth?", "The Sun", ["Wind", "Water", "The Sun", "Coal"], "Almost all energy on Earth ultimately comes from the Sun."),
    
    # Medium
    (2, "What is the process by which plants make their food?", "Photosynthesis", ["Respiration", "Photosynthesis", "Digestion", "Absorption"], "Plants use sunlight, water, and CO2 to create food in a process called photosynthesis."),
    (2, "Which planet is known as the Red Planet?", "Mars", ["Venus", "Mars", "Jupiter", "Saturn"], "Mars appears red due to iron oxide (rust) on its surface."),
    (2, "What is the hardest natural substance on Earth?", "Diamond", ["Gold", "Iron", "Diamond", "Quartz"], "Diamonds are formed under extreme heat and pressure, making them the hardest natural mineral."),
    (2, "What force keeps us on the ground?", "Gravity", ["Magnetism", "Friction", "Gravity", "Inertia"], "Gravity is the invisible force that pulls objects toward each other."),
    (2, "How many bones are in the adult human body?", "206", ["206", "108", "300", "150"], "While babies have around 300 bones, they fuse together to form 206 bones in adults."),
    (2, "What gas makes up most of the Earth's atmosphere?", "Nitrogen", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "The air is about 78% Nitrogen and 21% Oxygen."),
    (2, "What is the boiling point of water in Fahrenheit?", "212", ["100", "212", "32", "150"], "Water boils at 212°F (or 100°C)."),
    (2, "Which organ pumps blood through the body?", "Heart", ["Lungs", "Brain", "Heart", "Liver"], "The heart is a muscle that continuously pumps blood to all parts of your body."),
    (2, "What do caterpillars turn into?", "Butterflies", ["Bees", "Butterflies", "Beetles", "Spiders"], "Caterpillars undergo metamorphosis in a chrysalis to become butterflies."),
    (2, "What part of the plant conducts photosynthesis?", "Leaf", ["Root", "Stem", "Leaf", "Flower"], "Leaves contain chlorophyll which absorbs sunlight to make food."),
    (2, "What is a group of stars forming a pattern called?", "Constellation", ["Galaxy", "Solar System", "Constellation", "Asteroid"], "Constellations are imaginary patterns of stars, like the Big Dipper."),
    (2, "What energy comes from moving water?", "Hydroelectric", ["Solar", "Geothermal", "Hydroelectric", "Wind"], "Hydroelectric power uses the force of flowing water to generate electricity."),
    (2, "Which type of animal has feathers?", "Bird", ["Mammal", "Reptile", "Bird", "Amphibian"], "Birds are the only animals that have feathers."),
    (2, "What is the primary gas found in the sun?", "Hydrogen", ["Oxygen", "Helium", "Hydrogen", "Carbon"], "The sun is mostly made of hydrogen, which it fuses into helium."),
    (2, "What is it called when birds move to warmer climates in winter?", "Migration", ["Hibernation", "Migration", "Evolution", "Adaptation"], "Migration is the seasonal movement of animals from one region to another."),
    (2, "What is the colored part of the eye called?", "Iris", ["Pupil", "Cornea", "Iris", "Retina"], "The iris controls the size of the pupil to let light in."),
    (2, "What instrument is used to see very tiny objects?", "Microscope", ["Telescope", "Microscope", "Periscope", "Stethoscope"], "Microscopes use lenses to magnify tiny things like cells."),
    
    # Hard
    (3, "What is the chemical symbol for Gold?", "Au", ["Ag", "Au", "Gd", "Go"], "The symbol 'Au' comes from the Latin word 'aurum', meaning shining dawn."),
    (3, "Which blood cells fight infection?", "White blood cells", ["Red blood cells", "White blood cells", "Platelets", "Plasma"], "White blood cells are the immune system's defense against disease."),
    (3, "What is the largest planet in our solar system?", "Jupiter", ["Saturn", "Jupiter", "Neptune", "Earth"], "Jupiter is a gas giant and the largest planet in the solar system."),
    (3, "What is the main component of a plant cell wall?", "Cellulose", ["Protein", "Lipid", "Cellulose", "Starch"], "Cellulose provides structural support and rigidity to plant cells."),
    (3, "What force opposes motion between two surfaces?", "Friction", ["Gravity", "Inertia", "Friction", "Tension"], "Friction is the resistance that one surface or object encounters when moving over another."),
    (3, "Which planet has the most moons?", "Saturn", ["Jupiter", "Saturn", "Uranus", "Neptune"], "Saturn has over 140 discovered moons, surpassing Jupiter."),
    (3, "What is the study of weather called?", "Meteorology", ["Geology", "Meteorology", "Astronomy", "Ecology"], "Meteorology focuses on weather processes and forecasting."),
    (3, "Which element has the atomic number 1?", "Hydrogen", ["Oxygen", "Carbon", "Helium", "Hydrogen"], "Hydrogen is the lightest and most abundant element in the universe."),
    (3, "What process involves turning a liquid into a gas?", "Evaporation", ["Condensation", "Sublimation", "Evaporation", "Melting"], "Evaporation happens when liquid is heated and turns into vapor."),
    (3, "Which vitamin is produced when a person is exposed to sunlight?", "Vitamin D", ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin B"], "The skin synthesizes Vitamin D when exposed to UVB rays from the sun."),
    (3, "What is the outer layer of the Earth called?", "Crust", ["Mantle", "Core", "Crust", "Magma"], "The crust is the solid, outermost shell of the Earth."),
    (3, "What is the name of the galaxy we live in?", "Milky Way", ["Andromeda", "Milky Way", "Whirlpool", "Sombrero"], "Our solar system is located in the Milky Way galaxy."),
    (3, "What part of the brain controls balance?", "Cerebellum", ["Cerebrum", "Cerebellum", "Brainstem", "Thalamus"], "The cerebellum helps coordinate voluntary movements and maintain balance."),
    (3, "What is the speed of light?", "300,000 km/s", ["150,000 km/s", "300,000 km/s", "1,000 km/s", "3,000,000 km/s"], "Light travels at roughly 300,000 kilometers per second in a vacuum."),
    (3, "Which gas is responsible for the fizz in soda?", "Carbon Dioxide", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"], "Carbon dioxide is dissolved under pressure to create the bubbles in carbonated drinks."),
    (3, "What type of rock is formed from cooled magma?", "Igneous", ["Sedimentary", "Metamorphic", "Igneous", "Fossil"], "Igneous rocks form when hot, molten rock crystallizes and solidifies.")
]

history_data = [
    # Easy
    (1, "Who is known as the Father of the Nation in India?", "Mahatma Gandhi", ["Jawaharlal Nehru", "Mahatma Gandhi", "Subhas Chandra Bose", "Bhagat Singh"], "Mahatma Gandhi led the peaceful struggle for India's independence."),
    (1, "What colors are in the Indian National Flag?", "Saffron, White, Green", ["Red, White, Blue", "Saffron, White, Green", "Green, Yellow, Red", "Blue, White, Orange"], "The flag has three horizontal bands of Saffron, White, and Green with a blue wheel."),
    (1, "Which festival is known as the festival of lights?", "Diwali", ["Holi", "Diwali", "Eid", "Christmas"], "Diwali celebrates the victory of light over darkness."),
    (1, "Who was the first Prime Minister of India?", "Jawaharlal Nehru", ["Mahatma Gandhi", "Sardar Patel", "Jawaharlal Nehru", "B.R. Ambedkar"], "Nehru served as the first Prime Minister from 1947 until 1964."),
    (1, "Which monument was built by Shah Jahan for his wife?", "Taj Mahal", ["Red Fort", "Taj Mahal", "Qutub Minar", "Hawa Mahal"], "The Taj Mahal is a famous white marble mausoleum in Agra."),
    (1, "In which city is the Red Fort located?", "Delhi", ["Agra", "Mumbai", "Delhi", "Jaipur"], "The Red Fort is a historic fort in the capital city of Delhi."),
    (1, "What did early humans use to make tools?", "Stones", ["Iron", "Plastic", "Stones", "Glass"], "Early humans made simple tools by chipping stones."),
    (1, "Who wrote the Indian National Anthem 'Jana Gana Mana'?", "Rabindranath Tagore", ["Bankim Chandra", "Rabindranath Tagore", "Sarojini Naidu", "Premchand"], "Tagore was a famous poet who also won a Nobel Prize."),
    (1, "What is the capital of India?", "New Delhi", ["Mumbai", "Kolkata", "New Delhi", "Chennai"], "New Delhi has been the capital of India since 1911."),
    (1, "Which famous leader was called 'Chacha' by children?", "Jawaharlal Nehru", ["Gandhi", "Nehru", "Patel", "Bose"], "Nehru was fond of children and his birthday is celebrated as Children's Day."),
    (1, "What was the main occupation of early civilized humans?", "Farming", ["Software", "Farming", "Flying", "Mining"], "Agriculture allowed humans to settle in one place and build civilizations."),
    (1, "Which bird is the national bird of India?", "Peacock", ["Eagle", "Peacock", "Parrot", "Pigeon"], "The peacock is known for its beautiful, colorful tail feathers."),
    (1, "What animal is the national animal of India?", "Tiger", ["Lion", "Elephant", "Tiger", "Leopard"], "The Bengal Tiger represents strength and agility."),
    (1, "Which wheel is at the center of the Indian flag?", "Ashoka Chakra", ["Dharma Chakra", "Ashoka Chakra", "Sudarshan Chakra", "Time Chakra"], "The blue Ashoka Chakra has 24 spokes representing continuous progress."),
    (1, "Which day is celebrated as Independence Day in India?", "August 15", ["January 26", "August 15", "October 2", "November 14"], "India gained independence from British rule on August 15, 1947."),
    (1, "What did people live in before houses were built?", "Caves", ["Tents", "Caves", "Trees", "Boats"], "Early humans sought shelter in natural caves to protect themselves."),
    (1, "Which famous king ruled the Mauryan Empire and later embraced peace?", "Ashoka", ["Akbar", "Ashoka", "Shivaji", "Babar"], "Ashoka the Great gave up war after the Battle of Kalinga."),

    # Medium
    (2, "Who was the founder of the Maurya Empire?", "Chandragupta Maurya", ["Ashoka", "Chandragupta Maurya", "Bindusara", "Harsha"], "Chandragupta Maurya built one of the largest empires on the Indian subcontinent."),
    (2, "Which empire was ruled by Krishnadevaraya?", "Vijayanagara", ["Chola", "Mughal", "Vijayanagara", "Gupta"], "The Vijayanagara Empire was famous for its rich culture and architecture in Hampi."),
    (2, "Who is known as the Iron Man of India?", "Sardar Vallabhbhai Patel", ["Bhagat Singh", "Sardar Vallabhbhai Patel", "Subhas Chandra Bose", "Lala Lajpat Rai"], "He integrated over 500 princely states into the Indian Union."),
    (2, "What was the capital of the Chola Dynasty?", "Thanjavur", ["Madurai", "Thanjavur", "Kanchipuram", "Hampi"], "Thanjavur was the center of Chola power and culture in South India."),
    (2, "Which ancient civilization was built around the Indus River?", "Harappan Civilization", ["Mesopotamian", "Harappan Civilization", "Egyptian", "Maya"], "Also known as the Indus Valley Civilization, it was known for planned cities."),
    (2, "Who wrote the ancient Indian epic, the Mahabharata?", "Sage Vyasa", ["Valmiki", "Sage Vyasa", "Kalidasa", "Tulsidas"], "The Mahabharata is one of the two major Sanskrit epics of ancient India."),
    (2, "Who was the first woman Prime Minister of India?", "Indira Gandhi", ["Sarojini Naidu", "Indira Gandhi", "Pratibha Patil", "Sonia Gandhi"], "Indira Gandhi served as Prime Minister for several terms."),
    (2, "Which Mughal Emperor built the Red Fort in Delhi?", "Shah Jahan", ["Akbar", "Jahangir", "Shah Jahan", "Aurangzeb"], "Shah Jahan also built the Taj Mahal and Jama Masjid."),
    (2, "What was the ancient name of Patna?", "Pataliputra", ["Kashi", "Pataliputra", "Ayodhya", "Taxila"], "Pataliputra was the capital of several major Indian empires."),
    (2, "Who founded the Indian National Army (INA)?", "Subhas Chandra Bose", ["Bhagat Singh", "Subhas Chandra Bose", "Chandrashekhar Azad", "Mangal Pandey"], "Bose formed the INA to fight against British rule with Japanese support."),
    (2, "Which battle led to the establishment of the British Empire in India?", "Battle of Plassey", ["Battle of Panipat", "Battle of Buxar", "Battle of Plassey", "Battle of Haldighati"], "Fought in 1757, it was a major victory for the British East India Company."),
    (2, "Who is called the Nightingale of India?", "Sarojini Naidu", ["Lata Mangeshkar", "Sarojini Naidu", "Annie Besant", "Kasturba Gandhi"], "She was a poet and a prominent leader in the independence movement."),
    (2, "The Ajanta and Ellora caves are in which state?", "Maharashtra", ["Madhya Pradesh", "Maharashtra", "Gujarat", "Karnataka"], "These caves feature ancient rock-cut temples and Buddhist artwork."),
    (2, "Who gave the slogan 'Give me blood and I will give you freedom'?", "Subhas Chandra Bose", ["Bhagat Singh", "Subhas Chandra Bose", "Bal Gangadhar Tilak", "Lala Lajpat Rai"], "Bose used this to inspire the youth to fight for independence."),
    (2, "Which period is often called the 'Golden Age of India'?", "Gupta Empire", ["Maurya Empire", "Mughal Empire", "Gupta Empire", "Chola Empire"], "The Gupta period saw immense achievements in science, math, and art."),
    (2, "Who was the chief architect of the Indian Constitution?", "B.R. Ambedkar", ["Jawaharlal Nehru", "B.R. Ambedkar", "Rajendra Prasad", "Sardar Patel"], "Dr. Ambedkar chaired the drafting committee of the Constitution."),
    (2, "When did the Indian Constitution come into effect?", "Jan 26, 1950", ["Aug 15, 1947", "Jan 26, 1950", "Nov 26, 1949", "Oct 2, 1948"], "This day is celebrated annually as Republic Day."),

    # Hard
    (3, "Which Chinese traveler visited India during the reign of Harsha?", "Hiuen Tsang", ["Fa Hien", "Hiuen Tsang", "I-Tsing", "Marco Polo"], "Hiuen Tsang (Xuanzang) documented early Indian society and Buddhism."),
    (3, "Who was the last Mughal Emperor?", "Bahadur Shah Zafar", ["Aurangzeb", "Shah Alam II", "Bahadur Shah Zafar", "Akbar II"], "He was exiled to Rangoon by the British after the 1857 revolt."),
    (3, "The famous 'Quit India Movement' was launched in which year?", "1942", ["1930", "1942", "1919", "1947"], "Gandhi launched the movement demanding an end to British rule."),
    (3, "What was the real name of Swami Vivekananda?", "Narendranath Datta", ["Gadadhar Chattopadhyay", "Narendranath Datta", "Mool Shankar", "Ram Mohan Roy"], "He was a key figure in introducing Indian philosophies to the Western world."),
    (3, "Who built the famous Sanchi Stupa?", "Ashoka", ["Chandragupta", "Ashoka", "Harsha", "Kanishka"], "The Great Stupa at Sanchi is one of the oldest stone structures in India."),
    (3, "In which year did the Jallianwala Bagh massacre take place?", "1919", ["1905", "1919", "1922", "1931"], "A tragic event where British troops fired on an unarmed crowd in Amritsar."),
    (3, "Who started the Bhoodan Movement?", "Vinoba Bhave", ["Mahatma Gandhi", "Vinoba Bhave", "Jayaprakash Narayan", "Baba Amte"], "It was a voluntary land reform movement encouraging the wealthy to give land to the landless."),
    (3, "Which King fought Alexander the Great at the Battle of the Hydaspes?", "King Porus", ["Chandragupta", "King Porus", "Dhana Nanda", "Bimbisara"], "Porus fought valiantly, earning Alexander's respect."),
    (3, "Who wrote 'Arthashastra'?", "Chanakya", ["Megasthenes", "Chanakya", "Kalidasa", "Banabhatta"], "Chanakya (Kautilya) wrote this ancient Indian treatise on statecraft and economic policy."),
    (3, "The partition of Bengal took place in which year?", "1905", ["1905", "1911", "1947", "1885"], "The partition was announced by Lord Curzon and caused massive protests."),
    (3, "Who founded the Brahmo Samaj?", "Raja Ram Mohan Roy", ["Swami Dayananda", "Raja Ram Mohan Roy", "Ishwar Chandra Vidyasagar", "Vivekananda"], "He was a social reformer who worked to abolish practices like Sati."),
    (3, "What was the capital of the Pallava dynasty?", "Kanchipuram", ["Madurai", "Thanjavur", "Kanchipuram", "Badami"], "Kanchipuram was known for its magnificent temples and learning centers."),
    (3, "Who was the first Indian to go to space?", "Rakesh Sharma", ["Kalpana Chawla", "Rakesh Sharma", "Vikram Sarabhai", "Sunita Williams"], "He flew aboard the Soviet T-11 spacecraft in 1984."),
    (3, "The 'Dandi March' was undertaken to protest against which tax?", "Salt Tax", ["Land Tax", "Salt Tax", "Water Tax", "Income Tax"], "Gandhi marched to the Arabian Sea to make salt in defiance of the British monopoly."),
    (3, "Who was the Maratha ruler famous for his guerrilla warfare tactics?", "Shivaji", ["Baji Rao", "Shivaji", "Sambhaji", "Rana Pratap"], "Chhatrapati Shivaji Maharaj established a competent and progressive civil rule."),
    (3, "Which Indian city was the center of the 1857 Mutiny?", "Meerut", ["Delhi", "Kanpur", "Meerut", "Lucknow"], "The first war of independence sparked when sepoys rebelled in Meerut.")
]

create_json('science.json', science_data)
create_json('history.json', history_data)

print("Generated science.json and history.json")
