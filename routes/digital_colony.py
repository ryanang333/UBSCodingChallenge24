from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def calculate_weight_and_new_colony(colony):
    # Calculate the weight of the colony
    weight = sum(int(digit) for digit in colony)
    
    # Calculate new colony digits based on the signatures
    new_colony = []
    for i in range(len(colony) - 1):
        a = int(colony[i])
        b = int(colony[i + 1])
        
        # Calculate signature
        if a == b:
            signature = 0
        else:
            signature = abs(a - b) if a > b else (10 - abs(a - b))
        
        # New digit to be added
        new_digit = (weight + signature) % 10
        new_colony.append(colony[i])
        new_colony.append(str(new_digit))
    
    new_colony.append(colony[-1])  # add the last digit of the current colony
    return ''.join(new_colony), weight

def simulate_generations(colony, generations):
    current_colony = colony
    for _ in range(generations):
        current_colony, _ = calculate_weight_and_new_colony(current_colony)
    final_weight = sum(int(digit) for digit in current_colony)
    return final_weight

@app.route('/digital-colony', methods=['POST'])
def digital_colony():
    data = request.get_json()
    results = []
    
    for entry in data:
        generations = entry['generations']
        colony = entry['colony']
        weight_after_generations = simulate_generations(colony, generations)
        results.append(str(weight_after_generations))
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
