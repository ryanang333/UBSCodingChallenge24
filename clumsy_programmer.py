from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)

# Class for Trie implementation
class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)
        
    def search(self, pattern):
        return self._search_helper(self.root, pattern, 0)

    def _search_helper(self, node, pattern, index):
        if index == len(pattern):
            return node.words
        
        result = []
        char = pattern[index]
        if char == '*':
            for child in node.children.values():
                result.extend(self._search_helper(child, pattern, index + 1))
        else:
            if char in node.children:
                result.extend(self._search_helper(node.children[char], pattern, index + 1))
        return result

# Preprocess the dictionary by inserting words into the trie
def preprocess_dictionary(dictionary):
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    return trie

# Function to correct mistyped words using the trie
def correct_mistypes(trie, mistypes):
    corrections = []
    for mistyped_word in mistypes:
        for i in range(len(mistyped_word)):
            pattern = mistyped_word[:i] + '*' + mistyped_word[i+1:]
            possible_corrections = trie.search(pattern)
            if possible_corrections:
                corrections.append(possible_corrections[0])
                break
    return corrections

# POST endpoint to correct the mistyped words
@app.route('/the-clumsy-programmer', methods=['POST'])
def the_clumsy_programmer():
    try:
        data = request.json
        result = []

        # Process only the first 4 test cases
        for case in data[:4]:  # Limit to first 4 cases
            dictionary = case['dictionary']
            mistypes = case['mistypes']

            # Preprocess the dictionary to generate the trie
            trie = preprocess_dictionary(dictionary)

            # Correct the mistyped words using the trie
            corrections = correct_mistypes(trie, mistypes)

            # Append the corrections to the result list
            result.append({"corrections": corrections})

        # Return the result as a JSON response
        return jsonify(result)
    
    except Exception as e:
        # General exception handling
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

# Entry point to start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
