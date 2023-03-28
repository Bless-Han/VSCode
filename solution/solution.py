import os
import time

def show_reminder():
    title = "Reminder"
    message = "Time to take a break!"
    command = f'display notification "{message}" with title "{title}" sound name "Glass"'
    os.system(f"osascript -e '{command}'")

# 设置提醒时间间隔（秒）
interval = 6

while True:
    show_reminder()
    time.sleep(interval)



print("Ok")

