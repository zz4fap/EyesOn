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
import csv

def quantize_to_grid(x, y, cell_width, grid_cols, cell_height, grid_rows):
    col = min(x // cell_width, grid_cols - 1)
    row = min(y // cell_height, grid_rows - 1)

    # Calcula o centro da célula
    x_center = (col * cell_width) + (cell_width // 2)
    y_center = (row * cell_height) + (cell_height // 2)

    return (x_center, y_center)

def load_and_convert_csv(file_path):
    data = []
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            # Converte cada valor na linha para float
            try:
                converted_row = [float(value) for value in row]
                data.append(converted_row)
            except ValueError as e:
                print(f"Aviso: Não foi possível converter a linha {row}: {e}")
                continue
    return np.array(data)

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
    width, height = 1920, 1080
    tempo = 0
    aux_tempo = True
    ac_tracker = []

    interface_tela = threading.Thread(target=new_interface.Interface)

    cap = cv2.VideoCapture(cam)

    cap.set(cv2.CAP_PROP_FPS, 12) #NÃO COMENTAR NEM REMOVER ESSA LINHA
    #print(cap.get(cv2.CAP_PROP_FPS))

    file_path = 'avaliacoes/luiz/calib_file.csv'
    data = load_and_convert_csv(file_path)

    pitch_min = np.mean((data[0][0], data[2][0]))
    pitch_max = np.mean((data[1][0], data[3][0]))
    yaw_min = np.mean((data[0][1], data[1][1]))
    yaw_max = np.mean((data[2][1], data[3][1]))

    pitch_offset = -pitch_min
    yaw_offset = -yaw_min


    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")
    else:
        print("Webcam OK")
        interface_tela.start()
        print("INTERFACE OK")
    with torch.no_grad():
        while interface_tela.is_alive(): #enquanto o programa roda ...
            # Get frame
            success, frame = cap.read()
            start_fps = time.time()


            if aux_tempo:
                tempo = time.time()
                aux_tempo = False

            if not success:
                print("Failed to obtain frame")
                time.sleep(0.1)

            blinking = click.click_mouse(detector, predictor, frame)
            print(blinking)
            #CLICK NA PISCADA
            if blinking >= 4.4 and success:
                frame_count+=1
                print("PRINT FRAME COUNT ", frame_count)
                if frame_count == 12:
                    pag.click()
                    frame_count = 0
                    ac_tracker.append( ( time.time() - tempo, teclado.keyb_thread_on, calculadora.calc_thread_on, interface_google.interface_google_on) )
                    aux_tempo = True
            else:
                frame_count = 0
                b_act = False


            # Process frame
            results = gaze_pipeline.step(frame) #calc é feito

            pitch_max_escalonado = pitch_max + pitch_offset
            pitch_escalonado = results.pitch + pitch_offset
            pos_x = (pitch_escalonado / pitch_max_escalonado) * width

            yaw_max_escalonado = yaw_max + yaw_offset
            yaw_escalonado = results.yaw + yaw_offset
            pos_y = (yaw_escalonado / yaw_max_escalonado) * height

            try:
                if pos_y >= 800:
                    vis.move_cursor(results, teclado.keyb_thread_on, calculadora.calc_thread_on,interface_google.interface_google_on, pos_x, pos_y)
                else:
                    if blinking <= 4.4 and success:
                        vis.move_cursor(results, teclado.keyb_thread_on, calculadora.calc_thread_on, interface_google.interface_google_on, pos_x, pos_y)
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

with open('avaliacoes/luiz/ac_tracker.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(['Tempo desde último', 'Teclado ativo', 'Calculadora ativa', 'Google ativo'])
    write.writerows(ac_tracker)


avg_fps = np.array(avg_fps)
print("AVERAGE FPS: ", np.mean(avg_fps))








































