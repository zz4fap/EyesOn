import numpy as np


def calculate_distance(C, P):
    """Calcula a distância euclidiana entre C e P"""
    return np.sqrt((P[0] - C[0]) ** 2 + (P[1] - C[1]) ** 2)


def calculate_v_red(C, P, D):
    """Calcula V_red(C, P)"""
    dist = calculate_distance(C, P)
    return 2 * np.arctan(dist / (2 * D))


def calculate_v_deg(C, P, D):
    """Converte V_red(C, P) para graus"""
    v_red = calculate_v_red(C, P, D)
    return (v_red / (2 * np.pi)) * 360


def calculate_accuracy(C, P_list, D):
    """Calcula a acurácia média"""
    v_deg_values = [calculate_v_deg(C, P, D) for P in P_list]
    return np.mean(v_deg_values)


# Exemplo de uso:
C = (960, 140)  # Coordenadas do ponto C
P_list = [(908.9, 179.2)]  # Lista de pontos P




D = 2200  # Valor arbitrário para D

accuracy = calculate_accuracy(C, P_list, D)
print(f"Acurácia (AAE): {accuracy:.4f}")

#primeiro ponto = 1318
