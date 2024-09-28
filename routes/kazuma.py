from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_efficiency(monsters):
    n = len(monsters)
    if n == 0:
        return 0
    
    # Initialize dp array with zeroes
    dp = [0] * (n + 2)  # Extra space for boundary conditions

    # Fill dp array from back to front
    for i in range(n - 1, -1, -1):
        # Calculate potential earnings if attacking now
        attack_now = monsters[i] + (dp[i + 2] if i + 2 < n else 0) - 1
        # Carry over max efficiency from the next time frame
        move_to_rear = dp[i + 1]
        
        # Store the maximum of both options
        dp[i] = max(attack_now, move_to_rear)

    return max(dp[0], 0)  # Ensure non-negative efficiency

@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma():
    data = request.get_json()
    output_data = []

    for entry in data:
        monsters = entry["monsters"]
        efficiency = calculate_efficiency(monsters)
        output_data.append({"efficiency": efficiency})

    return jsonify(output_data)

if __name__ == '__main__':
    app.run(debug=True)