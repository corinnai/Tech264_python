# Research:
# What is encoding vs serialising (very quick, two or three dot points to understand the difference)
    # Encoding: The process of converting data into a specific format so it can be safely transmitted or stored.
    # Serializing: The process of converting an in-memory object (like a Python dictionary) into a format that can be easily stored or transmitted (like json or XML).
# Work out which one of them are you doing with the subtasks below
from operator import index
import json
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}
#the task serialize the dictionary into json-formatted string
print(type(servers_dict))

# Subtasks:

# Convert this Python dictionary into a json-formatted string
json_string = json.dumps(servers_dict, indent=4)
print(json_string)


# Convert this Python dictionary to a json file
with open('servers.json', 'w') as json_file:
    json.dump(servers_dict, json_file, indent=4)

# Check if the file was created and print the content to verify
with open('servers.json', 'r') as json_file:
    data = json_file.read()
    print(data)

