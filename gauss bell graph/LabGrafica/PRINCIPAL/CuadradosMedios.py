import numpy as np
from math import sqrt, log, cos, pi
import matplotlib.pyplot as plt

def cuadrados_medios(semilla, iteraciones, digitos):


    numeros_generados = []


    for _ in range(iteraciones):


        semilla = int(str(semilla ** 2).zfill(2 * digitos)[digitos//2:-digitos//2])


        numeros_generados.append(semilla / 10 ** digitos)


    return numeros_generados

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



# Cambiar los parámetros para ajustarse al método de cuadrados medios

digitos = 7

iteraciones = 1000

# Generar números pseudoaleatorios utilizando cuadrados medios


numeros_pseudoaleatorios1 = cuadrados_medios(semilla1, iteraciones, digitos)


numeros_pseudoaleatorios2 = cuadrados_medios(semilla2, iteraciones, digitos)




# Asegurar que los valores sean mayores que cero


epsilon = 1e-10


numeros_pseudoaleatorios1 = [max(epsilon, x) for x in numeros_pseudoaleatorios1]




# Calcular la media y la mediana de los números generados


todos_numeros = numeros_pseudoaleatorios1 + numeros_pseudoaleatorios2


media_total = np.mean(todos_numeros)


mediana_total = np.median(todos_numeros)




# Generar la distribución de campana de Gauss a partir de los números pseudoaleatorios


resultados = []


for i in range(len(numeros_pseudoaleatorios1)):


    resultado = sqrt(-2 * log(numeros_pseudoaleatorios1[i])) * cos(2 * pi * numeros_pseudoaleatorios2[i])


    resultados.append(resultado)

print("Números generados:")
for num in todos_numeros:
    print(num)


print('Media',media_total)


print('Mediana',mediana_total)

# Graficar el histograma
plt.hist(resultados, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')


plt.axvline(x=media_total, color='r', linestyle='-', linewidth=2.5, label='Media Total ')
plt.axvline(x=mediana_total, color='k', linestyle='-', linewidth=2.0, label='Mediana Total')
plt.axvline(x=media, color='k', linestyle='-', linewidth=2.0, label='Media ID')

plt.xlabel('Valor de los resultados')
plt.ylabel('Frecuencia')
plt.title('Histograma de Resultados')
plt.grid(True)
plt.legend()
plt.show()
