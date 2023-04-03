import tkinter as tk

def on_select(event):
    # 获取当前选中的项
    selected_item = my_listbox.get(my_listbox.curselection())
    # 在控制台中打印选中的项
    print(selected_item)

root = tk.Tk()

# 创建一个Listbox并添加选项
my_listbox = tk.Listbox(root)
my_listbox.insert(0, "Option 1")
my_listbox.insert(1, "Option 2")
my_listbox.insert(2, "Option 3")
my_listbox.pack()

# 绑定<<ListboxSelect>>事件处理程序
my_listbox.bind("<<ListboxSelect>>", on_select)

root.mainloop()

