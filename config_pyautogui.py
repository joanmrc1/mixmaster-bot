import os
from dotenv import load_dotenv
import pyautogui

load_dotenv()

pyautogui.FAILSAFE = False
pyautogui.PAUSE = float(os.getenv('PAUSE_INTERVAL'))
