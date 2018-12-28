# (c) Breeze Static-Site Generator 2018
# Made by Fred Adams (xtrp)
# Check out Breeze on GitHub at https://github.com/xtrp/breeze
# Check out the Breeze official website at https://xtrp.github.io/breeze/

import sys
import os

# Get project directory file using command line argument
try:
    global project_directory
    project_directory = sys.argv[1]
except:
    print("ERROR: valid project folder not specified")
    sys.exit(1)

# Get all files in project directory


printVal = ""
def display(text):
    global printVal
    if(printVal != ""):
        printVal += "\n"
    printVal += str(text)

exec('''
global printVal
printVal = ""
''')
print printVal