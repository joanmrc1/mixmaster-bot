import threading
import time
from datetime import datetime
from config_pyautogui import pyautogui, mouse_click, press_keyboard, image_in_screen

INTERVAL_CLICKS = 0.5
TIME_SLEEP = 1

SUPERIOR_ESQUERDA = [825, 253]
INFERIOR_ESQUERDA = [787, 783]
SUPERIOR_DIREITO = [1714, 263]
INFERIOR_DIREITA = [1722, 783]
ICREMENTO_EIXO_X = 30
ICREMENTO_EIXO_Y = 45

LIMIT_DOWN_VIEW = 679

JAULA_50 = [
    ['./imagens/cores/jaula_50/MixMaster_4.png', './imagens/cores/jaula_50/MixMaster_5.png',
        './imagens/cores/jaula_50/MixMaster_6.png', './imagens/cores/jaula_50/MixMaster_7.jpg'],
    ['./imagens/cores/jaula_50/MixMaster_8.jpg', './imagens/cores/jaula_50/MixMaster_9.jpg',
     './imagens/cores/jaula_50/MixMaster_10.jpg', './imagens/cores/jaula_50/MixMaster_11.jpg'],
    ['./imagens/cores/jaula_50/MixMaster_12.jpg', './imagens/cores/jaula_50/MixMaster_13.jpg',
     './imagens/cores/jaula_50/MixMaster_14.jpg'],
    ['./imagens/cores/jaula_50/MixMaster_15.jpg',
     './imagens/cores/jaula_50/MixMaster_16.jpg']
]

JAULA_70 = [
    [
        './imagens/cores/jaula_70/MixMaster_1.jpg', 
        './imagens/cores/jaula_70/MixMaster_2.jpg',
        './imagens/cores/jaula_70/MixMaster_3.jpg'
    ],
    [
        './imagens/cores/jaula_70/MixMaster_4.jpg', 
        './imagens/cores/jaula_70/MixMaster_5.jpg',
        './imagens/cores/jaula_70/MixMaster_6.jpg'
    ],
    [
        './imagens/cores/jaula_70/MixMaster_7.jpg',
        './imagens/cores/jaula_70/MixMaster_8.jpg'
    ],
    [
        './imagens/cores/jaula_70/MixMaster_9.jpg', 
        './imagens/cores/jaula_70/MixMaster_10.jpg',
        './imagens/cores/jaula_70/MixMaster_11.jpg', 
        './imagens/cores/jaula_70/MixMaster_12.jpg'
    ],
    [
        './imagens/cores/jaula_70/MixMaster_13.jpg', 
        './imagens/cores/jaula_70/MixMaster_14.jpg',
        './imagens/cores/jaula_70/MixMaster_15.jpg', 
        './imagens/cores/jaula_70/MixMaster_16.jpg'
    ]
]

JAULA_150 = [['./imagens/cores/jaula_150/MixMaster_3.jpg',
              './imagens/cores/jaula_150/MixMaster_4.jpg',
              './imagens/cores/jaula_150/MixMaster_5.jpg']]

JAULA_125 = [
    [
        './imagens/cores/jaula_125/MixMaster_1.jpg',
        './imagens/cores/jaula_125/MixMaster_2.jpg',
    ],
    [
        './imagens/cores/jaula_150/MixMaster_3.jpg',
        './imagens/cores/jaula_125/MixMaster_4.jpg',
        './imagens/cores/jaula_125/MixMaster_5.jpg'
    ],
    [
        './imagens/cores/jaula_125/MixMaster_6.jpg',
        './imagens/cores/jaula_125/MixMaster_7.jpg',
        './imagens/cores/jaula_125/MixMaster_8.jpg'
    ],
    [
        './imagens/cores/jaula_125/MixMaster_9.jpg',
        './imagens/cores/jaula_125/MixMaster_10.jpg'
    ],
    [
        './imagens/cores/jaula_125/MixMaster_11.jpg',
        './imagens/cores/jaula_125/MixMaster_12.jpg'
    ]
]
#pyautogui.PAUSE = 0.11
pyautogui.FAILSAFE = False

date_execution_inital = datetime.now()


