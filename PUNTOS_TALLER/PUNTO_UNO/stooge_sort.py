import random
import time

def test_sort_algorithm(sort_function, array_size):
    arr = [random.randint(1, 10000) for _ in range(array_size)]

    try:
        start_time = time.time()
        sorted_arr = sort_function(arr)
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Print the execution time with more decimal places
        print(f"Algoritmo: {sort_function.__name__}, Tamaño del arreglo: {array_size}, Tiempo de ejecución: {elapsed_time:.6f} segundos")

        # Print the sorted array (use cautiously for large arrays)
        print("Arreglo ordenado:", sorted_arr)

        # Check if the array is sorted
        assert sorted_arr == sorted(arr), "El arreglo no está ordenado correctamente"

    except Exception as e:
        print(f"Error: {e}")
        print(f"El tiempo de ejecución para el arreglo de tamaño {array_size} fue demasiado largo.")


def stooge_sort(arr):
    if len(arr) <= 1:
        return arr

    if arr[0] > arr[-1]:
        arr[0], arr[-1] = arr[-1], arr[0]

    if len(arr) > 2:
        t = len(arr) // 3
        arr[:t] = stooge_sort(arr[:t])
        arr[-t:] = stooge_sort(arr[-t:])
        arr[:t] = stooge_sort(arr[:t])

    return arr

if __name__ == "__main__":
    arr = [5, 3, 7, 2, 8, 4, 1, 6]
    sorted_arr = stooge_sort(arr.copy())
    print("Lista ordenada (Stooge Sort):", sorted_arr)

    test_sort_algorithm(sorted, 10)
    test_sort_algorithm(sorted, 100)
    test_sort_algorithm(sorted, 1000)
    test_sort_algorithm(sorted, 10000)
