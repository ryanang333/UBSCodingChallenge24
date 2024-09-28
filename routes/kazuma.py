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
            
            # Initialize variables to track maximum efficiency
            prev2 = 0  # Corresponds to dp[i - 2]
            prev1 = max(0, monsters[0])  # Corresponds to dp[i - 1]

            for i in range(1, n):
                # Calculate current attack value
                attack = max(0, monsters[i] - monsters[i - 1])
                
                # Calculate the maximum efficiency for the current time frame
                current = max(prev1, prev2 + attack)

                # Update previous states for the next iteration
                prev2 = prev1
                prev1 = current

            results.append({"efficiency": prev1})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
