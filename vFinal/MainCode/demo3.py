import argparse
import pathlib
import numpy as np
import cv2
import time
import threading

import torch
import torch.backends.cudnn as cudnn

import pyautogui as pag

from l2cs import vis
from l2cs import Pipeline, render
import calculadora
import teclado
import interface_google
import mouse_clicks.click as click
import dlib
import new_interface


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




if __name__ == '__main__':
    args = parse_args()
    avg_fps = []
    cudnn.enabled = True
    arch=args.arch
    cam = args.cam_id
    snapshot_path = args.snapshot
    #print(CWD)
    gaze_pipeline = Pipeline(
        weights=CWD / 'models' / 'L2CSNet_gaze360.pkl',
        arch='ResNet50',
        device=torch.device('cuda') #cpu or cuda
    )

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('./mouse_clicks/shape_predictor_68_face_landmarks.dat')
    frame_count = 0

    interface_tela = threading.Thread(target=new_interface.Interface)

    cap = cv2.VideoCapture(cam)

    cap.set(cv2.CAP_PROP_FPS, 12) #NÃO COMENTAR NEM REMOVER ESSA LINHA
    #print(cap.get(cv2.CAP_PROP_FPS))

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    else:
        print("Webcam OK")
        interface_tela.start()
        print("INTERFACE OK")
    with torch.no_grad():
        while True: #enquanto o programa roda ...
            # Get frame
            success, frame = cap.read()
            start_fps = time.time()

            if not success:
                print("Failed to obtain frame")
                time.sleep(0.1)

            blinking = click.click_mouse(detector, predictor, frame)
            print(blinking)
            #CLICK NA PISCADA
            if blinking >= 4 and success:
                frame_count+=1
                print("PRINT FRAME COUNT ", frame_count)
                if frame_count == 12:
                    pag.click()
                    frame_count = 0
            else:
                frame_count = 0


            # Process frame
            results = gaze_pipeline.step(frame) #calc é feito
            try:
                vis.move_cursor(results, teclado.keyb_thread_on, calculadora.calc_thread_on, interface_google.interface_google_on)
            except:
                print("0 FACES DETECTADAS")

            # Visualize output
            frame = render(frame, results)

            myFPS = 1.0 / (time.time() - start_fps)
            avg_fps.append(myFPS)

            cv2.putText(frame, 'FPS: {:.1f}'.format(myFPS), (10, 20),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1, cv2.LINE_AA)

            cv2.imshow("frame1",frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            success,frame = cap.read()
        cap.release()


avg_fps = np.array(avg_fps)
print("AVERAGE FPS: ", np.mean(avg_fps))


#FAZER O APAGAR DO TECLADO FUNCIONAR NO GOOGLE
#COLOCAR DLIB NA GPU
#ALTERAR TECLADO
#TENTAR COLOCAR A DETECÇÃO DE PONTOS NA FACE NA ÁREA APENAS DA FACE
#COLOCAR ALGO NO TECLADO/CALCULADORA QUE INDIQUE O BOTÃO SENDO APERTADO
#ADICIONAR A INTERFACE_GOOGLE TAMBÉM NO YOUTUBE

#fazer video








































