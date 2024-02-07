# Se preguntó al copiloto de bing: realiza un código del algoritmo de ordenamiento llamado gnome sort,
# luego se le agregó la creación de 1000 números aleatorios en un rango de 3000.

import time
import matplotlib.pyplot as plt
import random

def gnome_sort(lista):
    i = 0
    while i < len(lista):
        if i == 0 or lista[i-1] <= lista[i]:
            i += 1
        else:
            lista[i], lista[i-1] = lista[i-1], lista[i]
            i -= 1
    return lista

# Lista de prueba
# 1000, 1400, 1800, 2200, 2600
lista_desordenada = [random.randint(0, 2200) for _ in range(3000)]
print (lista_desordenada)

# Medir el tiempo de inicio
inicio = time.time()

# Ordenar la lista
lista_ordenada = gnome_sort(lista_desordenada)
print (lista_ordenada)

# Medir el tiempo de fin
fin = time.time()

# Calcular e imprimir el tiempo de ejecución
tiempo_ejecucion = fin - inicio
print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")