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