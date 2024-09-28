from flask import Flask, request, jsonify

app = Flask(__name__)

def efficient_hunter_kazuma(monsters):
    n = len(monsters)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # Calculate the maximum efficiency by considering two options:
        # 1. Attack at the current time frame (i)
        # 2. Attack at the previous time frame (i-1) and move to the current time frame (i)
        dp[i] = max(dp[i - 1], dp[i - 2] + monsters[i - 1] - 1 if i > 1 else monsters[i - 1] - 1)

    return {"efficiency": dp[n]}

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