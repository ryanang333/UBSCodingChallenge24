from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_efficiency(monster_counts):
    n = len(monster_counts)
    if n == 0:
        return 0

    # Initialize a dp array to store max efficiency
    dp = [0] * n
    
    # Base case: if Kazuma attacks at the last time frame
    dp[n - 1] = monster_counts[n - 1]  # He can only attack the last time frame

    # Fill the DP table backwards
    for i in range(n - 2, -1, -1):
        max_efficiency = 0
        # Calculate the sum of monsters defeated from current index to j
        current_cost = 0
        
        for j in range(i, n):
            current_cost += monster_counts[j]
            # Kazuma attacks at time i, then moves to the rear at time i+1
            # The next time he can attack is at j + 1
            if j + 1 < n:
                efficiency = current_cost + dp[j + 1]
            else:
                efficiency = current_cost
            
            # Max efficiency at i
            max_efficiency = max(max_efficiency, efficiency)

        dp[i] = max_efficiency
    
    return dp[0]  # Maximum efficiency starting from time t0

@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma():
    data = request.json
    results = []

    for entry in data:
        monster_counts = entry['monsters']
        efficiency = calculate_efficiency(monster_counts)
        results.append({'efficiency': efficiency})
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)