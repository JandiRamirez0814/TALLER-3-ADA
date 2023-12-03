import random
import statistics

#Codigo para hallar la moda haciendo uso del algoritmo QuickSort

def pruebas(num):
    lista= [0]*num
    for i in range(num):
        lista[i] = random.randint(1, num)
    partition( lista, 0, len(lista)-1)
    sort(lista,0,num-1)
    lis = statistics.multimode(lista)
    comparar=""
    for i in range(len(lis)):
       comparar+=str(lis[i])+", "
    return "Tamaño del arreglo: "+str(num)+"\nModa del algoritmo construido: "+moda(lista)+"\nModa de la función multimode: "+str(comparar)+"\n"
        
    
def partition(lista, p, r):
    pivot = lista[r]
    i = p - 1
    for j in range(p, r):
        if lista[j] <= pivot:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i+1], lista[r] = lista[r], lista[i+1]
    return i + 1


def sort(lista, p, r):
    if p<r:
      q = partition(lista, p, r)
      sort(lista, p, q-1)
      sort(lista, q+1, r)

#Algoritmo para hallar la moda
def moda(lista):
    cont = 0
    moda = ""
    contador = 0
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            contador += 1
            if contador > cont:
                cont = contador
                moda = str(lista[i])+", "
            elif contador == cont:
                moda+= str(lista[i])+", "
        else:
            contador = 1
    return moda

print(pruebas(10))
print(pruebas(100))
print(pruebas(1000))
print(pruebas(10000))




