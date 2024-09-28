from flask import Flask, request, jsonify

app = Flask(__name__)

def efficient_hunter_kazuma(monsters):
    n = len(monsters)
    dp = [[0] * 2 for _ in range(n + 1)]

    for i in range(1, n + 1):
        # Prepare Transmutation Circle
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - monsters[i - 1])

        # Attack
        dp[i][1] = max(dp[i - 1][0] + monsters[i - 1] - 1, dp[i - 1][1])

    # Find the maximum efficiency
    max_efficiency = 0
    for i in range(n + 1):
        for j in range(2):
            if dp[i][j] > max_efficiency:
                max_efficiency = dp[i][j]

    return {"efficiency": max_efficiency}

@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma_endpoint():
    data = request.get_json()
    results = [{"efficiency": efficient_hunter_kazuma(m["monsters"])["efficiency"]} for m in data]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)