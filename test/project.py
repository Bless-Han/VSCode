from tkinter import *
from tkinter import ttk
import pyperclip

root = Tk()
mainframe = ttk.Frame(root, padding="12 3 12 3")
label_left = ttk.Label(mainframe, text="Enter a number.", width=20, foreground="green")
label_left.grid(column=1, row=1, sticky=(W, N))
label_right = ttk.Label(mainframe, text="1111  Click to copy.", width=20, foreground="green")
label_right.grid(column=2, row=2, sticky=(W, N))
before = StringVar()
entry = ttk.Entry(mainframe, width=20, textvariable=before)
listbox_left = Listbox(mainframe, width=22, height=4, bg="systemTransparent")
listbox_right = Listbox(mainframe, width=22, height=4, bg="systemTransparent")

numbers = {}
curselection_left = (0, )
curselection_right = (0, )
s = ["Bin", "Oct", "Dec", "Hex"]

def main():
    root.title("Base Converter")

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    entry.grid(column=1, row=2, sticky=W)
    entry.bind("<KeyRelease>", entry_on_change)
    listbox_left.grid(column=1, row=3, sticky=W)
    listbox_left.insert(0, "Binary")
    listbox_left.insert(1, "Octal")
    listbox_left.insert(2, "Decimal")
    listbox_left.insert(3, "Hex")
    listbox_left.selection_set(0)
    listbox_left.bind("<<ListboxSelect>>", on_select_left)
    listbox_right.grid(column=2, row=3, sticky=E)
    listbox_right.bind("<<ListboxSelect>>", on_select_right)
    init_listbox()

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
        
    entry.focus()
    root.mainloop()
    
def entry_on_change(event):
    convert()
    
def init_listbox():
    listbox_right.delete(0)
    listbox_right.insert(0, "Binary")
    listbox_right.delete(1)
    listbox_right.insert(1, "Octal")
    listbox_right.delete(2)
    listbox_right.insert(2, "Decimal")
    listbox_right.delete(3)
    listbox_right.insert(3, "Hex")

def convert(*args):
    global numbers
    global curselection_left
    value = entry.get()
    print("left:", curselection_left)
    if value == "":
        init_listbox()
        label_left.config(text="Enter a number.", foreground="green")
        return False
    elif check(value, s[curselection_left[0]]):
        label_left.config(text="OK", foreground="green")
        label_right.config(text="Click to copy.", foreground="green")
        numbers = count(value, s[curselection_left[0]])
        listbox_right.delete(0)
        listbox_right.insert(0, f"Binary {numbers['Bin']}")
        listbox_right.delete(1)
        listbox_right.insert(1, f"Octal {numbers['Oct']}")
        listbox_right.delete(2)
        listbox_right.insert(2, f"Decimal {numbers['Dec']}")
        listbox_right.delete(3)
        listbox_right.insert(3, f"Hex {numbers['Hex']}")
        print(value)
        return True
    else:
        init_listbox()
        label_left.config(text="Invalid number.", foreground="red")
        return False
        
# Check if the value valid.
def check(value, base):
    match base:
        case "Bin": return all(c in "01" for c in value)
        case "Oct": return all(c in "01234567" for c in value)
        case "Dec": return all(c in "0123456789" for c in value)
        case "Hex": return all(c in "0123456789ABCDEF" for c in value.upper())
        
# Change the base of value to all the others
def count(value, base):
    decimal = 0
    match base:
        case "Bin": decimal = int(value, 2)
        case "Oct": decimal = int(value, 8)
        case "Dec": decimal = int(value, 10)
        case "Hex": decimal = int(value, 16)
        
    return {
        "Bin": bin(decimal)[2:],
        "Oct": oct(decimal)[2:],
        "Dec": decimal,
        "Hex": hex(decimal)[2:].upper()
    }

def on_select_left(event):
    global curselection_left
    curselection_left = event.widget.curselection()
    if curselection_left:
        # If s[curselection_left[0]] in numbers, then change the entry.
        if s[curselection_left[0]] in numbers:
            entry.delete(0, END)
            entry.insert(0, numbers[s[curselection_left[0]]])
        convert()

def on_select_right(event):
    global curselection_right
    global numbers
    curselection_right = event.widget.curselection()
    if curselection_right:
        pyperclip.copy(numbers[s[curselection_right[0]]])
        label_right.config(text="Copied!", foreground="green")

if __name__ == "__main__":
    main()
