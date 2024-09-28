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

            # Edge case for no monsters
            if n == 0:
                results.append({"efficiency": 0})
                continue

            # Initialize efficiencies
            previous_efficiency = 0  # Efficiency up to the previous monster
            current_efficiency = 0   # Efficiency up to the current monster
            
            for i in range(n):
                # Calculate the potential attack earnings
                attack_earning = monsters[i] - 1 if monsters[i] > 0 else 0
                
                # Determine the new current efficiency
                # 1. Either we don't attack and carry forward the previous efficiency
                # 2. Or we attack, which means we add current earnings to previous efficiency
                new_efficiency = max(current_efficiency, previous_efficiency + attack_earning)
                
                # Update previous and current efficiencies for the next iteration
                previous_efficiency = current_efficiency
                current_efficiency = new_efficiency

            results.append({"efficiency": current_efficiency})

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
