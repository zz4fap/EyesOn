def calcular_posicao_grid(row, col, cell_width, cell_height):
    x = col * cell_width + cell_width // 2
    y = row * cell_height + cell_height // 2
    return x, y


ROWS, COLS = 6, 10

WIDTH, HEIGHT = 1920, 1080
CELL_WIDTH = WIDTH // COLS
CELL_HEIGHT = HEIGHT // ROWS

positions = []

for row in range(ROWS):
    for col in range(COLS):
        positions.append(calcular_posicao_grid(row, col, CELL_WIDTH, CELL_HEIGHT))

print(positions)
print(len(positions))
x_atual = 1020
y_atual = 730

print(x_atual // 10)
print((y_atual//6) * 6)