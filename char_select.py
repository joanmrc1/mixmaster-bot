import time
from config_pyautogui import pyautogui, move_to_location

INTERVAL_CLICKS = 0.5
TIME_SLEEP = 1


def select_serve():
    move_to_location('./imagens/serve/serve_draco.png')
    pyautogui.doubleClick(interval=INTERVAL_CLICKS)


def select_char():
    time.sleep(TIME_SLEEP)
    pyautogui.moveTo(1445, 551)
    pyautogui.click()


def select_start():
    time.sleep(TIME_SLEEP)
    move_to_location('./imagens/select_char/entrar.png')
    pyautogui.doubleClick(interval=INTERVAL_CLICKS)


def char_exec():
    select_serve()
    select_char()
    select_start()
