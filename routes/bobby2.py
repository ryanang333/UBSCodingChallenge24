from flask import Flask, request, jsonify

app = Flask(__name__)

def max_bugs_fixed(bug_seq):
    # Sort bugs by their limits
    current_time = 0
    count = 0
    
    for difficulty, limit in bug_seq:
        # Check if we can complete this bug within its limit
        if current_time + difficulty <= limit:
            current_time += difficulty  # Update current time spent
            count += 1  # Increment the count of fixed bugs

    return count

@app.route('/bugfixer/p2', methods=['POST'])
def bugfixer():
    data = request.json
    if not data or 'bugseq' not in data[0]:
        return jsonify({"error": "Invalid input"}), 400

    bug_seq = data[0]['bugseq']
    result = max_bugs_fixed(bug_seq)
    
    return jsonify([result]), 200

if __name__ == '__main__':
    app.run(debug=True)
