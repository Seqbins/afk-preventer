import time
import sys
import platform
import os
import pyautogui
import random

OS = platform.system()

# check for supported OS and display instructions if needed
def check_os():
    if OS == "Darwin":
        print("macOS: Ensure your terminal has Accessibility access.")
        print("System Settings > Privacy & Security > Accessibility\n")
    elif OS == "Linux":
        display = os.environ.get("DISPLAY") or \
                  os.environ.get("WAYLAND_DISPLAY")
        if not display:
            print("No display server detected. Requires X11 or Wayland.")
            sys.exit(1)

def get_interval():
    while True:
        raw = input("\nTime interval in seconds between each keypress: ")
        try:
            interval = float(raw)
            if interval > 0:
                return interval
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_key():
    default = "shift"
    while True:
        raw = input(f"\nKey to press (press Enter for default '{default}'): ").strip()
        if not raw:
            return default
        if raw in pyautogui.KEYBOARD_KEYS:
            return raw
        print(f"'{raw}' is not a valid key. Try again.")

def run(key, interval):
    print(f"\nRunning — pressing '{key}' every {interval}s. Ctrl+C to stop.\n")
    press_count = 0
    try:
        while True:
            # random hold between 30–80ms so it doesn't look robotic
            hold = random.uniform(0.03, 0.08)
            pyautogui.keyDown(key)
            time.sleep(hold)
            pyautogui.keyUp(key)
            press_count += 1
            print(f"[{press_count}] Pressed '{key}' — next in {interval}s", end="\r", flush=True)
            time.sleep(max(0.1, interval + random.uniform(-0.5, 0.5)))
    except KeyboardInterrupt:
        pyautogui.keyUp(key)  # release in case we're interrupted mid-hold
        print(f"\n\nStopped after {press_count} keypresses. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    print("=== AFK Preventer ===")
    check_os()
    interval = get_interval()
    key = get_key()
    run(key, interval)