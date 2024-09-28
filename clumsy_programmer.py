from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

# Function to preprocess the dictionary by creating patterns with one letter removed
def preprocess_dictionary(dictionary):
    pattern_dict = defaultdict(list)
    
    for word in dictionary:
        for i in range(len(word)):
            # Create a pattern by removing the character at index i
            pattern = word[:i] + '*' + word[i+1:]
            pattern_dict[pattern].append(word)
    
    return pattern_dict

# Function to correct mistyped words using the preprocessed dictionary
def correct_mistypes(preprocessed_dict, mistypes):
    corrections = []
    
    for mistyped_word in mistypes:
        # Try to match the mistyped word by generating patterns with one letter removed
        for i in range(len(mistyped_word)):
            pattern = mistyped_word[:i] + '*' + mistyped_word[i+1:]
            
            # If a match is found in the preprocessed dictionary, take the first match
            if pattern in preprocessed_dict:
                corrections.append(preprocessed_dict[pattern][0])
                break
    
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
