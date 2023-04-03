from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    root.title("Base Converter")

    mainframe = ttk.Frame(root, padding="12 3 12 3")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="From:", width=10).grid(column=1, row=1, sticky=(W, N))
    ttk.Label(mainframe, text="To:", width=10).grid(column=2, row=1, sticky=W)

    before = StringVar()
    before_entry = ttk.Entry(mainframe, width=10, textvariable=before)
    before_entry.grid(column=1, row=2, sticky=W)
    before_entry.bind("<Key>", on_entry_change)

    after_label = ttk.Label(mainframe, text="", width=10)
    after_label.grid(column=2, row=2, sticky=W)
    after_label.config(text="1")

    listbox_left = Listbox(mainframe, width=12, height=4, bg="systemTransparent")
    listbox_left.grid(column=1, row=3, sticky=W)
    listbox_left.insert(0, "Binary")
    listbox_left.insert(1, "Octal")
    listbox_left.insert(2, "Decimal")
    listbox_left.insert(3, "Hex")
    listbox_left.selection_set(0)

    listbox_right = Listbox(mainframe, width=12, height=4, bg="systemTransparent")
    listbox_right.grid(column=2, row=3, sticky=W)
    listbox_right.insert(0, "Binary")
    listbox_right.insert(1, "Octal")
    listbox_right.insert(2, "Decimal")
    listbox_right.insert(3, "Hex")

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    before_entry.focus()
    root.bind("<Return>", calculate)

    root.mainloop()

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

def on_entry_change(event):
    print(event.widget.get())
    # TODO: 监测事件，并修改其他控件内容


def on_select_left(event):
    # TODO: 监测事件，并修改其他控件内容
    ...

def on_select_right(event):
    # TODO: 监测事件，并修改其他控件内容
    ...

if __name__ == "__main__":
    main()
