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

            # Initialize the DP array
            dp = [0] * n

            # Base cases
            dp[0] = 0  # No monsters, no efficiency
            if monsters[0] > 0:
                dp[1] = max(0, monsters[0] - 0)  # Only attack if there's something to defeat

            # Fill the DP array
            for i in range(1, n):
                attack = max(0, monsters[i] - monsters[i - 1]) if i > 0 else monsters[i]
                dp[i] = max(dp[i - 1], (dp[i - 2] + attack) if i > 1 else attack)

            results.append({"efficiency": dp[n - 1]})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
