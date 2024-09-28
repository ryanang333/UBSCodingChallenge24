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

            # DP array to store maximum efficiency at each time frame
            dp = [0] * (n + 2)  # We use n + 2 to avoid boundary checks

            for i in range(n):
                # Calculate the attack earning at time i
                attack_earning = max(0, monsters[i] - 1)

                # Carry forward the maximum efficiency
                dp[i + 1] = max(dp[i + 1], dp[i])

                # If Kazuma attacks at time i, he can earn attack_earning
                dp[i + 2] = max(dp[i + 2], dp[i] + attack_earning)

            results.append({"efficiency": max(dp)})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
