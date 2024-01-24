import pyautogui
import pygetwindow as gw

import utils.keyboard_interaction as ki
from utils.keys import hex_key

def active_roblox_window():
    try:
        roblox_window = gw.getWindowsWithTitle('Roblox')[0]

        left = roblox_window.left
        top = roblox_window.top
        width = roblox_window.width
        height = roblox_window.height

        pyautogui.click(left + width / 2, top + height / 2)
    except IndexError:
        print("Roblox window not found")

def move_around_yourself():
    ki.pressKey(hex_key.get('w'), 0.3)
    ki.pressKey(hex_key.get('a'), 0.3)
    ki.pressKey(hex_key.get('s'), 0.3)
    ki.pressKey(hex_key.get('d'), 0.3)

def move():
    active_roblox_window()
    move_around_yourself()

move()
