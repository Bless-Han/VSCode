import tkinter as tk

root = tk.Tk()

# 创建一个Listbox
listbox = tk.Listbox(root)

# 向Listbox中添加项目
listbox.insert(1, "项目1")
listbox.insert(2, "项目2")
listbox.insert(3, "项目3")
listbox.insert(4, "项目4")

# 将Listbox放置在窗口中
listbox.pack()

root.mainloop()

