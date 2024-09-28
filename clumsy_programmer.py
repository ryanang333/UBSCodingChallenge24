from flask import Flask, request, jsonify

app = Flask(__name__)


# Helper function to check if two words differ by exactly one letter
def differs_by_one(word1, word2):
    diff_count = 0
    for a, b in zip(word1, word2):
        if a != b:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1

# Function to correct mistyped words using the dictionary
def correct_mistypes(dictionary, mistypes):
    corrections = []
    for mistyped_word in mistypes:
        # Iterate over each correct word in the dictionary
        for correct_word in dictionary:
            # Call differs_by_one and pass mistyped_word and correct_word
            if differs_by_one(mistyped_word, correct_word):
                corrections.append(correct_word)
                break  # Once a match is found, no need to check further
    return corrections

# POST endpoint to correct the mistyped words
@app.route('/the-clumsy-programmer', methods=['POST'])
def the_clumsy_programmer():
    data = request.json
    result = []
    
    # Process each case in the input list
    for case in data:
        dictionary = case['dictionary']
        mistypes = case['mistypes']
        
        # Correct the mistyped words
        corrections = correct_mistypes(dictionary, mistypes)
        
        # Append the corrections to the result list
        result.append({"corrections": corrections})
    
    # Return the result as a JSON response
    return jsonify(result)

# Entry point to start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
