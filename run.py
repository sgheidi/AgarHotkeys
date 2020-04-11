from pynput.keyboard import Key, Listener
import pyautogui
from win32api import GetSystemMetrics

def on_press(key):
    print('{0} pressed'.format(
        key))
    if key == Key.shift_l:
      pyautogui.moveTo((GetSystemMetrics(0)//2)+1, (GetSystemMetrics(1)//2) + 1)

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
