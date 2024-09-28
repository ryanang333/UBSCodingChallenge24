from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/mailtime', methods=['POST'])
def average_response_time():
    data = request.get_json()

    # Prepare dictionaries to store response times and counts
    response_times = {user['name']: [] for user in data['users']}
    last_sent_time = {}

    # Process each email to calculate response times
    for email in data['emails']:
        sender = email['sender']
        receiver = email['receiver']
        time_sent = datetime.fromisoformat(email['timeSent'])
        
        if receiver in last_sent_time:
            # Calculate response time
            response_time = (time_sent - last_sent_time[receiver]).total_seconds()
            response_times[receiver].append(response_time)

        # Update the last sent time for the sender
        last_sent_time[sender] = time_sent

    # Calculate average response times
    average_response_times = {
        user: int(sum(times) / len(times)) if times else 0
        for user, times in response_times.items()
    }

    return jsonify(average_response_times)

if __name__ == '__main__':
    app.run(debug=True)