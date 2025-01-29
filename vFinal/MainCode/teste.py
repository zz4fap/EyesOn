import math

def calculate_dist(x_p, y_p, x_g, y_g):
    dist = math.sqrt((x_p - x_g)**2 + (y_p - y_g)**2)
    return dist

def calculate_rad(dist_c_p, d):
    rad = 2 * math.atan(dist_c_p / (2 * d))
    return rad

def calculate_deg(rad):
    deg = (rad / math.pi) * 180
    return deg

def calculate_aae_per_point(points, d):
    aae_per_point = []

    for (x_p, y_p), (x_g, y_g) in points:
        dist_c_p = calculate_dist(x_p, y_p, x_g, y_g)
        rad = calculate_rad(dist_c_p, d)
        deg = calculate_deg(rad)
        aae_per_point.append(deg)

    return aae_per_point

#pontos artigo
points = [
    ((960, 540), (989.5, 578.0)),
    ((960, 140), (908.9, 179.2)),
    ((1242, 257), (1166.1, 259.3)),
    ((1360, 540), (1333.7, 432.3)),
    ((1242, 822), (1252.3, 786.4)),
    ((960, 940), (987.0, 964.2)),
    ((677, 822), (705.7, 819.9)),
    ((560, 540), (594.7, 476.4)),
    ((677, 257), (652.4, 284.6)),
]

d = 50  # distancia da camera para o user

# aae por ponto
aae_per_point = calculate_aae_per_point(points, d)

for i, aae in enumerate(aae_per_point):
    print(f"AAE para o par de pontos {i+1}: {aae:.2f}")


rad = 2 * math.atan(calculate_dist(960, 540, 989.5, 578) / 100)
print( (rad/math.pi) * 180)