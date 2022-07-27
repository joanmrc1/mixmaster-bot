import time
from config_pyautogui import pyautogui, os
from helper import move_to_location


def login_exec():
    pyautogui.press('win')
    pyautogui.write('mix')
    pyautogui.press('enter')

    time.sleep(3)

    pyautogui.write(os.getenv('LOGIN'))
    pyautogui.press('tab')
    pyautogui.write(os.getenv('PASSWORD'))
    pyautogui.press('enter')

    move_to_location('./imagens/launcher/iniciar_button.png')
    pyautogui.click(clicks=1)
