import json

# Step 1: Use 'with' to open the json file
with open('servers.json', 'r') as json_file:
    # Step 2: Parse the contents of the json file into a Python dictionary
    servers = json.load(json_file)

# Step 3: Print the type of "servers" to verify it's a dictionary
print("Type of 'servers':", type(servers))

# Step 4: Print the dictionary record with the key "server1"
print("Record with key 'server1':", servers['server1'])

# Step 5: Print the dictionary record with the key "server2"
print("Record with key 'server2':", servers['server2'])

# Step 6: Print all keys and values
for key, value in servers.items():  # item() - method to return key-value pairs in dictionary
                                    # key - server's identifier(name or ID)
                                    # value - dictionary records
    print(f"Key and value: '{key}' = '{value}'")
    for sub_key, sub_value in value.items():
        print(f"  Record key and sub value: '{sub_key}' = '{sub_value}'")