def auto_attack_sequence():
    # eixo_x, eixo_y, status = [825, 253, 'DIREITA']
    eixo_x, eixo_y, status = [855, 748, 'ESQUERDA']
    time.sleep(1.5)

    # Posição INICIAL
    pyautogui.moveTo(x=SUPERIOR_ESQUERDA[0], y=SUPERIOR_ESQUERDA[1])

    while True:
        if status == 'DIREITA':
            time.sleep(0.2)
            x, y = pyautogui.position()
            pyautogui.moveTo(eixo_x, eixo_y)
            mouse_click()
            if eixo_x >= SUPERIOR_DIREITO[0]:
                print('ola2')
                status = 'ESQUERDA'
                eixo_y += ICREMENTO_EIXO_Y
                continue
            if y > INFERIOR_DIREITA[1]:
                eixo_x, eixo_y = [787, 253]
                print('ola1')
            eixo_x += ICREMENTO_EIXO_X

            print('eixo_x: ', eixo_x, 'position x: ', x,
                  'eixo_y: ', eixo_y, 'position y: ', y, 'status', status)
        if status == 'ESQUERDA':
            time.sleep(0.2)
            x, y = pyautogui.position()
            pyautogui.moveTo(eixo_x, eixo_y)
            mouse_click()
            print('valor antes: ', eixo_x)
            eixo_x -= ICREMENTO_EIXO_X

            if eixo_x <= SUPERIOR_ESQUERDA[0]:
                print('Incrementa y')
                print('valor depois: ', eixo_x)
                status = 'DIREITA'
                eixo_y += ICREMENTO_EIXO_Y
                continue
            if eixo_y > INFERIOR_ESQUERDA[1]:
                eixo_x, eixo_y = [787, 253]

            print('eixo_x: ', eixo_x, 'position x: ', x,
                  'eixo_y: ', eixo_y, 'position y: ', y, 'status', status)


def auto_attack_by_images(images):
    date_execution_inital_local = datetime.now()
    while True:
        if (datetime.now() - date_execution_inital_local).seconds > 9500:
            use_mark()
            print('Marca resetada!')
            date_execution_inital_local = datetime.now()
        for image in images:
            for i in image:
                time.sleep(0.1)
                locale = pyautogui.locateOnScreen(i, confidence=0.52)
                if locale is not None:
                    position_mouse = pyautogui.center(locale)
                    if position_mouse.y < LIMIT_DOWN_VIEW:
                        print('SUCESSO -> ', i)
                        pyautogui.moveTo(position_mouse)
                        mouse_click()
                        


def auto_attack(images):  # [['path...']]
    while True:
        time.sleep(1)

        reset_mark()

        for image in images:  # ->[[]]
            print('1')
            time.sleep(0.5)
            while image_in_screen([
                './imagens/screens/MixMaster_3.jpg',
                './imagens/screens/MixMaster_4.jpg',
                './imagens/screens/MixMaster_5.jpg']
            ) is True:
                print('ACHOOU (1)', datetime.now().second)
                time.sleep(1)
            time.sleep(0.1)
            for i in image:  # [->[]]
                print('2')
                time.sleep(0.5)
                while pyautogui.locateOnScreen('./imagens/screens/MixMaster_3.jpg', confidence=0.6) is not None:
                    print('ACHOOU (2)', datetime.now().second)
                    time.sleep(2)

                locale = pyautogui.locateOnScreen(i, confidence=0.6)  # old 0.6

                if locale is not None:
                    position_mouse = pyautogui.center(locale)
                    print('3', datetime.now().second)
                    if position_mouse.y < LIMIT_DOWN_VIEW:
                        print('SUCESSO -> ', i)
                        pyautogui.moveTo(position_mouse)
                        mouse_click()


def get_position():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')


def execute_attack_by_thered():
    thread_auto_attack = threading.Thread(target=auto_attack_by_images,)
    thread_auto_attack.start()


def reset_mark():
    global date_execution_inital
    if (datetime.now() - date_execution_inital).seconds > 10800:
        use_mark()
        print('Marca resetada!')
        date_execution_inital = datetime.now()


def use_mark():
    try:
        press_keyboard('u')  # Abrir invetário
        time.sleep(1)
        pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen(
            './imagens/bag/mark.jpg', confidence=0.7)))
        mouse_click(clicks=2)
        time.sleep(1)
        pyautogui.moveTo(pyautogui.center(pyautogui.locateOnScreen(
            './imagens/confirmations/confirme.jpg', confidence=0.7)))
        mouse_click()
    except:
        press_keyboard('u')  # Fechar invetário

auto_attack_by_images(JAULA_70)