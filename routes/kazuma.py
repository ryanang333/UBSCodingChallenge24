from flask import Flask, request, jsonify

app = Flask(__name__)

def efficient_hunter_kazuma(monsters):
    n = len(monsters)
    dp = [0] * n

    for i in range(n):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = max(0, monsters[i] - 1)
        else:
            dp[i] = max(dp[i-1], dp[i-2] + max(0, monsters[i] - 1))

    return {"efficiency": dp[n-1]}

@app.route('/efficient-hunter-kazuma', methods=['POST'])
def efficient_hunter_kazuma_endpoint():
    try:
        data = request.get_json()
        results = [{"efficiency": efficient_hunter_kazuma(m["monsters"])["efficiency"]} for m in data]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)