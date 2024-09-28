from textwrap import indentfrom textwrap import indent

# JSON (JavaScript Object Notation)
*   Data Representation Format
* Commonly Used for Apis and Configs
* Lightweight and easy to Read/Write
* Integrates easily with most languages

## Data Types 
* strings  -- "Hello World"
* numbers -- 10 1.5 -30 
* booleans -- true 
* null -- null 
* arrays  -- [1,2,3] ["Hello", "World"]
* object -- {"key": "value"} {"age": 30}



# Convert this Python dictionary to a JSON file

```python
import json

example = {
    "id": "1",
    "name": "first name",
    "age": "in years"
}
with open("example.json", "w") as json_file:
    json.dump(example ,json_file, indent = 4 )
```

### json.dump() `writes the JSON format to the file,`
### json.dumps() `just returns the string representation.`

# Convert this Python dictionary into a JSON-formatted string

```python
import json

example = {
    "id": "1",
    "name": "first name",
    "age": "in years"
}
json_object = json.dumps(example, indent = 4)
print(json_object)
```

# Converting Json string into a python dictionary

```python
import json
json_data = '{"name": "ana", "age": 25, "skills": ["Python", "DevOps", "JavaScript"], "isStudent": true}'

python_dict = json.loads(json_data)
print(python_dict)
```
### json.loads() `takes a JSON string and converts it into a Python dictionary.`



# Load JSON from a file

```python
import json

with open("example.json", "r") as jsonfile:
    python_file = json.load(jsonfile)
print(python_file)
```
### json.load() `Reads a JSON file and converts it to a Python dictionary.`


#  Converting JSON string to YAML string

```python
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
```
### json.loads(json_string) `converts the JSON string into a Python dictionary.`

### yaml.dump(json_data, default_flow_style=False) `converts the Python dictionary into a YAML string. Setting default_flow_style=False ensures that YAML will be written in block style (more readable).`


# Converting JSON file to YAML file

```python
import json
import yaml

# Step 1: Read json data from a file
with open('input.json', 'r') as json_file:
    json_data = json.load(json_file)

# Step 2: Convert json to YAML
yaml_data = yaml.dump(json_data, default_flow_style=False)

# Step 3: Write YAML data to a file
with open('output.yaml', 'w') as yaml_file:
    yaml_file.write(yaml_data)

print("json data has been successfully converted to YAML and saved to output.yaml")

```
### json.load() `reads the JSON data from a file and converts it into a Python dictionary.`
### yaml.dump() `converts the Python dictionary to a YAML format.`
### yaml_file.write() `writes the converted YAML data into a new file named output.yaml.`
### default_flow_style=False ` Ensures YAML is written in a human-readable block style.`