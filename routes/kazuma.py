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

        # DP array for maximum efficiencies
        dp = [0] * (n + 1)

        # Fill the dp array in reverse order
        for i in range(n - 1, -1, -1):
            attack_value = monsters[i]
            fee = monsters[i - 1] if i > 0 else 0
            
            # Calculate net gain only if there are previous monsters
            if i == 0:
                net_gain = attack_value  # No fee for the first monster
            else:
                net_gain = attack_value - fee
            
            # If attacking the current monster is beneficial
            if net_gain > 0:
                dp[i] = max(dp[i + 1], net_gain + (dp[i + 2] if i + 2 < n else 0))  # Attack and skip
            else:
                dp[i] = dp[i + 1]  # Skip attack if net gain is non-positive

        results.append({"efficiency": dp[0]})  # The maximum efficiency from the first monster

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)