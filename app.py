from flask import Flask
from flask import Flask, request, jsonify
import requests, re
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

meaningpedia_resp = requests.get(
    "https://meaningpedia.com/5-letter-words?show=all")

# get list of words by grabbing regex captures of response
# there's probably a far better way to do this by actually parsing the HTML
# response, but I don't know how to do that, and this gets the job done

# compile regex
pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
# find all matches
word_list = pattern.findall(meaningpedia_resp.text)


def evaluate_possible_words(guess_history, evaluation_history, words):
    correct = [None] * 5   
    present = {}   
    absent = set()         
    
    for guess, evaluation in zip(guess_history, evaluation_history):
        for i, (letter, result) in enumerate(zip(guess, evaluation)):
            if result == 'O':
                correct[i] = letter  
            elif result == 'X':
                if letter not in present:
                    present[letter] = []
                present[letter].append(i)  
            elif result == '-':
                absent.add(letter) 
    
    def is_valid_word(word):
        for i, letter in enumerate(correct):
            if letter is not None and word[i] != letter:
                return False
        for letter, positions in present.items():
            if letter not in word:
                return False
            for pos in positions:
                if word[pos] == letter: 
                    return False
        if any(letter in word for letter in absent):
            return False
        return True

    filtered_words = [word for word in words if is_valid_word(word)]
    return filtered_words

@app.route('/wordle-game', methods=['POST'])
def wordle_game():
    if request.is_json:
        data = request.get_json()
        print(len(data['guessHistory']))
        if len(data['guessHistory']) == 0:
            # First guess
            guess = "stare"
        elif len(data['guessHistory']) == 1:
            guess = 'cloud'
        elif len(data['guessHistory']) == 2:
            guess = 'pinky'
        else:
            guess_history = data['guessHistory']
            evaluation_history = data['evaluationHistory']
            possible_words = evaluate_possible_words(guess_history, evaluation_history, word_list)
            guess = possible_words[0]
        response = {
            "guess": guess
        }
        return jsonify(response), 200
    else:
        return jsonify({"error": "Invalid request format"}), 400
    


