import cv2
import numpy as np
from .results import GazeResultContainer
import pyautogui as pag
import time
from sklearn.preprocessing import PolynomialFeatures

#PULAR DE LETRA EM LETRA
#tentar fazer com interface também


#usar TIME PARA MEDIR TEMPO da função
#dividir a função em funções menores

#TENTAR LIMITAR EM 1 MOVIMENTO POR SEGUNDO

dx_global = 0
dy_global = 0


last_execution_time = 0
#dx_l = np.random.rand(5).tolist()
#dy_l = np.random.rand(5).tolist()
def calc_dx_dy(a,b,c,d,pitchyaw,scale=1.7):
    global dx_global, dy_global
    length = c * scale #I CAN RESCALE THE ARROW
    pos = (int(a+c / 2.0), int(b+d / 2.0))
    dx = -length * np.sin(pitchyaw[0]) * np.cos(pitchyaw[1])
    dy = -length * np.sin(pitchyaw[1])

    #dx_l.pop(0)
    #dy_l.pop(0)

    #dx_l.append(dx)
    #dy_l.append(dy)

    #dx_mean = np.mean(dx_l)
    #dy_mean = np.mean(dy_l)

    #dx_global = dx_mean
    #dy_global = dy_mean

    return dx, dy

def move_cursor(results: GazeResultContainer, kb_t, calc_t, google_t, model_x, model_y, blink):
    global last_execution_time
    poly = PolynomialFeatures(degree=2)
    current_time = time.time()
    for i in range(results.pitch.shape[0]):
        bbox = results.bboxes[i]
        pitch = results.pitch[i]
        yaw = results.yaw[i]

        #print(pitch, yaw)

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

    ttt = np.array([[results.pitch, results.yaw]])
    if ttt.ndim > 2:
        ttt = ttt.reshape(-1, 2)
    poly.fit(ttt)
    X_test_poly = poly.transform(ttt)

    x_pred = model_x.predict(X_test_poly)
    y_pred = model_y.predict(X_test_poly)
    x_pred = x_pred[0]
    y_pred = y_pred[0]

    #print(x_pred)
    #print(y_pred)
    #print()

# 500 - 1500
# 200 - 800

    center_all = False
    right = False
    left = False
    top = False
    bottom = False

    x, y = pag.position()
    if x_pred > 500 and x_pred < 1500 and y_pred > 200 and y_pred < 800:
        center_all = True
    elif x_pred <= 500:
        left = True
    elif x_pred >= 1500:
        right = True
    elif y_pred <= 200:
        top = True
    elif y_pred >= 800:
        bottom = True
        blink = False

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

    print(blink)
    if current_time - last_execution_time >= 0.5 and not blink: #a cada x segundos é possível fazer um movimento com o cursor
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

    return blink


def draw_gaze(a,b,c,d,image_in, pitchyaw, thickness=2, color=(255, 255, 0),scale=1.7):
    """Draw gaze angle on given image with a given eye positions."""
    image_out = image_in
    (h, w) = image_in.shape[:2]
    length = c * scale #I CAN RESCALE THE ARROW
    pos = (int(a+c / 2.0), int(b+d / 2.0))
    if len(image_out.shape) == 2 or image_out.shape[2] == 1:
        image_out = cv2.cvtColor(image_out, cv2.COLOR_GRAY2BGR)
    dx = -length * np.sin(pitchyaw[0]) * np.cos(pitchyaw[1])
    dy = -length * np.sin(pitchyaw[1])

    #dx_l.pop(0)
    #dy_l.pop(0)

    #dx_l.append(dx)
    #dy_l.append(dy)

    #dx_mean = np.mean(dx_l)
    #dy_mean = np.mean(dy_l)
    cv2.arrowedLine(image_out, tuple(np.round(pos).astype(np.int32)),
                   tuple(np.round([pos[0] + dx, pos[1] + dy]).astype(int)), color,
                   thickness, cv2.LINE_AA, tipLength=0.18)
    return dx, dy, image_out  #esse return não importa o que retorna

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
