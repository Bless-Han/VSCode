import tkinter as tk

root = tk.Tk()

t = tk.Text(root)
t.pack()

t.insert(tk.END, "只读\n模式", width=55)
t.configure(state='disabled')

root.mainloop()
