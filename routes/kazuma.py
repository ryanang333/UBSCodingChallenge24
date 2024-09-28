from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma():
    data = request.json
    results = []

    for hunt in data:
        monsters = hunt["monsters"]
        n = len(monsters)
        
        # Create a DP table to store maximum efficiency at each position
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # No attack case: carry forward the previous efficiency
            dp[i] = dp[i + 1]

            # Evaluate attack on the current monster
            attack_value = monsters[i]
            fee = monsters[i - 1] if i > 0 else 0
            
            # Calculate the potential efficiency
            net_gain = max(0, attack_value - fee)
            
            # If we attack the current monster
            if i + 2 < n:
                dp[i] = max(dp[i], net_gain + dp[i + 2])  # Skip the next monster
            else:
                dp[i] = max(dp[i], net_gain)  # No monsters left to skip

        results.append({"efficiency": dp[0]})  # The maximum efficiency starting from the first monster
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
