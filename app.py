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

if __name__ == '__main__':
    app.run(debug=True)
