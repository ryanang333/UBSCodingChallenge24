from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma():
    data = request.json
    results = []

    for hunt in data:
        monsters = hunt["monsters"]
        n = len(monsters)

        if n == 0:
            results.append({"efficiency": 0})
            continue
        
        # Initialize variables for tracking efficiencies
        prev_efficiency = 0  # Efficiency when skipping current monster
        curr_efficiency = 0  # Efficiency when considering current monster

        for i in range(n - 1, -1, -1):
            # Calculate potential efficiency if attacking the current monster
            attack_value = monsters[i]
            fee = monsters[i - 1] if i > 0 else 0
            net_gain = max(0, attack_value - fee)

            # Update the current efficiency considering both attack and skip
            next_efficiency = prev_efficiency if i + 1 < n else 0  # Previous step efficiency
            curr_efficiency = max(net_gain + (prev_efficiency if i + 2 < n else 0), next_efficiency)

            # Move to the next state
            prev_efficiency, curr_efficiency = curr_efficiency, prev_efficiency

        results.append({"efficiency": prev_efficiency})  # The maximum efficiency starting from the first monster
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)