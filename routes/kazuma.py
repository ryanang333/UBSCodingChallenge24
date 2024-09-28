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
            
            # Initialize DP array
            dp = [0] * n
            
            # Base cases
            dp[0] = max(0, monsters[0])  # If he attacks the first time
            if n > 1:
                # Calculate the second time frame
                dp[1] = max(dp[0], monsters[1] - monsters[0])  # He can attack or skip

            # Fill the DP array
            for i in range(2, n):
                # Choose to attack or skip
                dp[i] = max(dp[i - 1],  monsters[i] - monsters[i - 1] + dp[i - 2])

            results.append({"efficiency": dp[-1]})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
