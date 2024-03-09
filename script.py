import json

# Open json file
with open("source_event_data.json") as f:
    # Load json data into a dictionary 
    data = json.load(f)

# print(data)
print(data)
