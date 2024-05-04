import numpy as np
from math import sqrt, log, cos, pi
import matplotlib.pyplot as plt

def cuadrados_medios(seed, n):
    random_numbers = []
    for _ in range(n):
        seed = (seed ** 2) // 100 % 10000  # Corrección aquí
        random_numbers.append(seed / 10000)
    return random_numbers

def ingresar_semilla():
    semilla = input("Ingrese una semilla de 7 dígitos: ")
    while not semilla.isdigit() or len(semilla) != 7:
        semilla = input("Por favor, ingrese una semilla válida de 7 dígitos: ")
    return int(semilla)

def calcular_media_y_mediana():
    entrada = "5 0 4 8 5 4"
    numeros = [float(x) for x in entrada.split()]
    media = np.mean(numeros)
    mediana = np.median(numeros)
    return media, mediana

media, mediana = calcular_media_y_mediana()

semilla1 = ingresar_semilla()
semilla2 = ingresar_semilla()

# Generar 1000 números pseudoaleatorios para cada semilla
numeros_pseudoaleatorios1 = cuadrados_medios(semilla1, 1000)
numeros_pseudoaleatorios2 = cuadrados_medios(semilla2, 1000)

# Imprimir los 1000 números generados por la primera semilla
print("Números generados por la primera semilla:")
print(numeros_pseudoaleatorios1)

# Imprimir los 1000 números generados por la segunda semilla
print("\nNúmeros generados por la segunda semilla:")
print(numeros_pseudoaleatorios2)

# Calcular los resultados para la distribución normal
resultados = []
for i in range(len(numeros_pseudoaleatorios1)):
    if numeros_pseudoaleatorios1[i] > 0:
        resultado = sqrt(-2 * log(numeros_pseudoaleatorios1[i])) * cos(2 * pi * numeros_pseudoaleatorios2[i])
        normal = resultado * media + mediana  # Sumar la mediana
        resultados.append(normal)

# Definir el rango de valores en el eje x
min_value = min(resultados)
max_value = max(resultados)
x = np.linspace(min_value, max_value, 1000)

# Calcular los valores de la distribución normal en este rango
y = 1 / (mediana * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - media) / mediana) ** 2)

# Graficar la distribución normal
plt.plot(x, y, color='r', label='Distribución normal')

# Imprimir la media y la mediana
print('\nMedia:', media)
print('Mediana:', mediana)

# Graficar el histograma con forma de campana de Gauss
plt.hist(resultados, bins=30, density=True, alpha=0.6, color='b', edgecolor='black', label='Histograma', range=(min_value, max_value))

# Configurar la visualización
plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución Normal y Histograma con Forma de Campana de Gauss')
plt.legend()
plt.grid(True)
plt.show()
