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

            if n == 1:
                results.append({"efficiency": monsters[0]})
                continue

            # Optimized DP: We don't need to store the entire DP array
            # We only need to keep track of the last two states (dp[i-1] and dp[i-2])
            prev2 = 0  # This will store dp[i-2]
            prev1 = monsters[0]  # This will store dp[i-1]

            for i in range(1, n):
                # Calculate the current dp[i] using the recurrence relation
                current = max(prev1, prev2 + monsters[i])
                
                # Move the window forward for the next iteration
                prev2 = prev1
                prev1 = current

            # The result is the maximum efficiency at the last time step
            results.append({"efficiency": prev1})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
