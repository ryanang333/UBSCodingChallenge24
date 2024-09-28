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

            # Edge case: No monsters
            if n == 0:
                results.append({"efficiency": 0})
                continue

            # DP array for tracking maximum efficiency
            dp = [0] * (n + 1)  # n+1 to handle edge cases easily

            for i in range(n):
                # Update current state without action
                dp[i + 1] = max(dp[i + 1], dp[i])  # Carry forward previous efficiency

                # Check if Kazuma can attack
                if monsters[i] > 0:
                    attack_earning = monsters[i] - 1  # Earnings after paying adventurers

                    # If Kazuma attacks at time i, he cannot attack at i + 1
                    if i + 1 < n:  # Only update if there is a next time
                        dp[i + 2] = max(dp[i + 2], dp[i] + attack_earning)
                    else:
                        dp[i + 1] = max(dp[i + 1], dp[i] + attack_earning)

            # Maximum efficiency found
            results.append({"efficiency": max(dp)})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
