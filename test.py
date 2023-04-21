import pyautogui, time

# Captura a região da tela
region = pyautogui.locateOnScreen('a.png', confidence=0.8)

while True:
    time.sleep(0.2)
    # Verifica se a região foi encontrada
    if region is not None:
        # Obtém as coordenadas da parte superior esquerda da região
        x, y = pyautogui.position(region)
        print(f"Coordenadas da região encontrada: ({x}, {y})")
    else:
        print("Região não encontrada na tela")