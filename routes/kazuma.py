from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_efficiency(monsters):
    """Helper function to calculate maximum efficiency for given monsters."""
    n = len(monsters)
    
    # If there are no monsters or only one monster, no attack is efficient
    if n == 0 or (n == 1 and monsters[0] <= 0):
        return 0

    # Initialize the DP array
    dp = [0] * n

    # Fill the DP array based on the logic derived
    for i in range(n):
        # Case 1: Move to rear (don't attack this time frame)
        if i > 0:
            dp[i] = dp[i - 1]

        # Case 2: Prepare a transmutation circle and attack this time frame
        if i >= 1:  # Need at least one time frame to prepare
            gain = monsters[i] - 1 if monsters[i] > 0 else 0
            dp[i] = max(dp[i], dp[i - 2] + gain if i > 1 else gain)

    return dp[n - 1]  # The last entry has the maximum efficiency

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
