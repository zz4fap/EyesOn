import cv2
import numpy as np
from .results import GazeResultContainer
import pyautogui as pag
import time

#PULAR DE LETRA EM LETRA
#tentar fazer com interface também


#usar TIME PARA MEDIR TEMPO da função
#dividir a função em funções menores

#TENTAR LIMITAR EM 1 MOVIMENTO POR SEGUNDO

dx_global = 0
dy_global = 0

last_execution_time = 0
dx_l = np.random.rand(5).tolist()
dy_l = np.random.rand(5).tolist()
def calc_dx_dy(a,b,c,d,pitchyaw,scale=1.7):
    global dx_global, dy_global
    length = c * scale #I CAN RESCALE THE ARROW
    pos = (int(a+c / 2.0), int(b+d / 2.0))
    dx = -length * np.sin(pitchyaw[0]) * np.cos(pitchyaw[1])
    dy = -length * np.sin(pitchyaw[1])

    dx_l.pop(0)
    dy_l.pop(0)

    dx_l.append(dx)
    dy_l.append(dy)

    dx_mean = np.mean(dx_l)
    dy_mean = np.mean(dy_l)

    dx_global = dx_mean
    dy_global = dy_mean

    return dx_mean, dy_mean

coord_x_list = np.random.rand(3).tolist()
coord_y_list = np.random.rand(3).tolist()
def move_cursor(results: GazeResultContainer, kb_t, calc_t, google_t, pos_x, pos_y):
    global last_execution_time
    current_time = time.time()

    #print(f"dx = {dx_mean} /// dy = {dy_mean}")
    center_all = False
    right = False
    left = False
    top = False
    bottom = False

    coord_x_list.pop(0)
    coord_y_list.pop(0)

    coord_x_list.append(pos_x)
    coord_y_list.append(pos_y)

    coord_x = np.mean(coord_x_list)
    coord_y = np.mean(coord_y_list)

#calibração puxando informações de um csv ou notepad
    limit_right = 1520
    limit_left = 400
    limit_top = 280
    limit_bot = 800

    x, y = pag.position()
    if coord_x > limit_left and coord_x < limit_right and coord_y < limit_bot and coord_y > limit_top:
        center_all = True
    elif coord_x <= limit_left:
        left = True
    elif coord_x >= limit_right:
        right = True
    elif coord_y <= limit_top:
        top = True
    elif coord_y >= limit_bot:
        bottom = True
    #print(coord_x, coord_y)


    #X
    #1 -> 320
    #2 -> 960
    #3 -> 1600

    #Y
    #1 -> 270
    #2 -> 810
    px, py = 0, 0
    if kb_t:
        interface_geral = False
        px = 160
        py = 150
    elif calc_t:
        interface_geral = False
        px = 480
        py = 160
    elif google_t:
        interface_geral = False
        px = 475
        py = 0
    else:
        interface_geral = True
        px = 485
        py = 320
    if current_time - last_execution_time >= 0.5: #a cada x segundos é possível fazer um movimento com o cursor
        last_execution_time = current_time
        if interface_geral:
            if center_all:
                print("CENTER_ALL")
            elif right:
                print("RIGHT")
                if x + px < 1600:
                    pag.moveTo(x + px, y)
            elif left:
                print("LEFT")
                if x - px > 1000:
                    pag.moveTo(x - px, y)
            if top:
                print("TOP")
                if y - py > 260:
                    pag.moveTo(x, y - py)
            elif bottom:
                print("BOTTOM")
                if y + py < 910:
                    pag.moveTo(x, y + py)
        else:
            if center_all:
                print("CENTER_ALL")
            elif right:
                print("RIGHT")
                if x + px < 1920:
                    pag.moveTo(x + px, y)
            elif left:
                print("LEFT")
                if x - px > 10:
                    pag.moveTo(x - px, y)
            if top:
                print("TOP")
                if y - py > 10:
                    pag.moveTo(x, y - py)
            elif bottom:
                print("BOTTOM")
                if y + py < 1080:
                    pag.moveTo(x, y + py)


#


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

    dx_l.pop(0)
    dy_l.pop(0)

    dx_l.append(dx)
    dy_l.append(dy)

    dx_mean = np.mean(dx_l)
    dy_mean = np.mean(dy_l)

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


#        mask = np.zeros_like(frame)
#        mask[y_min:y_min+bbox_height, x_min:x_min+bbox_width] = frame[y_min:y_min+bbox_height, x_min:x_min+bbox_width]
#        blurred_frame = cv2.GaussianBlur(frame, (21, 21), 0)
#        result = np.where(mask != 0, frame, blurred_frame)

        draw_gaze(x_min, y_min, bbox_width, bbox_height, frame, (pitch, yaw), color=(0, 0, 255))
        #draw_gaze(x_min, y_min, bbox_width, bbox_height, result, (pitch, yaw), color=(0, 0, 255))


    return frame#, result
