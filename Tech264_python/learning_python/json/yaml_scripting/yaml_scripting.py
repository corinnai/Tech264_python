# Steps:
# Create version of parse_json_to_dict.py but for parsing/converting YAML to a dictionary

# import yaml

# with open('file.yaml', 'r') as yaml_file:
#     servers = yaml.safe_load(yaml_file)
# print(servers)


# Create version of validate_json_file.py but for checking a YAML file

# import os
# import sys
# import yaml

# Check if the user provided a file path as a command-line argument
# if len(sys.argv) > 1:
    # Check if the specified file exists
    # if os.path.exists(sys.argv[1]):
        # Open the file for reading
        # with open(sys.argv[1], "r") as file:
            # Parse the YAML file into a dictionary - safe_load ensures safe parsing
            # file = yaml.safe_load(file)
            # Close the file (optional since 'with' automatically closes it)

        # Output the resulting dictionary if valid YAML was loaded
        # print("YAML file is valid!")
        # print(file)
    # else:
        # Alert the user if the specified file does not exist
        # print(f"ERROR: File '{sys.argv[1]}' not found")
# else:
    # Alert the user if no file was provided as a command-line argument
    # print("ERROR: No YAML file was specified to check")
    # print(f"Usage: {sys.argv[0]} <yaml filename>")





# Create a YAML to JSON file conversion script

# import os
# import sys
# import yaml
# import json


# Check if the user provided the YAML file path as a command-line argument
# if len(sys.argv) > 1:

    # Check if the YAML file exists
    # if os.path.exists(sys.argv[1]):
        # Open the YAML file and load its contents into a Python dictionary
        # with open("file.yaml", "r") as yaml_file:
        #     yaml_data = yaml.safe_load(yaml_file)

        # Create a new JSON file based on the input YAML file's name
        # json_data = os.path.splitext(sys.argv[1])[0] + ".json"


        # Open the JSON file and write the YAML content as JSON
        # with open("file.json", "w") as json_file:
        #     json.dump(yaml_data, json_file , indent = 4)

        # print(f"Successfully converted '{sys.argv[1]}' to '{json_data}'")
    # else:
    #     print(f"ERROR: The file '{sys.argv[1]}' does not exist.")
# else:
#     print("ERROR: No YAML file specified.")
#     print(f"Usage: {sys.argv[0]} <yaml_filename>")






# If time (leave until last): Create a script that check if an entire folders contents is valid YAML (will need loops to check each file)

import os
import sys
import yaml

# Check if the folder path was provided as a command-line argument
if len(sys.argv) > 1:
    folder_path = sys.argv[1]

    # Print the folder path for debugging
    print(f"Checking path: {folder_path}")

    # Check if the folder exists and is a directory
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # Loop through each file in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            # Only check files (ignore directories)
            if os.path.isfile(file_path):
                # Open and load the file as YAML
                with open(file_path, 'r') as file:
                    yaml_data = yaml.safe_load(file)

                # If the YAML loads successfully, it is considered valid
                if yaml_data is not None:
                    print(f"Valid YAML: {file_name}")
                else:
                    print(f"Invalid YAML: {file_name}")
            else:
                print(f"Skipping directory: {file_name}")
    else:
        print(f"ERROR: The path '{folder_path}' is not a valid directory.")
else:
    print("ERROR: No folder specified.")
    print(f"Usage: {sys.argv[0]} <folder_path>")
