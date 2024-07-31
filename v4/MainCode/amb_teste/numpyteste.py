import numpy as np

# Initialize arrays as lists to allow in-place modification
dx = np.random.rand(15).tolist()
dy = np.random.rand(15).tolist()

def sla(dx, dy):
    dx.pop(0)  # Remove the first element
    dy.pop(0)
    dx.append(np.array(np.random.rand()))  # Append a new random value
    dy.append(np.array(np.random.rand()))

for i in range(20):
    sla(dx, dy)
    print("dx:", np.array(dx))
    print("dy:", np.array(dy))
    print()
