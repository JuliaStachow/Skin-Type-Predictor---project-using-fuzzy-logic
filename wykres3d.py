import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Tworzenie zmiennych wejściowych i wyjściowej
x1 = np.linspace(0, 10, 100)
x2 = np.linspace(0, 10, 100)
y = np.linspace(0, 100, 100)

# Tworzenie funkcji przynależności dla każdej zmiennej
mf_x1 = fuzz.trimf(x1, [2, 5, 8])
mf_x2 = fuzz.trimf(x2, [1, 6, 9])
mf_y = fuzz.trimf(y, [20, 50, 80])

# Tworzenie siatki punktów wejściowych
x1, x2 = np.meshgrid(x1, x2)
y_mesh = np.zeros_like(x1)

# Ocena funkcji przynależności dla każdego punktu siatki
for i in range(len(x1)):
    for j in range(len(x2)):  # Fix here
        rule_activation = min(mf_x1[i], mf_x2[j])  # Fix here
        y_mesh[i, j] = rule_activation * mf_y[int((x1[i, j] + x2[i, j]) / 2)]

# Defuzyfikacja metodą MOM
y_mesh_flat = y_mesh.flatten()
y_defuzz = fuzz.defuzz(y, y_mesh_flat, 'mom')

# Reshape x1 and x2 to match the shape of y_mesh
x1_reshaped = x1.flatten()
x2_reshaped = x2.flatten()

# Rysowanie wykresu 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x1, x2, y_mesh, cmap='viridis', alpha=0.7)
ax.scatter(x1_reshaped, x2_reshaped, y_defuzz, color='red', marker='o', s=100, label='Wartość defuzyfikowana')
ax.set_xlabel('Zmienna Wejściowa 1')
ax.set_ylabel('Zmienna Wejściowa 2')
ax.set_zlabel('Zmienna Wyjściowa')
plt.legend()
plt.show()