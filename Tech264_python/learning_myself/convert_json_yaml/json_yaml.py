#Converting json string to YAML string
import json
import yaml

json_string = '''
{
  "name": "Maria",
  "age": 25,
  "skills": ["Python", "DevOps", "JavaScript"],
  "isStudent": true
}
'''

json_data = json.loads(json_string)
print(json_data)

yaml_data = yaml.dump(json_data, default_flow_style=False)
print(yaml_data)



#Converting json file to YAML file

import json
import yaml

# Step 1: Read json data from a file
with open("valid_json.json", "r") as  json_file:
    json_data = json.load(json_file)

# Step 2: Convert json to YAML
yaml_data = yaml.dump(json_data, default_flow_style=False)

# Step 3: Write YAML data to a file
with open("output.yaml", "w") as yaml_file:
    yaml_file.write(yaml_data)
print("json successfully")