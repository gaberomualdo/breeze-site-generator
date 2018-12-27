printVal = ""
def display(text):
    global printVal
    if(printVal != ""):
        printVal += "\n"
    printVal += text

exec('''
global printVal
printVal = ""
display("test")
''')
print printVal