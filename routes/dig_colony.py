from flask import Flask, request, jsonify

app = Flask(__name__)

# Memoization dictionary
memo = {}

# Precompute the signatures for all pairs of digits (00 to 99)
def precompute_signatures():
    signatures = {}
    for i in range(10):
        for j in range(10):
            if i == j:
                signatures[(i, j)] = 0
            else:
                diff = abs(i - j)
                signatures[(i, j)] = diff if i > j else 10 - diff
    return signatures

signatures = precompute_signatures()

# Function to calculate the new digit for a given pair
def calculate_new_digit(pair, weight):
    i, j = pair
    signature = signatures[(i, j)]
    return (weight + signature) % 10

# Simulate one generation of the colony growth
def simulate_generation(colony, weight):
    new_colony = []
    # Generate new digits for each pair
    length = len(colony)
    
    for i in range(length - 1):
        pair = (int(colony[i]), int(colony[i + 1]))
        new_digit = calculate_new_digit(pair, weight)
        new_colony.append(colony[i])  # Add original digit
        new_colony.append(str(new_digit))  # Add new digit produced by the pair

    new_colony.append(colony[-1])  # Add the last digit (which has no pair)
    return ''.join(new_colony)

# Function to update the running weight of the colony efficiently
def update_weight(colony):
    return sum(int(digit) for digit in colony)

# Main simulation function
def simulate_generations(colony, generations):
    current_colony = colony
    weight = update_weight(current_colony)

    for _ in range(generations):
        if current_colony in memo:
            current_colony, weight = memo[current_colony]
        else:
            new_colony = simulate_generation(current_colony, weight)
            weight = update_weight(new_colony)
            memo[current_colony] = (new_colony, weight)
            current_colony = new_colony

    return weight

@app.route('/digital-colony', methods=['POST'])
def digital_colony():
    data = request.get_json()
    results = []

    for entry in data:
        generations = entry['generations']
        colony = entry['colony']
        
        # Limit to a maximum of 50 generations if needed
        generations = min(generations, 50)

        weight_after_generations = simulate_generations(colony, generations)
        results.append(str(weight_after_generations))
    
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)

