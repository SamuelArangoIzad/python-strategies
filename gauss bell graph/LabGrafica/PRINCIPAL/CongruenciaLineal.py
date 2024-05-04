import numpy as np
from math import sqrt, log, cos, pi
import matplotlib.pyplot as plt

"""

LOGICA -----------------------------------------------------------------------------------------------------------------

"""

def congruencia_lineal(semilla, a, c, m, iteraciones):


    numeros_generados = []


    for _ in range(iteraciones):


        semilla = (a * semilla + c) % m


        numeros_generados.append(semilla / m)


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

a = 1664525
c = 1013904223
m = 2 ** 32

# Generar 1000 números pseudoaleatorios para cada semilla (aumentamos la cantidad)
numeros_pseudoaleatorios1 = congruencia_lineal(semilla1, a, c, m, 1000)
numeros_pseudoaleatorios2 = congruencia_lineal(semilla2, a, c, m, 1000)





"""

CONSOLA ----------------------------------------------------------------------------------------------------------------

"""

#MEDIA Y MEDIANA DE MI ID

print('Media Id', media)
print('Mediana Id', mediana)



print("Números generados por la primera semilla:")
print(numeros_pseudoaleatorios1)

print("\nNúmeros generados por la segunda semilla:")
print(numeros_pseudoaleatorios2)



# MEZCLAR NUMEROS GENERADOS EN AMBAS PARTES DE SEMILLA


todos_numeros = numeros_pseudoaleatorios1 + numeros_pseudoaleatorios2



# CALCULO DE MEDIA , MEDIANA Y MODA DE LOS 2000 NUMEROS PSEUDOALEATORIOS


media_total = np.mean(todos_numeros)
mediana_total = np.median(todos_numeros)

print('\nMedia de los números:', media_total)
print('Mediana de los números:', mediana_total)


resultados = []


for i in range(len(numeros_pseudoaleatorios1)):

    # SE AJUSTA PARA QUE SIGA UNA DISTRIBUCION DE CAMPANA CON BASE A LA FORMULA DADA POR LE PROFESOR
    resultado = sqrt(-2 * log(numeros_pseudoaleatorios1[i])) * cos(2 * pi * numeros_pseudoaleatorios2[i])

    # ALMACENAMOS LOS RESULTADOS EN UNA DISTRIBUCION CAMPANA
    resultados.append(resultado)



# AGREGAR LA LINEA DEL ID

plt.axvline(x=media, color='g', linestyle='--', linewidth=1.5, label='Media de Id')


# GRAFICA DE RESULTADOS

plt.hist(resultados, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')




# MEDIA DE LOS 2000 NUMEROS Y SU RESPECTIVA MEDIANA

plt.axvline(x=media_total, color='r', linestyle='-', linewidth=2.5, label='Media Total (2000 numeros)')
plt.axvline(x=mediana_total, color='k', linestyle='-', linewidth=2.0, label='Mediana Total (2000 numeros)')




plt.xlabel('Valor de los resultados')
plt.ylabel('Frecuencia')
plt.title('Histograma de Resultados')
plt.grid(True)
plt.legend()
plt.show()
