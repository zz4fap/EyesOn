import argparse
import pathlib
import numpy as np
import cv2
import time
import threading

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
from old import calc_thread


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


    interface_tela = threading.Thread(target=interface_v2.tela)

    #mouse_monitor = mouse_click.MouseMonitor(idle_time=2)
    #mouse_monitor.start()

    #FIXAR FPS
    #ADICIONAR BLUR NO FUNDO COM CV2
    print("INTERFACE OK")
    pag.moveTo(320, 270)
    cap = cv2.VideoCapture(cam)

    cap.set(cv2.CAP_PROP_FPS, 12) #NÃO COMENTAR NEM REMOVER ESSA LINHA
    #print(cap.get(cv2.CAP_PROP_FPS))

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    else:
        print("Webcam OK")
        interface_tela.start()
    with torch.no_grad():
        #while interface_tela.is_alive(): #enquanto o programa roda ...
        while True:
            # Get frame
            success, frame = cap.read()
            start_fps = time.time()

            if not success:
                print("Failed to obtain frame")
                time.sleep(0.1)

            #APLICAR O BLUR AQUI

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



#mouse_monitor.stop()
avg_fps = np.array(avg_fps)
print("AVERAGE FPS: ", np.mean(avg_fps))

'''
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            mask = np.zeros_like(frame)

            if len(faces) > 0: #não ta detectando legal com o óculos
                faces = sorted(faces, key=lambda x: x[2] * x[3], reverse=True)
                (x, y, w, h) = faces[0]
                mask[y:y + h, x:x + w] = (255, 255, 255)

            mask_bool = mask.astype(bool)
            bg_black = np.where(mask_bool, frame, 0)
'''