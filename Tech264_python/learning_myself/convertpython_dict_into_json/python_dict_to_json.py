#dictionary
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
# Convert this Python dictionary to a json file
with open("example.json", "w") as jsonfile :
    json.dump(servers_dict, jsonfile, indent = 4)

print(type(servers_dict))


# Convert this Python dictionary into a json-formatted string
employee_details ={
  "id": "04",
  "name": "sunil",
  "department": "HR"
}

json_object = json.dumps(employee_details, indent = 4)
print(json_object)


# Converting Json string into a python dictionary

json_data = '{"name": "ana", "age": 25, "skills": ["Python", "DevOps", "JavaScript"], "isStudent": true}'

python_dict = json.loads(json_data)
print(python_dict)


# Load json from a file

import json

with open("example.json", "r") as jsonfile:
    python_file = json.load(jsonfile)
print(python_file)