import tkinter as tk
import time

class TypingTest:
    def __init__(self, master):
        self.master = master
        master.title("Typing Test")

        # 创建GUI元素
        self.label = tk.Label(master, text="Type this:")
        self.label.pack()

        self.text = tk.Text(master, height=5, width=30)
        self.text.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack()

        self.time_label = tk.Label(master, text="")
        self.time_label.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        # 初始化变量
        self.started = False
        self.start_time = 0
        self.end_time = 0
        self.text_to_type = "Hello, World!"

    def start(self):
        if not self.started:
            self.started = True
            self.start_time = time.time()
            self.master.after(1000, self.update_time)
        else:
            self.check_result()

    def update_time(self):
        if self.started:
            elapsed_time = int(time.time() - self.start_time)
            self.time_label.config(text="Time: {} seconds".format(elapsed_time))
            self.master.after(1000, self.update_time)

    def check_result(self):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        typed_text = self.text.get("1.0", "end-1c")
        accuracy = self.calculate_accuracy(typed_text, self.text_to_type)
        wpm = self.calculate_wpm(typed_text, elapsed_time)
        self.result_label.config(text="Accuracy: {:.2f}%, WPM: {:.2f}".format(accuracy, wpm))

    def calculate_accuracy(self, typed_text, expected_text):
        correct_chars = 0
        for i in range(len(typed_text)):
            if typed_text[i] == expected_text[i]:
                correct_chars += 1
        return correct_chars / len(expected_text) * 100

    def calculate_wpm(self, typed_text, elapsed_time):
        num_chars = len(typed_text)
        num_words = num_chars / 5
        wpm = num_words / (elapsed_time / 60)
        return wpm

root = tk.Tk()
typing_test = TypingTest(root)
root.mainloop()

