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
            if i < n-1 and monsters[i+1] > monsters[i]:  # Look ahead for better attack timing
                i += 1  # Move to the rear, skip this time frame
                continue
            
            if monsters[i] > 0:  # Prepare to attack if there are monsters
                if i + 1 < n and monsters[i] > monsters[i+1]:
                    attack = monsters[i]
                    fee = monsters[i-1] if i > 0 else 0  # Fee based on monsters at previous time
                    efficiency += max(0, attack - fee)  # Calculate net gold gain
                    i += 2  # Skip the cooldown time after attack
                else:
                    i += 1  # No attack, continue to the next frame
            else:
                i += 1  # Move to the rear if no monsters

        results.append({"efficiency": efficiency})
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
