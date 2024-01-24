import pyautogui
import pygetwindow as gw
import time

import utils.keyboard_interaction as ki
from utils.keys import hex_key

FIFTEEN_MINUTES = 900

def active_roblox_window():
    try:
        roblox_window = gw.getWindowsWithTitle('Roblox')[1]

        left = roblox_window.left
        top = roblox_window.top
        width = roblox_window.width
        height = roblox_window.height

        pyautogui.click(left + width / 2, top + height / 2)
    except IndexError:
        print("Roblox window not found")

def move_around_yourself():
    ki.pressKey(hex_key.get('W'), 0.3)
    ki.pressKey(hex_key.get('A'), 0.3)
    ki.pressKey(hex_key.get('S'), 0.3)
    ki.pressKey(hex_key.get('D'), 0.3)

def move_character_each_15_minutes():
    while True:
        print("Getting active roblox window")
        active_roblox_window()
        print("Moving character")
        move_around_yourself()

        print("Waiting 15 minutes for next move...")
        time.sleep(FIFTEEN_MINUTES)

move_character_each_15_minutes()
