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

        while i < n:
            # Find the best monster to attack
            best_attack = -1
            best_index = -1

            for j in range(i, min(n, i + 3)):  # Look ahead up to 3 monsters
                if monsters[j] > best_attack:
                    best_attack = monsters[j]
                    best_index = j

            if best_index != -1:  # We found a monster to attack
                if best_index > 0:
                    fee = monsters[best_index - 1]  # Fee based on previous monster
                else:
                    fee = 0
                
                efficiency += max(0, best_attack - fee)
                i = best_index + 1  # Move to next monster after the attack
            else:
                i += 1  # No attack possible, move on

        results.append({"efficiency": efficiency})
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
