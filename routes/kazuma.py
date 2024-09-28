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

            # Initialize a DP array for maximum efficiency
            dp = [0] * n

            for i in range(n):
                # Base case: If Kazuma attacks here
                fee = monsters[i - 1] if i > 0 else 0
                dp[i] = max(dp[i], max(0, monsters[i] - fee))  # Attack now

                # If Kazuma was able to attack last time
                if i > 0:
                    # Move to rear from previous attack
                    dp[i] = max(dp[i], dp[i - 1])

                # Check if he can attack again after cooldown
                if i > 1 and monsters[i - 1] > 0:
                    dp[i] = max(dp[i], dp[i - 2] + max(0, monsters[i] - monsters[i - 1]))

            results.append({"efficiency": max(dp)})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
