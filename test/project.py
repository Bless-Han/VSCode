from tkinter import *
from tkinter import ttk

root = Tk()
mainframe = ttk.Frame(root, padding="12 3 12 3")
before = StringVar()
before_entry = ttk.Entry(mainframe, width=20, textvariable=before)
after_label = ttk.Label(mainframe, text="", width=20)
listbox_left = Listbox(mainframe, width=22, height=4, bg="systemTransparent")
listbox_right = Listbox(mainframe, width=22, height=4, bg="systemTransparent")

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

    before_entry.grid(column=1, row=2, sticky=W)

    after_label.grid(column=2, row=2, sticky=W)

    listbox_left.grid(column=1, row=3, sticky=W)
    listbox_left.insert(0, "Binary")
    listbox_left.insert(1, "Octal")
    listbox_left.insert(2, "Decimal")
    listbox_left.insert(3, "Hex")
    listbox_left.selection_set(0)

    listbox_right.grid(column=2, row=3, sticky=W)
    listbox_right.insert(0, "Binary")
    listbox_right.insert(1, "Octal")
    listbox_right.insert(2, "Decimal")
    listbox_right.insert(3, "Hex")

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)
        
    listening_event()
    before_entry.focus()
    root.bind("<Return>", convert)
    root.mainloop()
    
def listening_event():
    listbox_left.bind("<<ListboxSelect>>", on_select_left)
    listbox_right.bind("<<ListboxSelect>>", on_select_right)


def convert(*args):
    s = ["Bin", "Oct", "Dec", "Hex"]
    try:
        value = int(before_entry.get())
    except ValueError:
        after_label.config(text="Invalid value.")
    else:
        numbers = count(value, s[left_curselection[0]])
        listbox_right.delete(0)
        listbox_right.insert(0, f"Binary ({numbers['Bin']})")
        listbox_right.delete(1)
        listbox_right.insert(1, f"Octal ({numbers['Oct']})")
        listbox_right.delete(2)
        listbox_right.insert(2, f"Decimal ({numbers['Dec']})")
        listbox_right.delete(3)
        listbox_right.insert(3, f"Hex ({numbers['Hex']})")
        after_label.config(text=numbers[s[right_curselection[0]]])
        # TODO

def on_select_left(event):
    global left_curselection
    if event.widget.curselection():
        left_curselection = event.widget.curselection()
    convert()

def on_select_right(event):
    global right_curselection
    if event.widget.curselection():
        right_curselection = event.widget.curselection()
    convert()

if __name__ == "__main__":
    main()
