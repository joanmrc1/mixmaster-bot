import time
import os
import pyautogui
from dotenv import load_dotenv

load_dotenv()

MAX_RETRIES = int(os.getenv('RETRYS_IMAGENS_LOCATIONS'))


def move_to_location(image_location, click=False):
    """Move o mouse até o local usando imagem.

    Args:
      image_location (string): Url path da imagem para localizar na tela.
    Returns:
      None
    """

    for _ in range(MAX_RETRIES):
        # time.sleep(3)
        print('opa1', image_location)
        try:
            pyautogui.moveTo(image_location)
            if click is True:
                mouse_click(pyautogui.position())
            print('SUCESSO')
            break
        except TypeError:
            print("Imagem não encontrada [",
                  image_location, "]. Tente novamente.")
            continue
    print("Fatal Error: Imagem não encontrada [", image_location,
          "] depois de ", MAX_RETRIES, " tentativas.")


def mouse_click(x=None, y=None, left_click=False, clicks = 1):
    """Move o mouse até o local coordernadas x e y.

    Args:
        x (int, float, none): Parametro para definir eixo x.
        y (int, float, none): Parametro para definir eixo y.
        interval (int, float): Url path da imagem para localizar na tela.
    Returns:
      None
    """

    if x is not None and y is not None:
        pyautogui.moveTo(x, y)

    if left_click is True:
        mouse_right_click()

    for _ in range(clicks):
        pyautogui.mouseDown()
        pyautogui.mouseUp()


def mouse_right_click():
    pyautogui.mouseDown(button='right')
    pyautogui.mouseUp(button='right')


def press_keyboard(key='p'):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
