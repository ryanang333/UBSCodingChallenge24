from flask import Flask, request, jsonify

app = Flask(__name__)

def efficient_hunter_kazuma(monsters):
    n = len(monsters)
    
    # If no monsters, no efficiency can be earned
    if n == 0:
        return {"efficiency": 0}
    
    # Initialize DP arrays for resting and attacking
    dp_rest = [0] * (n + 1)
    dp_attack = [0] * (n + 1)
    
    max_efficiency = 0  # Track the maximum efficiency

    for i in range(1, n + 1):
        # If Kazuma prepares at time i (rest state), he could have rested or attacked in the previous time
        dp_rest[i] = max(dp_rest[i - 1], dp_attack[i - 1])

        # If Kazuma attacks at time i, he must have prepared at time i-1
        dp_attack[i] = dp_rest[i - 1] + monsters[i - 1] - 1  # 1 gold spent on adventurers
        
        # Update the maximum efficiency inline
        max_efficiency = max(max_efficiency, dp_rest[i], dp_attack[i])

    return {"efficiency": max_efficiency}

@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma_endpoint():
    data = request.get_json()
    results = [{"efficiency": efficient_hunter_kazuma(m["monsters"])["efficiency"]} for m in data]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
