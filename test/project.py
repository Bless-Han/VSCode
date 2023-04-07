from tkinter import *
from tkinter import ttk

root = Tk()
mainframe = ttk.Frame(root, padding="12 3 12 3")
before = StringVar()
before_entry = ttk.Entry(mainframe, width=20, textvariable=before)
after_label = ttk.Label(mainframe, text="", width=20)
left_listbox = Listbox(mainframe, width=22, height=4, bg="systemTransparent")
right_text = Text(root, height=4,width=20)

numbers = {}
left_curselection = (0, )
right_curselection = (0, )

def main():
    root.title("Base Converter")

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="From:", width=20).grid(column=1, row=1, sticky=(W, N))
    ttk.Label(mainframe, text="To:", width=20).grid(column=2, row=1, sticky=W)

    before_entry.bind("<KeyRelease>", entry_on_change)
    before_entry.grid(column=1, row=2, sticky=W)

    after_label.grid(column=2, row=2, sticky=W)

    left_listbox.grid(column=1, row=3, sticky=W)
    left_listbox.insert(0, "Binary")
    left_listbox.insert(1, "Octal")
    left_listbox.insert(2, "Decimal")
    left_listbox.insert(3, "Hex")
    left_listbox.selection_set(0)
    left_listbox.bind("<<ListboxSelect>>", on_select_left)

    right_text.grid(column=2, row=3, sticky=W)

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
        
    before_entry.focus()
    root.bind("<Return>", convert)
    root.mainloop()
    
def entry_on_change(event):
    convert()

def convert(*args):
    s = ["Bin", "Oct", "Dec", "Hex"]
    value = before_entry.get()
    if check(value, s[left_curselection[0]]):
        numbers = count(value, s[left_curselection[0]])
        right_label.config(text=f"{numbers['Bin']}\n{numbers['Oct']}\n{numbers['Dec']}\n{numbers['Hex']}")
        after_label.config(text="")
    else:
        after_label.config(text="Invalid value.")
        
def check(value, base):
    match base:
        case "Bin": return all(c in "01" for c in value)
        case "Oct": return all(c in "01234567" for c in value)
        case "Dec": return all(c in "0123456789" for c in value)
        case "Hex": return all(c in "0123456789ABCDEF" for c in value.upper())
        
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
    global left_curselection
    if event.widget.curselection():
        left_curselection = event.widget.curselection()
    convert()

if __name__ == "__main__":
    main()
