import matplotlib.pyplot as plt
import csv

# Lista de pontos (x, y)
def convert_to_float(data):
    converted_data = []
    for row in data:
        converted_row = []
        for item in row:
            # Verifica se o item é uma string representando uma lista e remove os colchetes
            if item.startswith('[') and item.endswith(']'):
                item = item.strip('[]')
            # Converte o item para float e adiciona à linha
            converted_row.append(float(item))
        converted_data.append(converted_row)

    return converted_data

with open('linear_models/calibration4s_file10-noflash-eachPredict-30-01.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
# Convert data to float
data = [item for item in data if item]
data = convert_to_float(data)

print(data)
# Criar o gráfico
fig, ax = plt.subplots(figsize=(6, 6))

# Plotar os eixos
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Plotar cada ponto na lista
for x, y, z, w in data:
    ax.plot(x, y, 'ro')  # 'ro' para pontos vermelhos
    #ax.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(10, 10), ha='center')

# Configurar limites do gráfico
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Adicionar grade ao plano cartesiano
ax.grid(color='gray', linestyle='--', linewidth=0.5)

# Adicionar rótulos e título
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_title('Plano Cartesiano com Múltiplos Pontos')

# Mostrar o gráfico
plt.show()
