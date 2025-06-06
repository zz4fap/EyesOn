#16 pontos
#calcula pitch, yaw
#2s cada ponto (media desses 2s)
#combine reference with predicted point ( (pitch, yaw) , Ref))
import numpy as np
import csv
import pygame

import pathlib
import argparse
import cv2
import torch
import time
from torch.backends import cudnn
import threading
from l2cs import Pipeline, render
import cv2


def calcular_posicoes(w=1920, h=1080, r=50):
    return [
        (r, r),  # Superior esquerdo
        (w - r, r),  # Superior direito
        (r, h - r),  # Inferior esquerdo
        (w - r, h - r),  # Inferior direito
    ]


ball_global = False
class CalibrationPoints(threading.Thread):
    def __init__(self, screen_width=1920, screen_height=1080, r=50):
        super().__init__()  
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.r = r
        self.positions = self.calcular_posicoes()
        self.running = True  # Controle de execução do loop

    def calcular_posicoes(self):
        """Calcula as posições baseadas na matriz fornecida."""
        r = self.r
        w, h = self.screen_width, self.screen_height
        return [
            (r, r),  # Superior esquerdo
            (w - r, r),  # Superior direito
            (r, h - r),  # Inferior esquerdo
            (w - r, h - r),  # Inferior direito
        ]

    def run(self):
        """Executa o loop principal."""
        # Inicializa o pygame
        global ball_global
        global iniciar
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("4 Pontos com Base na Matriz")
        while not iniciar:
            time.sleep(0.5)
            continue
        for pos in self.positions:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break

            if not self.running:
                break

            # Limpa a tela
            screen.fill((0, 0, 0))  # Preto

            # Desenha o ponto atual
            pygame.draw.circle(screen, (255, 255, 255), pos, self.r)

            # Atualiza a tela
            pygame.display.flip()

            # Espera 5 sec
            time.sleep(5)
            ball_global = True

        pygame.quit()

    def stop(self):
        """Para a execução do loop."""
        self.running = False


stop_time = False
sec_cont = 0
py_global = []
contador = 0
posicoes = calcular_posicoes()
iniciar = False
class GazeEvaluationThread(threading.Thread):
    def __init__(self, device="cpu", snapshot='output/snapshots/L2CS-gaze360-_loader-180-4/_epoch_55.pkl',
                 cam_id=0, arch='ResNet50'):
        super().__init__()
        self.device = device
        self.snapshot_path = pathlib.Path(snapshot)
        self.cam_id = cam_id
        self.arch = arch
        self.running = True  # Controle do loop
        self.gaze_pipeline = None
        self.cap = None

    def initialize_pipeline(self):
        """Inicializa o pipeline de gaze."""
        self.gaze_pipeline = Pipeline(
            weights=pathlib.Path.cwd() / 'models' / 'L2CSNet_gaze360.pkl',
            arch=self.arch,
            device=torch.device(self.device)
        )
        self.cap = cv2.VideoCapture(self.cam_id)
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")
        else:
            print("Webcam OK")

    def run(self):
        """Executa o loop principal da thread."""
        global stop_time
        global py_global
        global iniciar
        y_list = []
        p_list = []
        global contador
        global posicoes
        global ball_global
        k = False
        start = time.time()
        cudnn.enabled = True
        self.initialize_pipeline()

        with torch.no_grad():
            while self.running:
                if not k:
                    new_start = time.time()
                k = True
                
                success, frame = self.cap.read()
                iniciar = True
                if not success:
                    print("Failed to obtain frame")
                    time.sleep(0.1)
                    continue

                
                results = self.gaze_pipeline.step(frame)
                print(f"Pitch: {results.pitch}")
                print(f"Yaw: {results.yaw}")


                p_list.append(results.pitch)
                y_list.append(results.yaw)

                if ball_global:
                    py_global.append( (np.mean(p_list[ ( 2 * len(p_list) ) // 5: ( 4 * len(p_list) ) // 5]), np.mean(y_list[ ( 2 * len(y_list ) ) // 5: ( 4 * len(p_list) ) // 5]), posicoes[contador][0], posicoes[contador][1]) )
                    contador+=1
                    p_list.clear()
                    y_list.clear()
                    ball_global = False
                #print(time.time() - new_start)
                print()

                if time.time() - new_start > 21: #4points 5s each = 20 + 1
                    stop_time = True
                    with open('avaliacoes/luiz/calib_file.csv', 'w', newline='') as f:
                        # using csv.writer method from CSV package
                        write = csv.writer(f)
                        write.writerows(py_global)
                    break

                # Renderização - opcional para visualização
                frame = render(frame, results)
                cv2.imshow("Gaze Output", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.running = False

        self.cap.release()
        # cv2.destroyAllWindows()
        print("Time: ", new_start - start)

    def stop(self):
        """Encerra o loop."""
        self.running = False

    @staticmethod
    def parse_args():
        """Parseia os argumentos de entrada."""
        parser = argparse.ArgumentParser(
            description='Gaze evaluation using model pretrained with L2CS-Net on Gaze360.')
        parser.add_argument(
            '--device', dest='device', help='Device to run model: cpu or gpu:0',
            default="cuda", type=str)
        parser.add_argument(
            '--snapshot', dest='snapshot', help='Path of model snapshot.',
            default='output/snapshots/L2CS-gaze360-_loader-180-4/_epoch_55.pkl', type=str)
        parser.add_argument(
            '--cam', dest='cam_id', help='Camera device id to use [0]',
            default=0, type=int)
        parser.add_argument(
            '--arch', dest='arch',
            help='Network architecture, can be: ResNet18, ResNet34, ResNet50, ResNet101, ResNet152',
            default='ResNet50', type=str)

        return parser.parse_args()


if __name__ == "__main__":
    args = GazeEvaluationThread.parse_args()


    calibration = CalibrationPoints(screen_width=1920, screen_height=1080, r=50)

    gaze_thread = GazeEvaluationThread(
        device=args.device,
        snapshot=args.snapshot,
        cam_id=args.cam_id,
        arch=args.arch
    )

    gaze_thread.start()
 
    try:
        calibration.start()
        while gaze_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando...")
        gaze_thread.stop()
        gaze_thread.join()
        calibration.stop()
        calibration.join()

    if stop_time:
        gaze_thread.stop()
        gaze_thread.join()
        calibration.stop()
        calibration.join()

    print(stop_time)
    print(py_global)
    print(len(py_global))