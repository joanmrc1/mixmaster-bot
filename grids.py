import time
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.5

def select_npc():
    time.sleep(3)
    pyautogui.moveTo('./imagens/npcs/npc_jaula.png')
    pyautogui.click()


def select_grid():
    time.sleep(3)
    pyautogui.moveTo('./imagens/grid/grid_100.png')
    pyautogui.click()


def go_to_grid_1():  # Primeira jaula

    while bool(1):
        pyautogui.moveTo(pyautogui.position())
        pyautogui.mouseDown()
        time.sleep(0.5) #or whatever you need, if even needed
        pyautogui.mouseUp()
        #pyautogui.doubleClick(pyautogui.position(), interval=0.5)
        #pyautogui.click(pyautogui.position())
        #print(pyautogui.position())
    # while bool(1):
    #     time.sleep(1)
    #     try:
    #         pyautogui.moveTo('./imagens/cores/amarelo.png')
    #         break;
    #     except:
    #       print("Unable to find. Trying again")
    # pyautogui.click()

    pyautogui.doubleClick()
    # pyautogui.doubleClick(x=814, y=774,interval= 0.5)
    # pyautogui.doubleClick(x=978, y=337,interval= 0.5)
    # pyautogui.doubleClick(x=999, y=306,interval= 0.5)
    # pyautogui.press('p')


def grid_exec():
    select_npc()
    select_grid()
    #go_to_grid_1()
