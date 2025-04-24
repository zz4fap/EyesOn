import pygame
import math

# Configurações do grid
ROWS, COLS = 8, 14
WIDTH, HEIGHT = 1920, 1080
CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
DARK_GRAY = (100, 100, 100)


# Função para calcular a posição do grid
def calcular_posicao_grid(row, col, cell_width, cell_height):
    x = col * cell_width + cell_width // 2
    y = row * cell_height + cell_height // 2
    return x, y


# Inicializa o pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid 14x8 - Acendendo Quadrados")
clock = pygame.time.Clock()

# Timer para acender os quadrados
CHANGE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_EVENT, 2000)

current_index = 0  # Índice do quadrado que será iluminado

t = 0

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_EVENT:
            current_index = (current_index + 1) % (ROWS * COLS)
    # Desenhar o grid
    for row in range(ROWS):
        for col in range(COLS):
            x, y = calcular_posicao_grid(row, col, CELL_WIDTH, CELL_HEIGHT)
            if t < 14*8:
                print(x, y)
                t += 1
            rect = pygame.Rect(col * CELL_WIDTH, row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
            cell_number = row * COLS + col
            color = WHITE if cell_number == current_index else GRAY
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)  # Borda principal mais grossa

            # Desenhar círculo no centro de cada célula
            pygame.draw.circle(screen, DARK_GRAY, (x, y), 5)  # Pequeno círculo central

    pygame.display.flip()
    clock.tick(30)

pygame.quit()