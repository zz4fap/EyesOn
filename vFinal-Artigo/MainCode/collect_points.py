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
py_global = []
x_pred = 0
y_pred = 0

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


pos_x = 0
pos_y = 0
class GazeEvaluationThread(threading.Thread):
    def __init__(self, device="cpu", snapshot='output/snapshots/L2CS-gaze360-_loader-180-4/_epoch_55.pkl',
                 cam_id=0, arch='ResNet50'):
        super().__init__()
        self.device = device
        self.snapshot_path = pathlib.Path(snapshot)
        self.cam_id = cam_id
        self.arch = arch
        self.running = True 
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
        global pos_x
        global pos_y
        width, height = 1920, 1080
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

        file_path = 'calib_10xPonto/calib12/calib_file12.csv'
        data = load_and_convert_csv(file_path)

        pitch_min = np.mean( (data[0][0], data[2][0]))
        pitch_max = np.mean( (data[1][0], data[3][0]))
        yaw_min = np.mean( (data[0][1], data[1][1]))
        yaw_max = np.mean( (data[2][1], data[3][1]))

        pitch_offset = -pitch_min
        yaw_offset = -yaw_min


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

                pitch_max_escalonado = pitch_max + pitch_offset
                pitch_escalonado = results.pitch + pitch_offset
                pos_x = (pitch_escalonado / pitch_max_escalonado) * width

                yaw_max_escalonado = yaw_max + yaw_offset
                yaw_escalonado = results.yaw + yaw_offset
                pos_y = (yaw_escalonado / yaw_max_escalonado) * height


                if pos_x < 0:
                    pos_x = 0

                if pos_x > 1920:
                    pos_x = 1920

                if pos_y > 1080:
                    pos_y = 1080

                if pos_y < 0:
                    pos_y = 0

                print(pos_x, pos_y)
                print()


                x_list.append(pos_x)
                y_list.append(pos_y)


                if ball_global:
                    x_list = x_list[ int( (1/3) * len(x_list) ): ].copy()
                    y_list = y_list[ int( (1/3) * len(y_list) ): ].copy()
                    #py_global.append( (np.mean(x_list[int( (2/4) * len(x_list) ):]),
                    #                           np.mean(y_list[int( (2/4) * len(y_list) ):]), contador) )
                    for i in range(len(x_list)):
                        py_global.append( (x_list[i], y_list[i], contador) )

                    contador+=1
                    x_list.clear()
                    y_list.clear()
                    ball_global = False

                if time.time() - new_start > 345: #X points
                    stop_time = True
                    print("SAVING")
                    with open('calib_10xPonto/calib12/teste_4points_allPreds13x21p-pt1-TESTESFTESTES.csv', 'w', newline='') as f:
                        # using csv.writer method from CSV package
                        write = csv.writer(f)
                        write.writerows(py_global)
                        print(write)
                        print('SAVED')
                    break

                #print(py_global)
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
    # Calcula os limites do retângulo (célula do grid)
    x_min = x_centro - cell_width//2
    x_max = x_centro + cell_width//2
    y_min = y_centro - cell_height//2
    y_max = y_centro + cell_height//2

    # Calcula a distância do ponto predito até a borda mais próxima da célula
    distancia = distancia_ponto_retangulo(x_pred, y_pred, x_min, y_min, x_max, y_max)

    return distancia

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
    distancias = []
    stop_time = False
    sec_cont = 0
    contador = 0
    ball_global = False
    dist_aux = []
    positions = []

    gaze_thread = GazeEvaluationThread(
        device=args.device,
        snapshot=args.snapshot,
        cam_id=args.cam_id,
        arch=args.arch
    )

    # Inicia a thread
    gaze_thread.start()
    time.sleep(7.8)

    pygame.init()
    # Configurações do grid
    ROWS, COLS = 13, 21
    WIDTH, HEIGHT = 1920, 1080
    CELL_WIDTH = WIDTH // COLS
    CELL_HEIGHT = HEIGHT // ROWS

    # Cores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (50, 50, 50)
    DARK_GRAY = (100, 100, 100)
    RED = (255, 0, 0)

    for row in range(ROWS):
        for col in range(COLS):
            positions.append(calcular_posicao_grid(row, col, CELL_WIDTH, CELL_HEIGHT))

    # Inicializa a tela
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Grid")
    clock = pygame.time.Clock()

    # Configuração do timer para mudar os quadrados
    CHANGE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(CHANGE_EVENT, 300)  # Muda a cada x segundos

    # Padrão de ativação dos quadrados
    squares_order = [(row, col) for row in range(ROWS) for col in range(COLS)]
    current_index = 0
    active_square = squares_order[current_index]
    collected_points = []

    running = True
    start_time = time.time()
    pos_aux = 0
    pos_memo = positions[0]
    repeater = 0


    while running:
        screen.fill(BLACK)

        # Processar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == CHANGE_EVENT:
                current_index = (current_index + 2) % len(squares_order)
                distancias.append( (np.mean(dist_aux.copy()), current_index))
                dist_aux.clear()
                try:
                    active_square = squares_order[current_index]
                    center_pos = calcular_posicao_grid(active_square[0], active_square[1], CELL_WIDTH, CELL_HEIGHT)
                    #print("CENTER POS ", center_pos)
                    collected_points.append(center_pos)
                    #print(collected_points)
                    ball_global = True
                    print("BALL GLOBAL TRUE")
                except:
                    print("EXCEPT")


                # Termina após percorrer todos os quadrados
                if len(collected_points) >= 138:  # Parada após X pontos
                    print("INDO PARA RUNNING FALSE")
                    running = False
                    time.sleep(0.5)  # Tempo extra para processar o último ponto

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
                pygame.draw.circle(screen, DARK_GRAY, center, 5)

                # Marcar pontos coletados com vermelho
                for point in collected_points:
                    pygame.draw.circle(screen, RED, point, 8)

        pygame.display.flip()
        clock.tick(30)
        repeater+=1 #repeater para debug


    time.sleep(8)
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

