from flask import Flask, request, jsonify

app = Flask(__name__)

def efficient_hunter_kazuma(monsters):
    n = len(monsters)
    if n == 0:
        return {"efficiency": 0}

    # Initialize DP table: dp[i][0] -> rest/prepare, dp[i][1] -> attack
    dp = [[0] * 2 for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        # Rest or Prepare at time i
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        
        # Attack at time i (only possible if prepared at time i-1)
        dp[i][1] = dp[i-1][0] + monsters[i-1]
    
    # The final answer is the maximum efficiency at the last time step, either resting or attacking
    max_efficiency = max(dp[n][0], dp[n][1])
    
    return {"efficiency": max_efficiency}

@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma_endpoint():
    data = request.get_json()
    results = [{"efficiency": efficient_hunter_kazuma(m["monsters"])["efficiency"]} for m in data]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
