from datetime import datetime, timedelta
import pytz
import json

def calculate_response_times(data):
    emails = data['emails']
    users_info = {user['name']: user['officeHours'] for user in data['users']}
    
    response_times = {user['name']: [] for user in data['users']}
    
    # Convert timestamps to UTC
    for email in emails:
        sender = email['sender']
        receiver = email['receiver']
        sent_time = datetime.fromisoformat(email['timeSent']).astimezone(pytz.utc)
        
        # Find the corresponding response
        for response in emails:
            if response['sender'] == receiver and response['receiver'] == sender:
                response_time = datetime.fromisoformat(response['timeSent']).astimezone(pytz.utc)
                
                if sender == 'Bob':
                    # Calculate time from sent to response
                    response_times[sender].append(int((response_time - sent_time).total_seconds()))
                else:
                    # Check for office hours and calculate adjusted response time
                    office_start = datetime.combine(sent_time.date(), datetime.min.time()).replace(hour=users_info[sender]['start'], tzinfo=pytz.timezone(users_info[sender]['timeZone']))
                    office_end = datetime.combine(sent_time.date(), datetime.min.time()).replace(hour=users_info[sender]['end'], tzinfo=pytz.timezone(users_info[sender]['timeZone']))
                    
                    if sent_time < office_start:
                        sent_time = office_start
                    
                    if sent_time > office_end:
                        sent_time += timedelta(days=1)
                        sent_time = office_start
                    
                    # Calculate the response time considering office hours
                    total_time = 0
                    while sent_time < response_time:
                        if sent_time < office_start:
                            sent_time = office_start
                        if sent_time < office_end:
                            # Calculate next interval until the response time or end of work
                            next_end = min(office_end, response_time)
                            total_time += (next_end - sent_time).total_seconds()
                            sent_time = office_end
                        else:
                            sent_time += timedelta(days=1)
                            sent_time = office_start
                    
                    response_times[sender].append(int(total_time))

    # Calculate averages
    average_times = {}
    for user, times in response_times.items():
        if times:
            average_times[user] = round(sum(times) / len(times))
    
    return average_times

# Example Input
data = {
  "emails": [
    {
      "subject": "subject",
      "sender": "Alice",
      "receiver": "Bob",
      "timeSent": "2024-01-12T15:00:00+01:00"
    },
    {
      "subject": "RE: subject",
      "sender": "Bob",
      "receiver": "Alice",
      "timeSent": "2024-01-15T09:00:00+08:00"
    },
    {
      "subject": "RE: RE: subject",
      "sender": "Alice",
      "receiver": "Bob",
      "timeSent": "2024-01-16T09:05:00+01:00"
    }
  ],
  "users": [
    {
      "name": "Alice",
      "officeHours": {
        "timeZone": "Europe/Paris",
        "start": 9,
        "end": 18
      }
    },
    {
      "name": "Bob",
      "officeHours": {
        "timeZone": "Asia/Singapore",
        "start": 8,
        "end": 17
      }
    }
  ]
}

# Calculate response times
result = calculate_response_times(data)
print(json.dumps(result, indent=2))
