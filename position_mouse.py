import time
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 1

time.sleep(2)
position = pyautogui.position()
print(position)
