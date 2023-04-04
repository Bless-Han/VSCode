from tkinter import *
from tkinter import ttk

root = Tk()
mainframe = ttk.Frame(root, padding="12 3 12 3")
before = StringVar()
before_entry = ttk.Entry(mainframe, width=10, textvariable=before)
after_label = ttk.Label(mainframe, text="", width=10)
listbox_left = Listbox(mainframe, width=12, height=4, bg="systemTransparent")
listbox_right = Listbox(mainframe, width=12, height=4, bg="systemTransparent")

def main():
    root.title("Base Converter")

    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="From:", width=10).grid(column=1, row=1, sticky=(W, N))
    ttk.Label(mainframe, text="To:", width=10).grid(column=2, row=1, sticky=W)

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
    # before_entry.bind("<Key>", on_entry_change)
    listbox_left.bind("<<ListboxSelect>>", on_select_left)
    listbox_right.bind("<<ListboxSelect>>", on_select_right)


def convert(*args):
    try:
        value = int(before_entry.get())
    except ValueError:
        after_label.config(text="Invalid value.")
    else:
        after_label.config(text=value)

def on_entry_change(event):
    convert()
    print(event.widget.get())
    # TODO: 监测事件，并修改其他控件内容
    # after_label.config(text=before_entry.get())

def on_select_left(event):
    # TODO: 监测事件，并修改其他控件内容
    print(event.widget.curselection())
    # after_label.config(text="left_test")
    ...

def on_select_right(event):
    # TODO: 监测事件，并修改其他控件内容
    # after_label.config(text="right_test")
    ...

if __name__ == "__main__":
    main()
