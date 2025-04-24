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

def get_label_to_coords():
    """Retorna dicionário completo de labels para coordenadas"""
    return {
        1: (50.0, 50.0),
        5: (656.0, 50.0),
        9: (1263.0, 50.0),
        13: (1870.0, 50.0),
        2: (50.0, 376.0),
        6: (656.0, 376.0),
        10: (1263.0, 376.0),
        14: (1870.0, 376.0),
        3: (50.0, 703.0),
        7: (656.0, 703.0),
        11: (1263.0, 703.0),
        15: (1870.0, 703.0),
        4: (50.0, 1030.0),
        8: (656.0, 1030.0),
        12: (1263.0, 1030.0),
        16: (1870.0, 1030.0)
    }

ball_global = False
py_global = []
x_pred = 0
y_pred = 0
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
        global x_pred
        global y_pred
        #dici = get_label_to_coords()
        y_list = []
        p_list = []
        global contador
        global posicoes
        global ball_global
        x_list = []
        y_list = []
        k = False
        ttt = []
        start = time.time()
        cudnn.enabled = True

        model_x = joblib.load('rf_regressorX.pkl')
        model_y = joblib.load('rf_regressorY.pkl')
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
                #print(f"Pitch: {results.pitch}")
                #print(f"Yaw: {results.yaw}")

                # Criar array 2D com formato (1, 2)
                ttt = np.array([[results.pitch, results.yaw]])
                ttt = np.array(ttt)  # Agora tem shape (1, 2, 1)
                ttt = ttt.reshape(1, -1)  # Transforma para (1, 2)
                #print("ttt = ", ttt)

                # Fazer previsões
                x_pred = model_x.predict(ttt)
                y_pred = model_y.predict(ttt)

                x_list.append(x_pred)
                y_list.append(y_pred)

                #print(f"Coordenada X prevista: {x_pred[0]}")
                #print(f"Coordenada Y prevista: {y_pred[0]}")

                pag.moveTo(x_pred[0], y_pred[0])
                print("COORDENADAS: ", x_pred[0], y_pred[0])
                print()

                if ball_global:
                    py_global.append( (np.mean(x_list.copy()), np.mean(y_list.copy())) )
                    contador+=1
                    x_list.clear()
                    y_list.clear()
                    ball_global = False
                #print(time.time() - new_start)
                print()
                print("diguidim")
                if time.time() - new_start > 15: #15points
                    stop_time = True
                    print("SALVANDO")
                    with open('accuracy_files/aaaaa.csv', 'w', newline='') as f:
                        # using csv.writer method from CSV package
                        write = csv.writer(f)
                        write.writerows(py_global)
                        print(write)
                        print('TA SALVO')
                    break

                print(py_global)
                print()

                # Renderização
                frame = render(frame, results)
                cv2.imshow("Gaze Output", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    self.running = False

        self.cap.release()
        # cv2.destroyAllWindows()
        #print("Time: ", new_start - start)

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


import math


def calcular_distancia_centro_para_borda(x_centro, y_centro, cell_width, cell_height, x_pred, y_pred):
    # Calcula o centro da célula do grid

    # Calcula os limites do retângulo (célula do grid)
    x_min = x_centro - cell_width//2
    x_max = x_centro + cell_width//2
    y_min = y_centro - cell_height//2
    y_max = y_centro + cell_height//2

    print("X, Y" , x_centro, y_centro)
    print("XMIN E XMAX = ", x_min, x_max)

    # Calcula a distância do ponto predito até a borda mais próxima da célula
    distancia = distancia_ponto_retangulo(x_pred, y_pred, x_min, y_min, x_max, y_max)

    return distancia


# Suas funções originais (mantidas como estão)
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

    return math.sqrt(dx ** 2 + dy ** 2)

if __name__ == "__main__":
    newww = time.time()
    args = GazeEvaluationThread.parse_args()
    #poly = PolynomialFeatures(degree=2)
    distancias = []
    stop_time = False
    sec_cont = 0
    contador = 0
    ball_global = False
    dist_aux = []

    gaze_thread = GazeEvaluationThread(
        device=args.device,
        snapshot=args.snapshot,
        cam_id=args.cam_id,
        arch=args.arch
    )

    # Inicia a thread
    gaze_thread.start()
    time.sleep(7.6)

    pygame.init()
    # Configurações do grid
    ROWS, COLS = 6, 5
    WIDTH, HEIGHT = 1920, 1080
    CELL_WIDTH = WIDTH // COLS
    CELL_HEIGHT = HEIGHT // ROWS

    # Cores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (50, 50, 50)
    DARK_GRAY = (100, 100, 100)
    RED = (255, 0, 0)

    # Inicializa a tela
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Grid")
    clock = pygame.time.Clock()

    # Configuração do timer para mudar os quadrados
    CHANGE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(CHANGE_EVENT, 1000)  # Muda a cada 2 segundos

    # Padrão de ativação dos quadrados (todos em sequência)
    squares_order = [(row, col) for row in range(ROWS) for col in range(COLS)]
    current_index = 0
    active_square = squares_order[current_index]
    collected_points = []

    running = True
    start_time = time.time()

    while running:
        screen.fill(BLACK)

        # Processar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == CHANGE_EVENT:
                current_index = (current_index + 1) % len(squares_order) + 1
                try:
                    active_square = squares_order[current_index]
                    center_pos = calcular_posicao_grid(active_square[0], active_square[1], CELL_WIDTH, CELL_HEIGHT)
                    #print("CENTER POS ", center_pos)
                    collected_points.append(center_pos)
                except:
                    print("EXCEPT")


                # Termina após percorrer todos os quadrados
                if current_index >= len(squares_order) - 1:
                    running = False

        # Desenhar o grid
        for row in range(ROWS):
            for col in range(COLS):
                rect = pygame.Rect(col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)

                # Quadrado ativo é branco, outros são cinza
                color = WHITE if (row, col) == active_square else GRAY
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)  # Borda

                # Ponto central
                center = calcular_posicao_grid(row, col, CELL_WIDTH, CELL_HEIGHT)
                dist_pred = calcular_distancia_centro_para_borda(center[0], center[1], CELL_WIDTH, CELL_HEIGHT,x_pred, y_pred)
                dist_aux.append(dist_pred)
                print("DIST PRED = ", dist_pred)
                ball_global = True
                pygame.draw.circle(screen, DARK_GRAY, center, 5)

                # Marcar pontos coletados com vermelho
                for point in collected_points:
                    pygame.draw.circle(screen, RED, point, 8)

        distancias.append(np.mean(dist_aux.copy()))
        dist_aux.clear()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

    # Exibir resultados
    print("Pontos coletados em ordem:")
    for i, point in enumerate(collected_points, 1):
        print(f"{i}: {point}")

    print(f"\nTempo total de execução: {time.time() - start_time:.2f} segundos")
    gaze_thread.stop()
    gaze_thread.join()

    print(py_global)
    print(distancias)

