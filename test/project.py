from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
root = Tk()
root.title("Base Converter")

mainframe = ttk.Frame(root, padding="12 3 12 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

before = StringVar()
before_entry = ttk.Entry(mainframe, width=10, textvariable=before)
before_entry.grid(column=1, row=2, sticky=W)

after = StringVar()
after_entry = ttk.Entry(mainframe, width=10, textvariable=after)
after_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="From:", width=10).grid(column=1, row=1, sticky=(W, N))
ttk.Label(mainframe, text="To:", width=10).grid(column=2, row=1, sticky=W)

ttk.Label(mainframe, text="Binary", width=10).grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Octal", width=10).grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Decimal", width=10).grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Hex", width=10).grid(column=1, row=6, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

before_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()