from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

# Function to preprocess the dictionary by creating patterns with one letter removed
def preprocess_dictionary(dictionary):
    pattern_dict = defaultdict(list)

    # Build patterns for all words in the dictionary
    for word in dictionary:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i+1:]
            pattern_dict[pattern].append(word)
    
    return pattern_dict

# Function to correct mistyped words using the preprocessed dictionary
def correct_mistypes(preprocessed_dict, mistypes):
    corrections = []

    # For each mistyped word, generate patterns and check for corrections
    for mistyped_word in mistypes:
        found_correction = False  # Flag to indicate if a correction was found
        for i in range(len(mistyped_word)):
            pattern = mistyped_word[:i] + '*' + mistyped_word[i+1:]
            if pattern in preprocessed_dict:
                corrections.append(preprocessed_dict[pattern][0])
                found_correction = True
                break  # Stop checking after finding the first match
        if not found_correction:
            corrections.append(mistyped_word)  # Append the original if no correction is found

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
