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
            efficiency_threshold = 1000  # Set your desired efficiency threshold

            if n == 0:
                results.append({"efficiency": 0})
                continue

            # Initialize variables to track efficiencies and costs
            prev_efficiency = 0  # Efficiency from the previous time frame
            curr_efficiency = 0  # Current efficiency calculation

            for i in range(n):
                # Calculate the attack value considering the previous monster count
                attack = max(0, monsters[i] - (monsters[i - 1] if i > 0 else 0))
                
                # Calculate the cost for hiring adventurers
                cost = monsters[i - 1] if i > 0 else 0
                
                # Calculate potential new efficiency
                new_efficiency = prev_efficiency + attack - cost

                # Ensure the new efficiency does not exceed the threshold
                if new_efficiency < efficiency_threshold:
                    curr_efficiency = max(curr_efficiency, new_efficiency)

                # Update previous efficiency for the next iteration
                prev_efficiency = curr_efficiency

            results.append({"efficiency": curr_efficiency})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
