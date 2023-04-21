import os
from dotenv import load_dotenv
import pyautogui
from helper import *

load_dotenv()

pyautogui.FAILSAFE = False
#pyautogui.PAUSE = float(os.getenv('PAUSE_INTERVAL'))
