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
            dp[1] = max(0, monsters[1] - 1)  # Only attack if there's something to defeat

            # Fill the DP array
            for i in range(2, n):
                attack = max(0, monsters[i] - monsters[i-1] - 1)
                dp[i] = max(dp[i - 1], dp[i - 2] + attack)

            results.append({"efficiency": dp[n - 1]})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)