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
            
            # Initialize the DP variables
            efficiency = 0  # Represents the efficiency at the current time
            previous_efficiency = 0  # Represents the efficiency at the previous time

            for i in range(n):
                # Calculate the attack value
                attack = max(0, monsters[i] - (monsters[i - 1] if i > 0 else 0))

                # Calculate current efficiency considering whether to attack or not
                current_efficiency = max(previous_efficiency, efficiency + attack)

                # Update previous efficiency for the next iteration
                efficiency = current_efficiency

            results.append({"efficiency": efficiency})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
