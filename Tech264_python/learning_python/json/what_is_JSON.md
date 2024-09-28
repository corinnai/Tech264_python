# JSON

* **What does it stand for?**
  * `JSON stands for JavaScript Object Notation. `


* **What is it used for?**
  *  `JSON is lightweight, text-based format that is easy for humans to read and write, and easy for machines to generate`
      `It is primarily used to transmit data between a server and web applications as text, making it ideal for APIs, web services, and configuration files.`
  

* **What is it written in?**
  *   `JSON is written in text format and is based on JavaScript object syntax.`


* **Include a simple example of JSON**
```python
{
 "name": "Maria ",
 "age": 25,
 "skills": ["JavaScript", "Python"],
}
```


* **Advantages of using it?**
  *  ` Lightweight: JSON is compact and efficient, reducing bandwidth usage and making it suitable for network communication.`
  
  * `Human-Readable: JSON's structure is easy to read and understand, even by non-programmers.`

  * `Language-Independent: Though based on JavaScript syntax, JSON can be used in almost any programming language, making it versatile.` 
  * `Easy to Parse: Most programming languages provide built-in functions for parsing and generating JSON, making it easy to work with.`
  * `Widely Adopted: JSON is the standard for data exchange in modern web applications and APIs.`

* **What data types can it store/use?**
  * `String (e.g., "hello")`
  * `Number (e.g., 42, 3.14)`
  * `Boolean (e.g., true, false)`
  * `Array (e.g., ["item1", "item2"])`
  * `Object (e.g., {"key": "value"})`
  * `Null (e.g., null)`


* **What is the JSON syntax for:**
  * **Name value pairs?**
     *   `In JSON, data is represented as key-value pairs.`
```python
    "name": "Maria"
```
    
  * **Objects?**
    *  `Objects in JSON are collections of key-value pairs, wrapped in curly braces {}.`
```python
{
  "name": "Maria",
  "age": 25
}
```
  * **How to separate data (key/value pairs) from one another?**
  * `In JSON, key-value pairs within an object are separated by commas.`

  * **JSON arrays (these are like lists in python)?**
    *  `Arrays are ordered collections of values enclosed in square brackets []`
```python
{
  "languages": ["Python", "JavaScript", "C#"]
}

```

# Encoding vs Serializing

#### Encoding: The process of converting data into a specific format so it can be safely transmitted or stored. Encoding typically refers to converting a sequence of characters into a byte format (like UTF-8).

#### Serializing: The process of converting an in-memory object (like a Python dictionary) into a format that can be easily stored or transmitted (like JSON or XML).

```python
  import json

# Create the dictionary
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

# Convert the Python dictionary to a json-formatted string
servers_json_string = json.dumps(servers_dict, indent=4)
print(servers_json_string)

# json.dumps(): This function serializes the Python dictionary into a json-formatted string. The optional parameter indent=4 makes the output more readable (pretty-printing).

```

```python
# Convert this Python dictionary to a json file

with open('servers.json', 'w') as json_file:
  json.dump(servers_dict, json_file, indent=4)

# open() function: This opens a file. The first argument ('servers.json') specifies the name of the file to open. If the file does not exist, Python will create it.


# 'w' mode: This indicates that the file is being opened in "write" mode. If the file already exists, it will be overwritten. If it doesn't exist, it will be created.

# with statement: This is a context manager that ensures the file is properly closed after the code block inside the with is executed, even if an error occurs.

# json.dump(servers_dict, json_file, indent=4):
# json.dump() function: This serializes (converts) the servers_dict (a Python dictionary) into json format and writes it to the open file (json_file).

# First argument (servers_dict): The Python dictionary to be serialized.

# Second argument (json_file): The file object to write the json data into.

# indent=4: This is used to format the json output in a readable way, with each level of nesting indented by 4 spaces. Without this, the json output would appear on a single line (compact form).


# What it does:
# This code converts the servers_dict Python dictionary into json format and saves it as a file called servers.json. The indent=4 ensures that the json file is human-readable with proper indentation.
```

```python
# Check if the file was created and print the content to verify
with open('servers.json', 'r') as json_file:
    data = json_file.read()
    print(data)

# 'r' mode: The file is opened in "read" mode. This means the file's contents will be read but not modified. If the file does not exist, Python will raise an error.

# data = json_file.read():
    # json_file.read(): Reads the entire content of the file (servers.json) and returns it as a single string. This content is then stored in the variable data.
#print(data):
    #Prints the contents of the file to the console, allowing you to verify that the data in the json file is correct and matches the original dictionary (servers_dict) that was written to the file.

# What it does:
    # This block of code opens the json file servers.json in read mode.
    # It reads the contents of the file into the variable data.
    # Then, it prints the content of the file to the console for verification.
```