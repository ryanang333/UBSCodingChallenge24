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

# Function to update the running weight of the colony efficiently
def update_weight(colony):
    return sum(int(digit) for digit in colony)

# Function to simulate a single generation with caching
def simulate_generation(colony, weight, cache):
    new_colony = []
    for i in range(len(colony) - 1):
        pair = (colony[i], colony[i + 1])
        if pair not in cache:
            a = int(colony[i])
            b = int(colony[i + 1])
            signature = abs(a - b) if a != b else 0
            new_digit = (weight + signature) % 10
            cache[pair] = str(new_digit)
        new_colony.append(colony[i])
        new_colony.append(cache[pair])
    new_colony.append(colony[-1])
    return ''.join(new_colony)

# Main simulation function with cycle detection and pair caching
def simulate_generations(colony, generations):
    current_colony = colony
    weight = update_weight(current_colony)
    seen = {}
    cycle_detected = False
    cycle_length = 0
    cycle_start = 0
    cache = {}

    for gen in range(generations):
        if current_colony in memo:
            current_colony, weight = memo[current_colony]
        else:
            if current_colony in seen:
                cycle_start = seen[current_colony]
                cycle_length = gen - cycle_start
                cycle_detected = True
                break
            seen[current_colony] = gen
            new_colony = simulate_generation(current_colony, weight, cache)
            weight = update_weight(new_colony)
            memo[current_colony] = (new_colony, weight)
            current_colony = new_colony

    if cycle_detected:
        remaining_generations = (generations - cycle_start) % cycle_length
        for _ in range(remaining_generations):
            current_colony, weight = memo[current_colony]

    return weight

@app.route('/digital-colony', methods=['POST'])
def digital_colony():
    data = request.get_json()
    results = []

    for entry in data:
        generations = entry['generations']
        colony = entry['colony']
        weight_after_generations = simulate_generations(colony, generations)
        results.append(str(weight_after_generations))

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)