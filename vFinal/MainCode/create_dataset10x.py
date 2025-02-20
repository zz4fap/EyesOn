import csv

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

with open('calib_10xPonto/calibration4s_file11-pt1-20-02.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data = [item for item in data if item]
data = convert_to_float(data)
#print(data)

#for i in data:
#    print(i)

#all_data = [ [ [x], [y], [groundtruth]  ], ]
with open(f'calib_10xPonto/calibration4s_file11-pt1-20-02.csv', newline='') as f:
    reader = csv.reader(f)
    data1 = list(reader)
    data = [item for item in data1 if item]
    data = convert_to_float(data)
all_data = [[[], [], []] for _ in range(len(data))]

for h in range(len(data)):
    if h >= len(all_data):
        print(f"Erro: h={h} está fora dos limites de all_data ({len(all_data)})")
        break  # Evita acessar um índice inválido
    all_data[h][2].append( (data[h][2], data[h][3]))



#print(all_data)
for i in range(10):
    with open(f'calib_10xPonto/calibration4s_file11-pt{i+1}-20-02.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        data2 = [item for item in data if item]
        data2 = convert_to_float(data2)
        #print(data2[0])

        for j in range(len(data2)):
            all_data[j][0].append(data2[j][0])
            all_data[j][1].append(data2[j][1])



print(all_data)

with open('calib_10xPonto/calibration10x_file.csv', 'w') as f:
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerows(all_data)
