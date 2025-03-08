import math
import numpy as np
from l2cs import Pipeline
import csv
import pygame

import pathlib
import argparse
import cv2
import torch
import time
from torch.backends import cudnn
import threading
import joblib
from sklearn.preprocessing import PolynomialFeatures
from l2cs import Pipeline, render



poly = PolynomialFeatures(degree=2)

def calcular_posicoes_circulares(w=1920, h=1080, space_radius=400):
    # Ponto central
    centro = (w // 2, h // 2)
    # Calculando os 8 pontos no círculo
    pontos = []
    for i in range(8):
        angulo = 2 * math.pi * i / 8  # Ângulo para cada ponto
        x = int(w // 2 + space_radius * math.cos(angulo))
        y = int(h // 2 + space_radius * math.sin(angulo))
        pontos.append((x, y))

    # Retornando os pontos com o ponto central no final
    return pontos + [centro]


ball_global = False
class AccuracyPoints(threading.Thread):
    def __init__(self, screen_width=1920, screen_height=1080, r=50):
        super().__init__()  # Inicializa a Thread
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.r = r
        self.positions = self.calcular_posicoes_circulares()
        self.running = True  # Controle de execução do loop

    def calcular_posicoes_circulares(self, space_radius=400):
        # Ponto central
        centro = (self.screen_width // 2, self.screen_height // 2)

        # Calculando os 8 pontos no círculo
        pontos = []
        for i in range(8):
            angulo = 2 * math.pi * i / 8  # Ângulo para cada ponto
            x = int(self.screen_width // 2 + space_radius * math.cos(angulo))
            y = int(self.screen_height // 2 + space_radius * math.sin(angulo))
            pontos.append((x, y))

        # Retornando os pontos com o ponto central no final
        return pontos + [centro]

    def run(self):
        """Executa o loop principal."""
        # Inicializa o pygame
        global ball_global
        pygame.init()
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("9 Pontos com no circulo")
        time.sleep(10)
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
            pygame.draw.circle(screen, (255, 255, 255), pos, self.r)  # Branco

            # Atualiza a tela
            pygame.display.flip()

            # Espera 2 segundos
            time.sleep(4)
            ball_global = True

        pygame.quit()

    def stop(self):
        """Para a execução do loop."""
        self.running = False


stop_time = False
sec_cont = 0
py_global = []
contador = 0
posicoes = calcular_posicoes_circulares()
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
        y_list = []
        p_list = []
        global contador
        global posicoes
        global ball_global
        p_pred = []
        yaw_pred = []
        k = False
        ttt = []
        start = time.time()
        cudnn.enabled = True

        model_x = joblib.load('model_x_linear_morePitch-27.02.pkl')
        model_y = joblib.load('model_y_linear_morePitch-27.02.pkl')
        print("Models loaded successfully!")

        self.initialize_pipeline()

        with torch.no_grad():
            while self.running:
                if not k:
                    new_start = time.time()
                    sec_cont = new_start
                k = True
                # Obtém frame da câmera
                success, frame = self.cap.read()
                if not success:
                    print("Failed to obtain frame")
                    time.sleep(0.1)
                    continue

                # Processa o frame
                results = self.gaze_pipeline.step(frame)
                print(f"Pitch: {results.pitch}")
                print(f"Yaw: {results.yaw}")


#                p_list.append(results.pitch)
#                y_list.append(results.yaw)
                ttt = np.array([[results.pitch, results.yaw]])

                # ttt duas dimensões
                if ttt.ndim > 2:
                    ttt = ttt.reshape(-1, 2)

                poly.fit(ttt)

                X_test_poly = poly.transform(ttt)

                x_pred = model_x.predict(X_test_poly)
                y_pred = model_y.predict(X_test_poly)

                print(x_pred)
                print(y_pred)

                p_pred.append(x_pred)
                yaw_pred.append(y_pred)

                print(p_pred)
                print(yaw_pred)
                print()

                if ball_global:
                    aux = 2 * len(p_pred) // 4
                    py_global.append( (p_pred[aux:].copy(), yaw_pred[aux:].copy() ,posicoes[contador][0], posicoes[contador][1]) )
                    contador+=1
                    p_pred.clear()
                    yaw_pred.clear()
                    ball_global = False
                #print(time.time() - new_start)
                print()

                if time.time() - new_start > 37.5: #9points
                    stop_time = True
                    with open('accuracy4s_test15-27.02.csv', 'w') as f:
                        # using csv.writer method from CSV package
                        write = csv.writer(f)
                        write.writerows(py_global)
                    break

                print(py_global)
                print()

                # Renderização (desativada, mas pode ser adicionada)
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
            default="cpu", type=str)
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

    # Cria uma instância da thread
    accuracy = AccuracyPoints(screen_width=1920, screen_height=1080, r=50)

    gaze_thread = GazeEvaluationThread(
        device=args.device,
        snapshot=args.snapshot,
        cam_id=args.cam_id,
        arch=args.arch
    )

    # Inicia a thread
    gaze_thread.start()

    # Simula o loop principal da aplicação
    try:
        accuracy.start()
        while gaze_thread.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        print("Encerrando...")
        gaze_thread.stop()
        gaze_thread.join()
        accuracy.stop()
        accuracy.join()

    if stop_time:
        gaze_thread.stop()
        gaze_thread.join()
        accuracy.stop()
        accuracy.join()

    print(stop_time)
    print(py_global)
    print(len(py_global))

#41s