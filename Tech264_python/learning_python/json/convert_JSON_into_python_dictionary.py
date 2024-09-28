#Steps:
# Create a new file servers.json and add this json to it:

# {
# 	"server1": {
# 		"hostname": "web-server-1",
# 		"ip_address": "192.168.1.1",
# 		"role": "web",
# 		"status": "active"
# 	},
# 	"server2": {
# 		"hostname": "db-server-1",
# 		"ip_address": "192.168.1.2",
# 		"role": "database",
# 		"status": "maintenance"
# 	}
# }
#Create a file called parse_json_to_dict.py and add code to it to: Steps:

#Use 'with' to open the file created above

#Parse contents the json file into a Python dictionary named "servers"

#Print out the type of "servers"

#Print out the dictionary record with the key "server1"

#Print out the dictionary record with the key "server2"

#Print all of the keys and values. Output should be:

# Key and value: 'server1' = '{'hostname': 'web-server-1', 'ip_address': '192.168.1.1', 'role': 'web', 'status': 'active'}'
#   Record key and sub value: 'hostname' = 'web-server-1'
#   Record key and sub value: 'ip_address' = '192.168.1.1'
#   Record key and sub value: 'role' = 'web'
#   Record key and sub value: 'status' = 'active'
# Key and value: 'server2' = '{'hostname': 'db-server-1', 'ip_address': '192.168.1.2', 'role': 'database', 'status': 'maintenance'}'
#   Record key and sub value: 'hostname' = 'db-server-1'
#   Record key and sub value: 'ip_address' = '192.168.1.2'
#   Record key and sub value: 'role' = 'database'
#   Record key and sub value: 'status' = 'maintenance'

