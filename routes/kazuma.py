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

            if n == 0:
                results.append({"efficiency": 0})
                continue
            elif n == 1:
                results.append({"efficiency": 0})
                continue

            # Initialize the previous two states for DP
            prev2 = 0  # Equivalent to dp[i-2]
            prev1 = max(0, monsters[0])  # Equivalent to dp[i-1] (only attack first monster)

            for i in range(1, n):
                attack = max(0, monsters[i] - monsters[i - 1])  # Calculate attack value
                
                # Current efficiency is the max of skipping the current monster or attacking it
                current = max(prev1, prev2 + attack)

                # Update previous states for next iteration
                prev2 = prev1
                prev1 = current

            results.append({"efficiency": prev1})  # The last computed efficiency

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