@app.route('/tourist', methods=['POST'])
def tourist(input_dict, starting_point, time_limit):
    # Constants (subway lines, travel times)
    subway_stations = {
        "Tokyo Metro Ginza Line": [
            "Asakusa", "Tawaramachi", "Inaricho", "Ueno", "Ueno-hirokoji", "Suehirocho",
            "Kanda", "Mitsukoshimae", "Nihombashi", "Kyobashi", "Ginza", "Shimbashi",
            "Toranomon", "Tameike-sanno", "Akasaka-mitsuke", "Nagatacho", "Aoyama-itchome",
            "Gaiemmae", "Omotesando", "Shibuya"
        ],
        "Tokyo Metro Marunouchi Line": [
            "Ogikubo", "Minami-asagaya", "Shin-koenji", "Higashi-koenji", "Shin-nakano",
            "Nakano-sakaue", "Nishi-shinjuku", "Shinjuku", "Shinjuku-sanchome", "Shin-ochanomizu",
            "Ochanomizu", "Awajicho", "Otemachi", "Tokyo", "Ginza", "Kasumigaseki", "Kokkai-gijidomae",
            "Akasaka-mitsuke", "Yotsuya", "Yotsuya-sanchome", "Shinjuku-gyoemmae", "Nishi-shinjuku-gochome",
            "Nakano-fujimicho", "Nakano-shimbashi", "Nakano-sakaue", "Shinjuku-sanchome", "Kokkai-gijidomae",
            "Kasumigaseki", "Ginza", "Tokyo", "Otemachi", "Awajicho", "Shin-ochanomizu", "Ochanomizu"
        ],
        "Tokyo Metro Hibiya Line": [
            "Naka-meguro", "Ebisu", "Hiroo", "Roppongi", "Kamiyacho", "Kasumigaseki", "Hibiya",
            "Ginza", "Higashi-ginza", "Tsukiji", "Hatchobori", "Kayabacho", "Nihombashi",
            "Kodemmacho", "Akihabara", "Naka-okachimachi", "Ueno", "Iriya", "Minowa",
            "Minami-senju", "Kita-senju"
        ],
        "Tokyo Metro Tozai Line": [
            "Nakano", "Ochiai", "Takadanobaba", "Waseda", "Kagurazaka", "Iidabashi", "Kudanshita",
            "Takebashi", "Otemachi", "Nihombashi", "Kayabacho", "Monzen-nakacho", "Kiba",
            "Toyosu", "Minami-sunamachi", "Nishi-kasai", "Kasai", "Urayasu", "Minami-gyotoku",
            "Gyotoku", "Myoden", "Baraki-nakayama", "Nishi-funabashi"
        ],
        "Tokyo Metro Chiyoda Line": [
            "Yoyogi-uehara", "Yoyogi-koen", "Meiji-jingumae", "Omotesando", "Nogizaka", "Akasaka",
            "Kokkai-gijidomae", "Kasumigaseki", "Hibiya", "Nijubashimae", "Otemachi",
            "Shin-ochanomizu", "Yushima", "Nezu", "Sendagi", "Nishi-nippori", "Machiya",
            "Kita-senju", "Ayase", "Kita-ayase"
        ],
        "Tokyo Metro Yurakucho Line": [
            "Wakoshi", "Chikatetsu-narimasu", "Chikatetsu-akatsuka", "Heiwadai", "Hikawadai",
            "Kotake-mukaihara", "Senkawa", "Kanamecho", "Ikebukuro", "Higashi-ikebukuro",
            "Gokokuji", "Edogawabashi", "Iidabashi", "Ichigaya", "Kojimachi", "Nagatacho",
            "Sakuradamon", "Yurakucho", "Ginza-itchome", "Shintomicho", "Toyocho",
            "Kiba", "Toyosu", "Tsukishima", "Shintomicho", "Tatsumi", "Shinonome", "Ariake"
        ],
        "Tokyo Metro Hanzomon Line": [
            "Shibuya", "Omotesando", "Aoyama-itchome", "Nagatacho", "Hanzomon", "Kudanshita",
            "Jimbocho", "Otemachi", "Mitsukoshimae", "Suitengumae", "Kiyosumi-shirakawa",
            "Sumiyoshi", "Kinshicho", "Oshiage"
        ],
        "Tokyo Metro Namboku Line": [
            "Meguro", "Shirokanedai", "Shirokane-takanawa", "Azabu-juban", "Roppongi-itchome",
            "Tameike-sanno", "Nagatacho", "Yotsuya", "Ichigaya", "Iidabashi", "Korakuen",
            "Todaimae", "Hon-komagome", "Komagome", "Nishigahara", "Oji", "Oji-kamiya",
            "Shimo", "Akabane-iwabuchi"
        ],
        "Tokyo Metro Fukutoshin Line": [
            "Wakoshi", "Chikatetsu-narimasu", "Chikatetsu-akatsuka", "Narimasu", "Shimo-akatsuka",
            "Heiwadai", "Hikawadai", "Kotake-mukaihara", "Senkawa", "Kanamecho", "Ikebukuro",
            "Zoshigaya", "Nishi-waseda", "Higashi-shinjuku", "Shinjuku-sanchome", "Kita-sando",
            "Meiji-jingumae", "Shibuya"
        ],
        "Toei Asakusa Line": [
            "Nishi-magome", "Magome", "Nakanobu", "Togoshi", "Gotanda", "Takanawadai",
            "Sengakuji", "Mita", "Shiba-koen", "Daimon", "Shimbashi", "Higashi-ginza",
            "Takaracho", "Nihombashi", "Ningyocho", "Higashi-nihombashi", "Asakusabashi",
            "Kuramae", "Asakusa", "Honjo-azumabashi", "Oshiage"
        ],
        "Toei Mita Line": [
            "Meguro", "Shirokanedai", "Shirokane-takanawa", "Mita", "Shiba-koen", "Onarimon",
            "Uchisaiwaicho", "Hibiya", "Otemachi", "Jimbocho", "Suidobashi", "Kasuga",
            "Hakusan", "Sengoku", "Sugamo", "Nishi-sugamo", "Shin-itabashi", "Itabashi-kuyakushomae",
            "Itabashi-honcho", "Motohasunuma", "Shin-takashimadaira", "Nishidai", "Hasune",
            "Takashimadaira", "Shimura-sakaue", "Shimura-sanchome", "Nishidai"
        ],
        "Toei Shinjuku Line": [
            "Shinjuku", "Shinjuku-sanchome", "Akebonobashi", "Ichigaya", "Kudanshita",
            "Jimbocho", "Ogawamachi", "Iwamotocho", "Bakuro-yokoyama", "Hamacho",
            "Morishita", "Kikukawa", "Sumiyoshi", "Nishi-ojima", "Ojima", "Higashi-ojima",
            "Funabori", "Ichinoe", "Mizue", "Shinozaki", "Motoyawata"
        ],
        "Toei Oedo Line": [
            "Hikarigaoka", "Nerima-kasugacho", "Toshimaen", "Nerima", "Nerima-sakamachi",
            "Shin-egota", "Ochiai-minami-nagasaki", "Nakai", "Higashi-nakano", "Nakano-sakaue",
            "Nishi-shinjuku-gochome", "Tochomae", "Shinjuku-nishiguchi", "Higashi-shinjuku",
            "Wakamatsu-kawada", "Ushigome-yanagicho", "Ushigome-kagurazaka", "Iidabashi",
            "Kasuga", "Hongosanchome", "Ueno-okachimachi", "Shin-okachimachi", "Kuramae",
            "Ryogoku", "Morishita", "Kiyosumi-shirakawa", "Monzen-nakacho", "Tsukishima",
            "Kachidoki", "Shiodome", "Daimon", "Akasaka-mitsuke", "Roppongi", "Aoyama-itchome",
            "Shinjuku", "Tochomae", "Shinjuku", "Shinjuku-sanchome", "Higashi-shinjuku",
            "Wakamatsu-kawada", "Ushigome-yanagicho", "Ushigome-kagurazaka", "Iidabashi",
            "Kasuga", "Hongosanchome", "Ueno-okachimachi", "Shin-okachimachi", "Kuramae",
            "Ryogoku", "Morishita", "Kiyosumi-shirakawa", "Monzen-nakacho", "Tsukishima",
            "Kachidoki", "Shiodome", "Daimon", "Shiodome", "Tsukishima"
        ]
    }
    
    travelling_time_betw_stations = {
        "Tokyo Metro Ginza Line": 2,
        "Tokyo Metro Marunouchi Line": 3,
        "Tokyo Metro Hibiya Line": 2.5,
        "Tokyo Metro Tozai Line": 4,
        "Tokyo Metro Chiyoda Line": 1.5,
        "Tokyo Metro Yurakucho Line": 2,
        "Tokyo Metro Hanzomon Line": 2,
        "Tokyo Metro Namboku Line" : 1,
        "Tokyo Metro Fukutoshin Line": 3,
        "Toei Asakusa Line": 3.5,
        "Toei Mita Line": 4,
        "Toei Shinjuku Line": 1.5,
        "Toei Oedo Line": 1
    }
    
    # Step 1: Identify the subway line
    starting_line = None
    for line, stations in subway_stations.items():
        if starting_point in stations:
            starting_line = line
            break
    
    if starting_line is None:
        return jsonify({"error": "Invalid starting point"})
    
    # All possible stations
    stations_list = subway_stations[starting_line]
    
    # Step 2: Pathfinding (maximize satisfaction within time constraints)
    def find_max_satisfaction_path():
        best_path = []
        max_satisfaction = 0
        
        # Initialize variables for exploration (visit each station)
        for i in range(len(stations_list)):
            current_path = [starting_point]
            current_satisfaction = input_dict[starting_point][0]  # Initial satisfaction
            time_spent = input_dict[starting_point][1]  # Time spent at starting point
            
            # Explore further stations
            for j in range(i+1, len(stations_list)):
                next_station = stations_list[j]
                travel_time = travelling_time_betw_stations[starting_line]
                required_time = input_dict[next_station][1]
                
                if time_spent + travel_time + required_time <= time_limit:
                    time_spent += travel_time + required_time
                    current_satisfaction += input_dict[next_station][0]
                    current_path.append(next_station)
                else:
                    break  # Stop if time limit exceeded
            
            # Check if this path is better than the previous one
            if current_satisfaction > max_satisfaction:
                max_satisfaction = current_satisfaction
                best_path = current_path
        
        return best_path, max_satisfaction
    
    # Step 3: Run pathfinding and determine the best path
    best_path, max_satisfaction = find_max_satisfaction_path()
    
    # Step 4: Return the result in JSON format
    return jsonify({
        "best_path": best_path,
        "max_satisfaction": max_satisfaction
    })


if __name__ == '__main__':
    app.run(debug=True)
