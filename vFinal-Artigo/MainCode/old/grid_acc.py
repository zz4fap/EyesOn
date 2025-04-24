import pygame
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
from l2cs import Pipeline, render
import cv2
import joblib
from sklearn.preprocessing import PolynomialFeatures
import pyautogui as pag

ball_global = False
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

        model_x = joblib.load('modelX_RF-newACC-40Sample.pkl')
        model_y = joblib.load('modelY_RF-newACC-40Sample.pkl')
        print("Models loaded successfully!")

        self.initialize_pipeline()

        with torch.no_grad():
            while self.running:
                if not k:
                    new_start = time.time()
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
                pag.moveTo(x_pred, y_pred)

                p_pred.append(x_pred)
                yaw_pred.append(y_pred)

                print(p_pred)
                print(yaw_pred)
                print()

                if ball_global:
                    aux = 2 * len(p_pred) // 4
                    py_global.append( (p_pred[aux:].copy(), yaw_pred[aux:].copy()) )
                    contador+=1
                    p_pred.clear()
                    yaw_pred.clear()
                    ball_global = False
                #print(time.time() - new_start)
                print()

                if time.time() - new_start > 33: #9points
                    stop_time = True
                    with open('accuracy_files/teste2-40sample.csv', 'w') as f:
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


# Função para calcular a posição do grid
def calcular_posicao_grid(row, col, cell_width, cell_height):
    x = col * cell_width + cell_width // 2
    y = row * cell_height + cell_height // 2
    return x, y

def distancia_ponto_retangulo(xp, yp, xmin, ymin, xmax, ymax):
    # Se o ponto está dentro do retângulo, a distância é 0
    if xmin <= xp <= xmax and ymin <= yp <= ymax:
        return 0

    # Calcula a menor distância para os lados do retângulo
    dx = max(xmin - xp, 0, xp - xmax)
    dy = max(ymin - yp, 0, yp - ymax)

    return math.sqrt(dx**2 + dy**2)

if __name__ == "__main__":
    newww = time.time()
    args = GazeEvaluationThread.parse_args()
    poly = PolynomialFeatures(degree=2)
    stop_time = False
    sec_cont = 0
    py_global = []
    contador = 0
    ball_global = False

    gaze_thread = GazeEvaluationThread(
        device=args.device,
        snapshot=args.snapshot,
        cam_id=args.cam_id,
        arch=args.arch
    )

    # Inicia a thread
    gaze_thread.start()

    # Configurações do grid
    ROWS, COLS = 4, 4
    WIDTH, HEIGHT = 1920, 1080
    CELL_WIDTH = WIDTH // COLS
    CELL_HEIGHT = HEIGHT // ROWS

    # Cores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (50, 50, 50)
    DARK_GRAY = (100, 100, 100)

    time.sleep(6)
    # Inicializa o pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Grid Acendendo Quadrados")
    clock = pygame.time.Clock()

    # Timer para acender os quadrados
    CHANGE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(CHANGE_EVENT, 2000)

    # Lista de índices seguindo o padrão desejado
    pattern = []
    for row in range(0, ROWS, 2):  # Pulando 1 linha entre cada
        for col in range(0, COLS, 4):  # Pulando 2 quadrados entre cada
            pattern.append((row, col))


    current_index = 0  # Índice do quadrado que será iluminado
    aux = 0
    pts = set()
    running = True

    print("TEMPO> ", newww - time.time())
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if current_index == 15:
                running = False
            elif event.type == CHANGE_EVENT:
                current_index = (current_index + 1) % len(pattern)
                ball_global = True
                #print(current_index)

        # Desenhar o grid
        for row in range(ROWS):
            for col in range(COLS):
                x, y = calcular_posicao_grid(row, col, CELL_WIDTH, CELL_HEIGHT)
                rect = pygame.Rect(col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
                # Definir cor do quadrado
    #            color = WHITE if (row, col) == pattern[current_index] else GRAY

                if (row, col) == pattern[current_index]:
                    color = WHITE
                    pts.add((x, y))
                else:
                    color = GRAY
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)  # Borda principal mais grossa

                # Desenhar círculo no centro de cada célula
                pygame.draw.circle(screen, DARK_GRAY, (x, y), 5)
        aux = 1

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
    gaze_thread.stop()
    gaze_thread.join()
    pts = list(pts)
    print(pts)
    print(len(pts))
