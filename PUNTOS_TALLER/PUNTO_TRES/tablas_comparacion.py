import time
import random
import math

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


def tabla1(tamano_arreglo):
    arr = [random.randint(1, 1000) for _ in range(tamano_arreglo)]
    tiempo_insercion = medir_tiempo(ordenamiento_insercion, arr.copy())
    constante= tiempo_insercion/(tamano_arreglo*(math.log(tamano_arreglo)))
    print("{:<15} {:<30} {:<20} {:<10}".format(tamano_arreglo, tiempo_insercion, tamano_arreglo**2, constante))

def tabla2(tamano_arreglo):
    arr = [random.randint(1, 1000) for _ in range(tamano_arreglo)]
    tiempo_fusion = medir_tiempo(ordenamiento_fusion, arr.copy())
    constante= tiempo_fusion/(tamano_arreglo**2)
    print("{:<15} {:<30} {:<20} {:<10}".format(tamano_arreglo, tiempo_fusion, tamano_arreglo*(math.log(tamano_arreglo)), constante))

def tabla3(tamano_arreglo):
    arr = [random.randint(1, 1000) for _ in range(tamano_arreglo)]
    tiempo_rapido = medir_tiempo(ordenamiento_rapido, arr.copy())
    constante= tiempo_rapido/(tamano_arreglo*(math.log(tamano_arreglo)))
    print("{:<15} {:<30} {:<20} {:<10}".format(tamano_arreglo, tiempo_rapido, tamano_arreglo*(math.log(tamano_arreglo)), constante))

tamanos_arreglo = [10,10,10, 50,50,50,100,100,100, 500,500,500,1000,1000, 1000,2000,2000, 2000,5000,5000, 5000,10000,10000, 10000]

print("{:<15} {:<30} {:<20} {:<10}".format("TAMAÑO ENTRADA", "TIEMPO ORDENAMIENTO INSERCION", "COMPLEJIDAD INSERCION", "CONSTANTE INSERCION"))
for tamano in tamanos_arreglo:
    tabla1(tamano)

print("\n----------------------------------\n")

print("{:<15} {:<30} {:<20} {:<10}".format("TAMAÑO ENTRADA", "TIEMPO ORDENAMIENTO FUSION", "COMPLEJIDAD FUSION", "CONSTANTE FUSION"))
for tamano in tamanos_arreglo:
    tabla2(tamano)

print("\n----------------------------------\n")

print("{:<15} {:<30} {:<20} {:<10}".format("TAMAÑO ENTRADA", "TIEMPO ORDENAMIENTO RAPIDO", "COMPLEJIDAD RAPIDO",   "CONSTANTE RAPIDO"))
for tamano in tamanos_arreglo:
    tabla3(tamano)

print("\n----------------------------------\n")