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
                results.append({"efficiency": max(0, monsters[0])})
                continue

            # Initialize variables for the DP calculation
            prev_efficiency_2 = 0  # Efficiency for two steps before
            prev_efficiency_1 = max(0, monsters[0])  # Efficiency for the previous step

            for i in range(1, n):
                attack = max(0, monsters[i] - monsters[i - 1]) if i > 0 else monsters[i]

                # Compute the current efficiency by considering two choices:
                # 1. Skip attacking this monster and take the previous efficiency (prev_efficiency_1)
                # 2. Attack this monster and add the efficiency from two steps back (prev_efficiency_2 + attack)
                current_efficiency = max(prev_efficiency_1, prev_efficiency_2 + attack)

                # Update the previous efficiencies for the next iteration
                prev_efficiency_2 = prev_efficiency_1
                prev_efficiency_1 = current_efficiency

            # Append the final efficiency for this hunt
            results.append({"efficiency": prev_efficiency_1})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
