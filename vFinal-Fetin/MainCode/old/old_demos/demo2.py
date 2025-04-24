import argparse
import pathlib
import numpy as np
import cv2
import time
import threading
import dlib

import torch
import torch.backends.cudnn as cudnn

import interface_v2
import pyautogui as pag

import old.calc_thread
from l2cs import vis

from l2cs import Pipeline, render
import calculadora
import teclado
import interface_google
import mouse_click_general
import mouse_click_browser
import mouse_click_general_teste
from old import calc_thread
import interface_google
import home
from vision_click import click



#TECLADO PRIMEIRO PLANO GOOGLE
#ADICIONAR INTERFACE YOUTUBE
#REMOVER ALTERNAR TECLADO E AUMENTAR ENTER


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
    #face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # snapshot_path = args.snapshot
    #print(CWD)
    gaze_pipeline = Pipeline(
        weights=CWD / 'models' / 'L2CSNet_gaze360.pkl',
        arch='ResNet50',
        device=torch.device('cuda') #cpu or cuda
    )

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    flag_click = False #false -> click general /// True -> click browser
    interface_tela = threading.Thread(target=home.tela)

    #mouse_monitor_general = mouse_click_general.MouseMonitor_general(general_time=3)
    #mouse_monitor_browser = mouse_click_browser.MouseMonitor_browser(browse_time=3)
    #mouse_teste = mouse_click_general_teste.MouseMonitor_teste(browse_on=False)

    #FIXAR FPS
    pag.moveTo(320, 270)
    cap = cv2.VideoCapture(cam)

    cap.set(cv2.CAP_PROP_FPS, 12) #NÃO COMENTAR NEM REMOVER ESSA LINHA
    #print(cap.get(cv2.CAP_PROP_FPS))

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    else:
        print("Webcam OK")
        #interface_tela.start()
        print("INTERFACE OK")
        #mouse_teste.start()
        click.run_click_thread(detector, predictor, frame)
        print("MOUSE CLICK OK")
    with torch.no_grad():
        #while interface_tela.is_alive(): #enquanto o programa roda ...
        while True:
            # Get frame
            success, frame = cap.read()
            start_fps = time.time()

            if not success:
                print("Failed to obtain frame")
                time.sleep(0.1)

            #FAZENDO O CLICK DO MOUSE
            # Process frame
            results = gaze_pipeline.step(frame) #calc é feito
            try:
                vis.move_cursor(results, teclado.keyb_thread_on, calculadora.calc_thread_on, interface_google.interface_google_on)
            except:
                print("0 FACES DETECTADAS")

            #print(teclado.keyb_thread_on)
            #print(calculadora.calc_thread_on)
            # Visualize output
            frame = render(frame, results)
            #_, frame2 = render(frame, results)


            myFPS = 1.0 / (time.time() - start_fps)
            avg_fps.append(myFPS)

            cv2.putText(frame, 'FPS: {:.1f}'.format(myFPS), (10, 20),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1, cv2.LINE_AA)

            cv2.imshow("frame1",frame)
            #cv2.imshow("frame2", frame2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            success,frame = cap.read()
        cap.release()


avg_fps = np.array(avg_fps)
#mouse_monitor_general.stop()
print("AVERAGE FPS: ", np.mean(avg_fps))