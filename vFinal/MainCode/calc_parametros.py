import csv
import numpy as np
from numpy import array

def convert_to_float(data):
    new_data = []
    for item in data:
        new_item = []
        for subitem in item:
            if 'array' in subitem:
                # Avalia o array do NumPy como uma expressão
                new_subitem = eval(subitem)
                # Converte para lista de floats
                new_subitem = [float(value) for value in new_subitem]
            else:
                # Converte a string para float diretamente
                new_subitem = float(subitem)
            new_item.append(new_subitem)
        new_data.append(new_item)
    return new_data


def euclidean_distance(x, y, xr, yr):
    return np.sqrt((np.array(x) - xr)**2 + (np.array(y) - yr)**2)

with open('linear_models/accuracy4s_test10-noFlash-eachPredict-30.01.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data = [item for item in data if item]
data = convert_to_float(data)

x_medio = []
y_medio = []
p_medio = []

for d in data:
    p_medio.append( (np.mean(d[0]), np.mean(d[1]), d[2], d[3]))
#print(p_medio)



# Calcular as distâncias para todos os pontos
dist = [euclidean_distance(item[0], item[1], item[2], item[3]) for item in data]
#print(distances)


'''data_xy = []
data_ans = []
for d in data:
    data_xy.append( (d[0], d[1]) )
    data_ans.append( (d[2], d[3]) )'''

#print(dist)
D = 600
rad = []
deg = []
aae = []

for d in dist:
    r = 2 * np.arctan(np.array(d) / (2 * D))
    rad.append(r)

#rad = 2 * np.arctan(np.array(dist) / (2 * D))
#print(len(rad), len(rad[0]))

for r in rad:
    d = (r / np.pi) * 180
    deg.append(d)
print(deg)
#print(deg)

cont = 0
for d in deg:
    a = np.sum(d) / len(deg[cont])
    aae.append(a)
    cont+=1

#print(aae)
#print(len(aae))
#print("Distância Euclidiana:", dist)
#print("Radianos:", rad)
#print("Graus:", deg)
print("AAE: ", aae)

#print(p_medio )

p_dist = [euclidean_distance(item[0], item[1], item[2], item[3]) for item in p_medio]
cc = 0
for p in p_medio:
    print(f"Q{cc} -- Ponto Médio:  ({p[0]:.2f}, {p[1]:.2f}) / Ground Truth: ({p[2]},{p[3]}) / AAE: {aae[cc]:.2f}")
    cc+=1




'''
[48.106652346634974,
 64.40380423546424,
 75.93484048840831,
 110.86469230553068,
 37.06008634636461,
 36.25796464226863,
 28.776726707532298,
 72.45032781154275,
 36.971881207209385]'''