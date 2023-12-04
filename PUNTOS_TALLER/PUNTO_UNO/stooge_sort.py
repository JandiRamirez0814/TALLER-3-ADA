def stooge_sort(arr, i=0, j=None):
    if j is None:
        j = len(arr) - 1

    if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]

    if i + 1 >= j:
        return

    k = (j - i + 1) // 3

    stooge_sort(arr, i, j - k)
    stooge_sort(arr, i + k, j)
    stooge_sort(arr, i, j - k)


# Ejemplo de uso:
arr = [5, 3, 7, 2, 8, 4, 1, 6]
stooge_sort(arr)
print("Lista ordenada:", arr)

import random
import time


def test_stooge_sort(tamano_arreglo):
    arr = [random.randint(1, 1000) for _ in range(tamano_arreglo)]
    tiempo_inicio = time.time()
    stooge_sort(arr)
    tiempo_fin = time.time()
    print(f"Tamaño del arreglo: {tamano_arreglo}, Tiempo de ejecución: {tiempo_fin - tiempo_inicio:.6f} segundos")


# Realizar pruebas con diferentes tamaños de arreglo
test_stooge_sort(10)
test_stooge_sort(100)
test_stooge_sort(1000)
test_stooge_sort(10000)
