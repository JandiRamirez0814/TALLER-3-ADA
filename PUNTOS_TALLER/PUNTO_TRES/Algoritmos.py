import random
import numpy as np

#pido un numero para generar un arreglo aleatorio
num= int(input("Tamaño del arreglo: "))
    
#Algoritmos de ordenamiento Quicksort
def quickSort(list):
    if len(list) <= 1:
        return list
    pivote = list[len(list) // 2]
    left = [x for x in list if x < pivote]
    division = [x for x in list if x == pivote]
    right = [x for x in list if x > pivote]
    return quickSort(left) + division + quickSort(right)

#Algoritmo de ordenamiento InsertionSort
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr

#Algoritmo de ordenamiento MergeSort
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def mergeSort(list):
    if len(list) <= 1:
        return list
    mitad = len(list) // 2
    left = mergeSort(list[:mitad])
    right = mergeSort(list[mitad:])
    return merge(left, right)


lista= [0]*num
for i in range(num):
    lista[i] = random.randint(1, num)
    
other= np.sort(lista, kind='quicksort')
print("\nQuickSort: "+str(quickSort(lista))+ "\nQuickSort de numpy: "+str(other)+"\n")


lista2= [0]*num
for i in range(num):
    lista2[i] = random.randint(1, num)
    
print("InsertionSort: "+str(insertionSort(lista2))+"\n")  

lista3= [0]*num
for i in range(num):
    lista3[i] = random.randint(1, num)
    
other2= np.sort(lista3, kind='mergesort')
print("MergeSort: "+str(mergeSort(lista3))+ "\nMergeSort de numpy: "+str(other2))
