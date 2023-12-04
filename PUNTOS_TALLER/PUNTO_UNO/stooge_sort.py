import random
import time

def stooge_sort(arr, l=0, h=None):
    if h is None:
        h = len(arr) - 1

    if l >= h:
        return

    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]

    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        stooge_sort(arr, l, h - t)
        stooge_sort(arr, l + t, h - t)
        stooge_sort(arr, l, h - t)

def test_stooge_sort(array_size):
    arr = [random.randint(1, 1000) for _ in range(array_size)]
    start_time = time.time()
    stooge_sort(arr)
    end_time = time.time()
    print(f"Tamaño del arreglo: {array_size}, Tiempo de ejecución: {end_time - start_time:.6f} segundos")

if __name__ == "_main_":
    arr = [5, 3, 7, 2, 8, 4, 1, 6]
    stooge_sort(arr)
    print("Lista ordenada:", arr)

    test_stooge_sort(10)
    test_stooge_sort(100)
    test_stooge_sort(1000)
    test_stooge_sort(10000)