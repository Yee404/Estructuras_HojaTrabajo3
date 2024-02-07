# Este código combina todos los algoritmos de ordenamiento, los cuales comparten la lista desordenada,
# con el fin de ahorrar tiempo y obtener el tiempo de una cantidad de variables de una vez para cada algoritmo.


import time
import random
# 1000, 2000, 3000, 4000, 5000
lista_desordenada = [random.randint(0, 5000) for _ in range(5100)]

#__GNOME SORT_____________________________________________________________________________________________________
# Se preguntó al copiloto de bing: realiza un código del algoritmo de ordenamiento llamado gnome sort calculando el tiempo de ordenamiento
def gnome_sort(lista):
    i = 0
    while i < len(lista):
        if i == 0 or lista[i-1] <= lista[i]:
            i += 1
        else:
            lista[i], lista[i-1] = lista[i-1], lista[i]
            i -= 1
    return lista


inicio = time.time()
lista_ordenada = gnome_sort(lista_desordenada)
fin = time.time()

# Calcular e imprimir el tiempo de ejecución
print(f"TGNOME: {fin - inicio}")


#__MERGE SORT_____________________________________________________________________________________________________
def merge_sort(lista_desordenada):
    if len(lista_desordenada) <= 1:
        return lista_desordenada

    medio = len(lista_desordenada) // 2
    izquierda = lista_desordenada[:medio]
    derecha = lista_desordenada[medio:]

    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    lista_ordenada = []
    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            lista_ordenada.append(izquierda[i])
            i += 1
        else:
            lista_ordenada.append(derecha[j])
            j += 1

    while i < len(izquierda):
        lista_ordenada.append(izquierda[i])
        i += 1

    while j < len(derecha):
        lista_ordenada.append(derecha[j])
        j += 1

    return lista_ordenada

inicio = time.time()
lista_ordenada = merge_sort(lista_desordenada)
fin = time.time()
print(f"TMERGE: {fin - inicio}")


#__QUICK SORT_____________________________________________________________________________________________________
def quick_sort(lista_desordenada):
    if len(lista_desordenada) <= 1:
        return lista_desordenada
    else:
        pivote = lista_desordenada[len(lista_desordenada) // 2]
        menores = [x for x in lista_desordenada if x < pivote]
        iguales = [x for x in lista_desordenada if x == pivote]
        mayores = [x for x in lista_desordenada if x > pivote]
        return quick_sort(menores) + iguales + quick_sort(mayores)

inicio = time.time()
lista_ordenada = quick_sort(lista_desordenada)
fin = time.time()
print(f"TQUICK: {fin - inicio}")


#__RADIX SORT_____________________________________________________________________________________________________
def counting_sort(lista_desordenada, exponente):
    n = len(lista_desordenada)
    lista_ordenada = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (lista_desordenada[i] // exponente) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (lista_desordenada[i] // exponente) % 10
        lista_ordenada[count[index] - 1] = lista_desordenada[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        lista_desordenada[i] = lista_ordenada[i]

def radix_sort(lista_desordenada):
    maximo = max(lista_desordenada)
    exponente = 1
    while maximo // exponente > 0:
        counting_sort(lista_desordenada, exponente)
        exponente *= 10

inicio = time.time()
radix_sort(lista_desordenada)
fin = time.time()
print(f"TRADIX: {fin - inicio}")


#__SELECTION SORT_____________________________________________________________________________________________________
def selection_sort(lista_desordenada):
    for i in range(len(lista_desordenada)):
        min_idx = i
        for j in range(i+1, len(lista_desordenada)):
            if lista_desordenada[j] < lista_desordenada[min_idx]:
                min_idx = j
        lista_desordenada[i], lista_desordenada[min_idx] = lista_desordenada[min_idx], lista_desordenada[i]

inicio = time.time()
selection_sort(lista_desordenada)
fin = time.time()
print(f"TSELECTION: {fin - inicio}")


#__SHELL SORT_____________________________________________________________________________________________________
def shell_sort(lista_desordenada):
    n = len(lista_desordenada)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = lista_desordenada[i]
            j = i
            while j >= gap and lista_desordenada[j - gap] > temp:
                lista_desordenada[j] = lista_desordenada[j - gap]
                j -= gap
            lista_desordenada[j] = temp
        gap //= 2

inicio = time.time()
shell_sort(lista_desordenada)
fin = time.time()
print(f"TSHELL: {fin - inicio}")


#__HEAP SORT_____________________________________________________________________________________________________
def heapify(lista_desordenada, n, i):
    mayor = i
    izq = 2 * i + 1
    der = 2 * i + 2

    if izq < n and lista_desordenada[i] < lista_desordenada[izq]:
        mayor = izq

    if der < n and lista_desordenada[mayor] < lista_desordenada[der]:
        mayor = der

    if mayor != i:
        lista_desordenada[i], lista_desordenada[mayor] = lista_desordenada[mayor], lista_desordenada[i]
        heapify(lista_desordenada, n, mayor)

def heap_sort(lista_desordenada):
    n = len(lista_desordenada)

    for i in range(n, -1, -1):
        heapify(lista_desordenada, n, i)

    for i in range(n-1, 0, -1):
        lista_desordenada[i], lista_desordenada[0] = lista_desordenada[0], lista_desordenada[i]
        heapify(lista_desordenada, i, 0)

inicio = time.time()
heap_sort(lista_desordenada)
fin = time.time()
print(f"THEAP: {fin - inicio}")



