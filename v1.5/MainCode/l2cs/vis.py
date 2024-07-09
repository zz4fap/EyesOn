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
def draw_gaze(a,b,c,d,image_in, pitchyaw, thickness=2, color=(255, 255, 0),scale=1.7, ign=False):
    """Draw gaze angle on given image with a given eye positions."""
    image_out = image_in
    (h, w) = image_in.shape[:2]
    length = c * scale #I CAN RESCALE THE ARROW
    pos = (int(a+c / 2.0), int(b+d / 2.0))
    if len(image_out.shape) == 2 or image_out.shape[2] == 1:
        image_out = cv2.cvtColor(image_out, cv2.COLOR_GRAY2BGR)
    dx = -length * np.sin(pitchyaw[0]) * np.cos(pitchyaw[1])
    dy = -length * np.sin(pitchyaw[1])
    #print(f"dx = {dx} /// dy = {dy}")

    center = False
    center_all = False
    right = False
    left = False
    top = False
    bottom = False

    #center_all = botão no centro para fazer o click ?

    x, y = pag.position()
    if dx >= 20:
        left = True
    elif dx <= -20:
        right = True
    else:
        center = True
    if dy <= 5:
        top = True
    elif dy >= 40:
        bottom = True
    if dx < 20 and dx > -20 and dy < 40 and dy > 5:
        center_all = True

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
    elif right and bottom:
        print("DIREITA INFERIOR")
        if x != 1300 or y != 675:
            pag.moveTo(1300, 675)

    #FUNÇÃO INTERIOR PARA COLETAR AS DIREÇÕES
    #get_direcoes(left, right, top, bottom, center, center_all)

    #enquanto centro - contagem

    #dx > 0 -> OLHANDO PARA A DIREITA
    #dx < 0 -> OLHANDO PARA A ESQUERDA

    #dy < 0 -> OLHANDO PARA BAIXO
    #dy > 0 -> OLHANDO PARA CIMA

    cv2.arrowedLine(image_out, tuple(np.round(pos).astype(np.int32)),
                   tuple(np.round([pos[0] + dx, pos[1] + dy]).astype(int)), color,
                   thickness, cv2.LINE_AA, tipLength=0.18)
    return image_out #esse return não importa o que retorna

def draw_bbox(frame: np.ndarray, bbox: np.ndarray):
    
    x_min=int(bbox[0])
    if x_min < 0:
        x_min = 0
    y_min=int(bbox[1])
    if y_min < 0:
        y_min = 0
    x_max=int(bbox[2])
    y_max=int(bbox[3])

    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0,255,0), 1)

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
        x_min=int(bbox[0])
        if x_min < 0:
            x_min = 0
        y_min=int(bbox[1])
        if y_min < 0:
            y_min = 0
        x_max=int(bbox[2])
        y_max=int(bbox[3])

        # Compute sizes
        bbox_width = x_max - x_min
        bbox_height = y_max - y_min

        draw_gaze(x_min,y_min,bbox_width, bbox_height,frame,(pitch,yaw),color=(0,0,255))

    return frame
