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

            efficiency = 0
            fee = 0  # This will track the total fees paid to adventurers
            i = 0

            while i < n:
                if monsters[i] > 0:  # Only consider attacking if there are monsters
                    # Calculate potential earnings
                    current_earning = monsters[i] - fee
                    if current_earning > 0:
                        efficiency += current_earning  # Add to efficiency
                    fee = monsters[i]  # Set fee to current monster count

                    # If next monster count is less than or equal, we should skip cooldown
                    if i + 1 < n and monsters[i + 1] <= monsters[i]:
                        i += 1  # Move to next time frame directly
                    else:
                        i += 2  # Move to next time frame after cooldown
                else:
                    i += 1  # Move to next time frame if no monsters

            results.append({"efficiency": efficiency})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
