from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

# Function to preprocess the dictionary by creating patterns with one letter removed
def preprocess_dictionary(dictionary):
    pattern_dict = defaultdict(set)

    for word in dictionary:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            pattern_dict[pattern].add(word)  # Use a set for faster lookups

    return pattern_dict

# Function to find the correct word by checking the mistyped word against the dictionary
def find_correction(mistyped_word, pattern_dict):
    # Generate patterns for the mistyped word and check against the pattern dictionary
    for i in range(len(mistyped_word)):
        pattern = mistyped_word[:i] + '*' + mistyped_word[i+1:]
        if pattern in pattern_dict:
            # Return the first matching word from the set
            return next(iter(pattern_dict[pattern]))  # Get an arbitrary element from the set
    return mistyped_word  # If no correction found, return the original word

# Function to correct mistyped words using the preprocessed dictionary
def correct_mistypes(preprocessed_dict, mistypes):
    corrections = [find_correction(word, preprocessed_dict) for word in mistypes]
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

        # Preprocess the dictionary to generate patterns
        preprocessed_dict = preprocess_dictionary(dictionary)

        # Correct the mistyped words using the preprocessed patterns
        corrections = correct_mistypes(preprocessed_dict, mistypes)

        # Append the corrections to the result list
        result.append({"corrections": corrections})

    # Return the result as a JSON response
    return jsonify(result)

# Entry point to start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
