import pyautogui as pag
import time as t

def moveOnScreen(direcao):
    match direcao:
        #ESQUERDA SUPERIOR
        case 0:
            pag.moveTo(360, 225)
        #ESQUERDA INFERIOR
        case 1:
            pag.moveTo(360, 675)
        #DIREITA INFERIOR
        case 2:
            pag.moveTo(1080, 225)
        #DIREITA SUPERIOR
        case 3:
            pag.moveTo(1080, 675)
        case _:
            print("direção invalida")
#1440 x 900
while True:
    print("TYPE")
    x = int(input())
    moveOnScreen(x)
    print("OK")