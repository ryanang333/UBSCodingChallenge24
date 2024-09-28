from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma():
    data = request.json
    results = []        
    for hunt in data:
        monsters = hunt["monsters"]
        n = len(monsters)
        efficiency = 0
        i = 0
        if n == 1:
            results.append({"efficiency": 0})
            continue
        while i < n:
            # Skip cooldown time if the next monster is stronger
            if i < n - 1 and monsters[i + 1] > monsters[i]:
                i += 1
                continue
            
            # Check if there are monsters to attack
            if monsters[i] > 0:
                # Calculate fee and attack if conditions are met
                fee = monsters[i - 1] if i > 0 else 0
                attack = monsters[i]

                if i + 1 < n and attack > monsters[i + 1]:
                    efficiency += max(0, attack - fee)
                    i += 2  # Skip cooldown time after attack
                else:
                    efficiency += max(0, attack - fee)  # Attack even if not skipping
                    i += 1  # Move to next time frame
            else:
                i += 1  # Move to next time frame if no monsters

        results.append({"efficiency": efficiency})
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)