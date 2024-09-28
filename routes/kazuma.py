from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_efficiency(monsters):
    """Helper function to calculate maximum efficiency for given monsters."""
    n = len(monsters)

    # Handle edge cases for efficiency
    if n == 0:
        return 0  # No monsters, no efficiency
    if n == 1:
        return 0  # One monster, no efficiency

    # Initialize the last two states for DP
    prev2 = 0  # Efficiency from two steps back
    prev1 = 0  # Efficiency from one step back

    # Iterate through the monsters starting from the second one
    for i in range(1, n):
        # Calculate potential efficiency gain by attacking the current monster
        attack_gain = max(0, monsters[i] - monsters[i - 1])
        # Current efficiency based on the last two states
        current_efficiency = max(prev1, prev2 + attack_gain)

        # Move the window forward
        prev2 = prev1
        prev1 = current_efficiency

    return prev1  # Return the last calculated efficiency


@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma():
    try:
        # Validate and parse input data
        data = request.json
        if not isinstance(data, list):
            return jsonify({"error": "Input should be a list of hunts"}), 400

        results = []

        for hunt in data:
            # Validate the structure of each hunt
            if not isinstance(hunt, dict) or "monsters" not in hunt:
                return jsonify({"error": "Each hunt should be a dictionary with a 'monsters' key"}), 400
            
            monsters = hunt["monsters"]
            if not isinstance(monsters, list) or not all(isinstance(m, int) for m in monsters):
                return jsonify({"error": "Monsters should be a list of integers"}), 400
            
            # Calculate efficiency for the current hunt using the helper function
            efficiency = calculate_efficiency(monsters)
            results.append({"efficiency": efficiency})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
