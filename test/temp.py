import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.lb = tk.Listbox(self)
        for x in range(20):
            self.lb.insert("end", x)
        self.lb.bind("<<ListboxSelect>>", self.OnSelect)
        self.lb.pack(side="top", fill="both", expand=True)

    def OnSelect(self, event):
        print(event.widget.get(event.widget.curselection()))

app = SampleApp()
app.mainloop()