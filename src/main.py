import pyautogui
import pygetwindow as gw
import time

def download_mod():
    try:
      window = gw.getWindowsWithTitle('Browser Window')[0]
      image = 'src/images/button.png'
      x, y, _, _ = pyautogui.locateOnScreen(image, region=(window.left, window.top, window.width, window.height))
      print(f"Download button found x={x}, y={y}")

      pyautogui.click(x, y)
    except pyautogui.ImageNotFoundException:
      print("Download button not found")
    except IndexError:
      print("Nexus window not found")


while True:
    download_mod()
    print("Waiting for the download window..")
    time.sleep(8)
