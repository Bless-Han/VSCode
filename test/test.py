from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Test")

mainframe = ttk.Frame(root, padding="12 3 12 3")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(mainframe, text="Hello World").grid(column=0, row=0)

root.mainloop()