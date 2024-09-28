from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/mailtime', methods=['POST'])
def average_response_time():
    data = request.get_json()

    response_times = {user['name']: [] for user in data['users']}
    last_sent_time = {}

    # Process each email to calculate response times
    for email in data['emails']:
        sender = email['sender']
        receiver = email['receiver']
        subject = email['subject']
        time_sent = datetime.fromisoformat(email['timeSent'])
        # Check if the email is a reply (subject starts with "RE:")
        if subject.startswith("RE:"):
            original_subject = subject[4:]  # Remove "RE: " prefix
            if (receiver, original_subject) in last_sent_time:
                # Calculate response time
                print(sender)
                print('this is time sent',time_sent)
                print('this is time received',last_sent_time[(receiver, original_subject)])
                response_time = (time_sent - last_sent_time[(receiver, original_subject)]).total_seconds()
                response_times[sender].append(response_time)
        
        # Update the last sent time for the subject and sender
        last_sent_time[(sender, subject)] = time_sent

    # Calculate average response times
    average_response_times = {
        user: int(sum(times) / len(times)) if times else 0
        for user, times in response_times.items()
    }
    return jsonify(average_response_times)

if __name__ == '__main__':
    app.run(debug=True)