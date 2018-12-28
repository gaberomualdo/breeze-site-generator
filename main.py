# (c) Breeze Static-Site Generator 2018
# Made by Fred Adams (xtrp)
# Check out Breeze on GitHub at https://github.com/xtrp/breeze
# Check out the Breeze official website at https://xtrp.github.io/breeze/

# Imports
import sys
import os

# Get project directory file using command line argument
try:
    global project_directory
    project_directory = sys.argv[1]
except:
    print("ERROR: valid project folder not specified")
    sys.exit(1)

# Format project directory file correctly
if(project_directory[-1] != "/"):
    project_directory += "/"

# Get all files in project directory
project_files = []

for dirname, dirnames, filenames in os.walk(project_directory):
    for filename in filenames:
        valid_dir = True
        for dir in dirname.split(os.path.sep)[1:]+[filename]:
            if(dir[0] == "."):
                valid_dir = False
        if(valid_dir):
            project_files.append(os.path.join(dirname, filename))

# Loop through project files and split into valid code and embedded Python code
for file in project_files:
    # Read and store file contents
    file_contents = open(file, "r").read()

    # Loop through contents and split into valid and embedded Python code; with even indices of split_file_contents array being valid code, and odd indices being Python embedded code
    split_file_contents = [""]
    for char_index in range(len(file_contents)):
        char = file_contents[char_index]

        # add new index to array if start or end embed tag has been found; if not, add content to last index in split contents list
        if((char == "<" and file_contents[char_index+1] == "=" and len(split_file_contents)%2 == 1) or (char == "=" and file_contents[char_index+1] == ">" and len(split_file_contents)%2 == 0)):
            split_file_contents.append("")
        else:
            # Only add char if char isn't end of embed tag; e.g. the ">" at the end of "=>" or the "=" at the end of "<="
            if(not (split_file_contents[-1] == "" and ((char == "=" and file_contents[char_index-1] == "<") or (char == ">" and file_contents[char_index-1] == "=")))):
                split_file_contents[-1] += char

# === Just some code I'm saving for later :) ===
# printVal = ""
# def display(text):
#     global printVal
#     if(printVal != ""):
#         printVal += "\n"
#     printVal += str(text)
#
# exec('''
# global printVal
# printVal = ""
# ''')
# print printVal