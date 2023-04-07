from tkinter import *
from tkinter import ttk

root = Tk()
mainframe = ttk.Frame(root, padding="12 3 12 3")
label = ttk.Label(mainframe, text="Enter a number.", width=20, foreground="green")
before = StringVar()
entry = ttk.Entry(mainframe, width=20, textvariable=before)
listbox = Listbox(mainframe, width=22, height=4, bg="systemTransparent")

numbers = {}
curselection = (0, )

def main():
    root.title("Base Converter")

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    label.grid(column=1, row=1, sticky=(W, N))
    entry.grid(column=1, row=2, sticky=W)
    entry.bind("<KeyRelease>", entry_on_change)
    listbox.grid(column=1, row=3, sticky=W)
    listbox.selection_set(0)
    listbox.bind("<<ListboxSelect>>", on_select)
    init_listbox()

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
        
    entry.focus()
    root.mainloop()
    
def entry_on_change(event):
    convert()
    
def init_listbox():
    listbox.delete(0)
    listbox.insert(0, "Binary")
    listbox.delete(1)
    listbox.insert(1, "Octal")
    listbox.delete(2)
    listbox.insert(2, "Decimal")
    listbox.delete(3)
    listbox.insert(3, "Hex")

def convert(*args):
    s = ["Bin", "Oct", "Dec", "Hex"]
    value = entry.get()
    if value == "":
        init_listbox()
        label.config(text="Enter a number.", foreground="green")
        return
    else:
        label.config(text="OK", foreground="green")
    if check(value, s[curselection[0]]):
        numbers = count(value, s[curselection[0]])
        listbox.delete(0)
        listbox.insert(0, f"Binary {numbers['Bin']}")
        listbox.delete(1)
        listbox.insert(1, f"Octal {numbers['Oct']}")
        listbox.delete(2)
        listbox.insert(2, f"Decimal {numbers['Dec']}")
        listbox.delete(3)
        listbox.insert(3, f"Hex {numbers['Hex']}")
        print(value)
    else:
        init_listbox()
        label.config(text="Invalid number.", foreground="red")
        
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

def on_select(event):
    global curselection
    if event.widget.curselection():
        # TODO: Fix this. Change the value of entry.
        curselection = event.widget.curselection()
    convert()

if __name__ == "__main__":
    main()
