from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma():
    try:
        data = request.json
        
        # Validate input data
        if not isinstance(data, list):
            return jsonify({"error": "Input should be a list of hunts"}), 400

        results = []

        for hunt in data:
            # Validate hunt structure
            if not isinstance(hunt, dict) or "monsters" not in hunt:
                return jsonify({"error": "Each hunt should be a dictionary with a 'monsters' key"}), 400

            monsters = hunt["monsters"]
            
            # Ensure monsters is a list
            if not isinstance(monsters, list) or not all(isinstance(m, int) for m in monsters):
                return jsonify({"error": "Monsters should be a list of integers"}), 400

            n = len(monsters)

            # Handle edge case for empty monster list
            if n == 0:
                results.append({"efficiency": 0})
                continue

            # Handle case where there is only one monster
            if n == 1:
                results.append({"efficiency": 0})
                continue

            # Initialize the DP array to track max efficiency
            dp = [0] * n

            # Base case: no efficiency gain for the first monster (dp[0] = 0)
            dp[0] = 0

            # Handle second position for DP array
            dp[1] = max(0, monsters[1] - monsters[0])

            # Fill the DP array with the maximum efficiency calculation
            for i in range(2, n):
                # Calculate the efficiency gain by attacking the current monster
                attack = max(0, monsters[i] - monsters[i - 1])
                # Update dp[i] by considering whether to skip the previous monster or not
                dp[i] = max(dp[i - 1], dp[i - 2] + attack)

            # Append the result for the current hunt
            results.append({"efficiency": dp[n - 1]})

        return jsonify(results)

    except Exception as e:
        # Return a 400 error with the exception message if something goes wrong
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
