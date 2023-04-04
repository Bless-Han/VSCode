from tkinter import *

root = Tk()

def testVal(inStr, acttyp):
    if acttyp == '1': #insert
        if not inStr.isdigit():
            return False
    return True

entry = Entry(root, validate="key")
# Q: What's this code mean and how does it work?
# A: It's a callback function that is called when the user types a character into the entry.
# Q: What is the first argument?
# A: It's the value of the entry.
# Q: What is the second argument?
# A: It's the action type. 1 means insert, 0 means delete, -1 means focus in, -2 means focus out.

entry['validatecommand'] = (entry.register(testVal), '%P', '%d')
entry.pack()

root.mainloop()