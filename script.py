import json
import csv

# Open json file
with open("source_event_data.json") as f:
    # Load json data into a dictionary 
    data = json.load(f)

# print(data)
# print(data)


# Open/Create csv file in write mode
with open("output.csv", "w", newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["event_id", "user_session_id", "user_id", "user_ip", "action", "url", "timestamp"])
    # Write the header
    writer.writeheader()

    # Iterate over each json objet to right it as a row in the csv file 
    for event in data:
        # Flatten the nested json "user"
        flattened_data = {
            "event_id": event["event_id"],
            "user_session_id": event["user"]["session_id"],
            "user_id": event["user"]["id"],
            "user_ip": event["user"]["ip"],
            "action": event["action"],
            "url": event["url"],
            "timestamp": event["timestamp"]
        }
        writer.writerow(flattened_data)

