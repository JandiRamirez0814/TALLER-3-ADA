import random
import time


def ordenamiento_insercion(arr):
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave


def ordenamiento_fusion(arr):
    if len(arr) > 1:
        medio = len(arr) // 2
        mitad_izquierda = arr[:medio]
        mitad_derecha = arr[medio:]

        ordenamiento_fusion(mitad_izquierda)
        ordenamiento_fusion(mitad_derecha)

        i = j = k = 0

        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                arr[k] = mitad_izquierda[i]
                i += 1
            else:
                arr[k] = mitad_derecha[j]
                j += 1
            k += 1

        while i < len(mitad_izquierda):
            arr[k] = mitad_izquierda[i]
            i += 1
            k += 1

        while j < len(mitad_derecha):
            arr[k] = mitad_derecha[j]
            j += 1
            k += 1


def ordenamiento_rapido(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivote]
    medio = [x for x in arr if x == pivote]
    derecha = [x for x in arr if x > pivote]
    return ordenamiento_rapido(izquierda) + medio + ordenamiento_rapido(derecha)


def medir_tiempo(algoritmo, arr):
    tiempo_inicio = time.time()
    algoritmo(arr)
    tiempo_fin = time.time()
    return tiempo_fin - tiempo_inicio


def ejecutar_experimento(tamano_arreglo):
    arr = [random.randint(1, 1000) for _ in range(tamano_arreglo)]

    # Ejecutar los algoritmos y medir el tiempo
    tiempo_insercion = medir_tiempo(ordenamiento_insercion, arr.copy())
    tiempo_fusion = medir_tiempo(ordenamiento_fusion, arr.copy())
    tiempo_rapido = medir_tiempo(ordenamiento_rapido, arr.copy())

    # Imprimir los resultados
    print(f"Tamaño del Arreglo: {tamano_arreglo}")
    print(f"Tiempo de Ordenamiento por Inserción: {tiempo_insercion:.6f} segundos")
    print(f"Tiempo de Ordenamiento por Fusión: {tiempo_fusion:.6f} segundos")
    print(f"Tiempo de Ordenamiento Rápido: {tiempo_rapido:.6f} segundos")
    print()


# Ejecutar experimentos para diferentes tamaños de arreglos
tamanos_arreglo = [10, 50, 100, 500, 1000, 2000, 5000, 10000]
for tamano in tamanos_arreglo:
    ejecutar_experimento(tamano)
