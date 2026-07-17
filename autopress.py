import pyautogui
import time

# settings, interval in seconds
key = "space"          
interval = 1.0         


print("Auto key press script started")
print(f"Pressing '{key}' every {interval} seconds.")
print("Switch to your target window now...")
print("Press Ctrl + C in this terminal to stop.")

time.sleep(3)  # 3 seconds to switch windows

try:
    while True:
        pyautogui.press(key)
        print(f"Pressed {key}")
        time.sleep(interval)
except KeyboardInterrupt:
    print("\nScript stopped.")