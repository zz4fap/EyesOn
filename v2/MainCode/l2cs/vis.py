import cv2
import numpy as np
from .results import GazeResultContainer
import pyautogui as pag

#PULAR DE LETRA EM LETRA
#tentar fazer com interface também
#
def inKeyCalc(x, y, left, right, bottom, top, center):
    if left:
        pag.moveTo(x - 30, y)
    elif right:
        pag.moveTo(x + 30, y)
    elif bottom:
        pag.moveTo(x, y + 30)
    elif top:
        pag.moveTo(x, y - 30)
    elif center:
        print("Centro")

#FAZER A MÉDIA DE VALORES DO VETOR -> DIMINUIR RUIDO
def inInterface(x, y, left, right, bottom, top, center, center_all):
    if center_all:
        print("CENTER_ALL")
    elif center and top:
        print("CENTRO BOT")
        if x != 750 or y != 225:
            pag.moveTo(750, 225)
    elif center and bottom:
        print("CENTRO TOP")
        if x != 750 or y != 675:
            pag.moveTo(750, 675)
    elif left and top:
        print("ESQUERDA SUPERIOR")
        if x != 160 or y != 225:
            pag.moveTo(160, 225)
    elif left and bottom:
        print("ESQUERDA INFERIOR")
        if x != 160 or y != 675:
            pag.moveTo(160, 675)
    elif right and top:
        print("DIREITA SUPERIOR")
        if x != 1300 or y != 225:
            pag.moveTo(1300, 225)

#usar TIME PARA MEDIR TEMPO da função
#dividir a função em funções menores

#TENTAR LIMITAR EM 1 MOVIMENTO POR SEGUNDO

dx_l = np.random.rand(5).tolist()
dy_l = np.random.rand(5).tolist()
def draw_gaze(a,b,c,d,image_in, pitchyaw, thickness=2, color=(255, 255, 0),scale=1.7, dx_l=dx_l, dy_l=dy_l):
    """Draw gaze angle on given image with a given eye positions."""
    image_out = image_in
    (h, w) = image_in.shape[:2]
    length = c * scale #I CAN RESCALE THE ARROW
    pos = (int(a+c / 2.0), int(b+d / 2.0))
    if len(image_out.shape) == 2 or image_out.shape[2] == 1:
        image_out = cv2.cvtColor(image_out, cv2.COLOR_GRAY2BGR)
    dx = -length * np.sin(pitchyaw[0]) * np.cos(pitchyaw[1])
    dy = -length * np.sin(pitchyaw[1])

    dx_l.pop(0)  # Remove the first element
    dy_l.pop(0)

    dx_l.append(dx)  # Append a new random value
    dy_l.append(dy)

    dx_mean = np.mean(dx_l)
    dy_mean = np.mean(dy_l)

    #print(f"dx = {dx} /// dy = {dy}")
    print(f"dx = {dx_mean} /// dy = {dy_mean}")

    center = False
    center_all = False
    right = False
    left = False
    top = False
    bottom = False

    #center_all = botão no centro para fazer o click ?

    x, y = pag.position()
    if dx_mean >= 20:
        left = True
    elif dx_mean <= -20:
        right = True
    else:
        center = True
    if dy_mean <= 40:
        top = True
    elif dy_mean >= 88:
        bottom = True
    if dx_mean < 20 and dx_mean > -20 and dy_mean < 88 and dy_mean > 28:
        center_all = True

    #X
    #1 -> 320
    #2 -> 960
    #3 -> 1600

    #Y
    #1 -> 270
    #2 -> 810
    if center_all:
        print("CENTER_ALL")
    elif right:
        print("RIGHT")
        if x + 640 < 1900:
            pag.moveTo(x + 640, y)
    elif left:
        print("LEFT")
        if x - 640 > 100:
            pag.moveTo(x - 640, y)
    elif top:
        print("TOP")
        if y - 540 > 100:
            pag.moveTo(x, y - 540)
    elif bottom:
        print("BOTTOM")
        if y + 540 < 1000:
            pag.moveTo(x, y + 540)



    cv2.arrowedLine(image_out, tuple(np.round(pos).astype(np.int32)),
                   tuple(np.round([pos[0] + dx_mean, pos[1] + dy_mean]).astype(int)), color,
                   thickness, cv2.LINE_AA, tipLength=0.18)
    return dx_l, dy_l, image_out  #esse return não importa o que retorna

    #FUNÇÃO INTERIOR PARA COLETAR AS DIREÇÕES
    #get_direcoes(left, right, top, bottom, center, center_all)

    #enquanto centro - contagem

    #dx > 0 -> OLHANDO PARA A DIREITA
    #dx < 0 -> OLHANDO PARA A ESQUERDA

    #dy < 0 -> OLHANDO PARA BAIXO
    #dy > 0 -> OLHANDO PARA CIMA


def draw_bbox(frame: np.ndarray, bbox: np.ndarray):
    x_min = int(bbox[0])
    if x_min < 0:
        x_min = 0
    y_min = int(bbox[1])
    if y_min < 0:
        y_min = 0
    x_max = int(bbox[2])
    y_max = int(bbox[3])

    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 1)

    return frame


def render(frame: np.ndarray, results: GazeResultContainer):
    # Draw bounding boxes
    for bbox in results.bboxes:
        frame = draw_bbox(frame, bbox)

    # Draw Gaze
    for i in range(results.pitch.shape[0]):

        bbox = results.bboxes[i]
        pitch = results.pitch[i]
        yaw = results.yaw[i]

        # Extract safe min and max of x,y
        x_min = int(bbox[0])
        if x_min < 0:
            x_min = 0
        y_min = int(bbox[1])
        if y_min < 0:
            y_min = 0
        x_max = int(bbox[2])
        y_max = int(bbox[3])

        # Compute sizes
        bbox_width = x_max - x_min
        bbox_height = y_max - y_min

        draw_gaze(x_min, y_min, bbox_width, bbox_height, frame, (pitch, yaw), color=(0, 0, 255))

    return frame