import argparse
import pathlib
import numpy as np
import cv2
import time
import threading

import torch
import torch.nn as nn
from torch.autograd import Variable
from torchvision import transforms
import torch.backends.cudnn as cudnn
import torchvision

from PIL import Image
from PIL import Image, ImageOps
import interface_v2
import mouse_click
import mouseV2
import pyautogui


from face_detection import RetinaFace

from l2cs import select_device, draw_gaze, getArch, Pipeline, render

CWD = pathlib.Path.cwd()

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(
        description='Gaze evalution using model pretrained with L2CS-Net on Gaze360.')
    parser.add_argument(
        '--device',dest='device', help='Device to run model: cpu or gpu:0',
        default="cpu", type=str)
    parser.add_argument(
        '--snapshot',dest='snapshot', help='Path of model snapshot.', 
        default='output/snapshots/L2CS-gaze360-_loader-180-4/_epoch_55.pkl', type=str)
    parser.add_argument(
        '--cam',dest='cam_id', help='Camera device id to use [0]',  
        default=0, type=int)
    parser.add_argument(
        '--arch',dest='arch',help='Network architecture, can be: ResNet18, ResNet34, ResNet50, ResNet101, ResNet152',
        default='ResNet50', type=str)

    args = parser.parse_args()
    return args


#CLICK ATUAL: 2 SEGUNDOS PARADO NA MESMA POSIÇÃO

#                   IDEIAS PARA O CLICK
#BOTÃO NO MEIO
#PEGAR AS ULTIMAS COORDENADAS IMEDIATAMENTE APÓS O MOUSE IR PARA O BOTÃO DO MEIO





if __name__ == '__main__':
    args = parse_args()
    avg_fps = []
    cudnn.enabled = True
    arch=args.arch
    cam = args.cam_id
    # snapshot_path = args.snapshot
    print(CWD)
    gaze_pipeline = Pipeline(
        weights=CWD / 'models' / 'L2CSNet_gaze360.pkl',
        arch='ResNet50',
        device=torch.device('cuda') #cpu or cuda
    )

    '''
    # Calculate the region coordinates
    screen_width, screen_height = pyautogui.size()
    region_width = 300  # 150 pixels on each side
    region_height = 300  # 150 pixels on each side
    region_x = (screen_width - region_width) // 2
    region_y = (screen_height - region_height) // 2
    # Define the region where you want to monitor the mouse (x, y, width, height)
    region = (region_x, region_y, region_width, region_height)
    # Instantiate and start the mouse monitor
    mouse_monitor = mouseV2.MouseMonitor(region, idle_time=3)
    mouse_monitor.start()
    '''
    #interface_tela = threading.Thread(target=interface_v2.tela)
    #interface_tela.start()

    #mouse_monitor = mouse_click.MouseMonitor(idle_time=2)
    #mouse_monitor.start()

    #FIXAR FPS
    #ADICIONAR BLUR NO FUNDO COM CV2
    print("INTERFACE OK")
    cap = cv2.VideoCapture(cam)
    cap.set(cv2.CAP_PROP_FPS, 12)
    print(cap.get(cv2.CAP_PROP_FPS))
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    else:
        print("Webcam OK")
    with torch.no_grad():
        #while interface_tela.is_alive(): #enquanto o programa roda ...
        while True:
            # Get frame
            success, frame = cap.read()
            start_fps = time.time()  

            if not success:
                print("Failed to obtain frame")
                time.sleep(0.1)

            # Process frame
            results = gaze_pipeline.step(frame)

            # Visualize output
            frame = render(frame, results)

            myFPS = 1.0 / (time.time() - start_fps)
            avg_fps.append(myFPS)

            cv2.putText(frame, 'FPS: {:.1f}'.format(myFPS), (10, 20),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1, cv2.LINE_AA)

            cv2.imshow("Visualizacao",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            success,frame = cap.read()  



#mouse_monitor.stop()
avg_fps = np.array(avg_fps)
print("AVERAGE FPS: ", np.mean(avg_fps))