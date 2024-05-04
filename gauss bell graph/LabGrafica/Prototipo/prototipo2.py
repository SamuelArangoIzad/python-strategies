import numpy as np
from math import sqrt, log, cos, pi
import matplotlib.pyplot as plt


def cuadrados_medios(seed, n):


    random_numbers = []


    for _ in range(n):


        seed = (seed ** 2) // 100 % 10000


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

numeros_pseudoaleatorios1 = cuadrados_medios(semilla1, 1000)
numeros_pseudoaleatorios2 = cuadrados_medios(semilla2, 1000)

resultados = []



for i in range(len(numeros_pseudoaleatorios1)):

    if numeros_pseudoaleatorios1[i] > 0:

        resultado = sqrt(-2 * log(numeros_pseudoaleatorios1[i])) * cos(2 * pi * numeros_pseudoaleatorios2[i])

        normal = resultado * media + mediana  # Sumar la mediana

        resultados.append(normal)



# Crear un rango de valores alrededor de la media para representar la campana


x = np.linspace(media - 3 * mediana, media + 3 * mediana, 1000)


# Calcular los valores de la distribución normal en este rango


y = 1 / (mediana * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - media) / mediana) ** 2)



# Graficar la campana

plt.plot(x, y, color='r', label='Distribución normal')

plt.fill_between(x, y, color='r', alpha=0.3)  # Rellenar el área bajo la curva



# Graficar los resultados

plt.hist(resultados, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')

# Agregar línea vertical para la media

plt.axvline(x=media, color='g', linestyle='--', linewidth=1.5, label='Media')




print('Media', media)
print('Mediana', mediana)



# Imprimir los 2000 números generados aleatoriamente por la primera semilla

print("Números generados por la primera semilla:")

print(numeros_pseudoaleatorios1)

# Imprimir los 2000 números generados aleatoriamente por la segunda semilla

print("\nNúmeros generados por la segunda semilla:")

print(numeros_pseudoaleatorios2)


plt.xlabel('Valor')
plt.ylabel('Densidad de probabilidad')
plt.title('Histograma de Resultados con Distribución Normal')
plt.legend()
plt.grid(True)
plt.show()