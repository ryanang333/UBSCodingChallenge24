from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma():
    try:
        data = request.json
        results = []

        for hunt in data:
            monsters = hunt["monsters"]
            n = len(monsters)

            if n == 1:
                results.append({"efficiency": 0})
                continue

            # Initialize the DP array with size n
            dp = [0] * n

            # Base cases
            dp[0] = 0  # No efficiency on the first step (since Kazuma rests initially)
            dp[1] = max(0, monsters[1] - monsters[0])  # Efficiency after first attack, only if it yields positive

            # Fill the DP array using optimized logic
            for i in range(2, n):
                # Attack option: consider current attack and rest one step before, with a check on monster size
                attack = max(0, monsters[i] - monsters[i - 1])
                dp[i] = max(dp[i - 1], dp[i - 2] + attack)

            # Append the maximum efficiency result for this hunt
            results.append({"efficiency": dp[n - 1]})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
