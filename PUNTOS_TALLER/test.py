import random
import statistics

#Codigo para hallar la moda haciendo uso del algoritmo QuickSort
num= int(input("Ingrese el tamaño del arreglo: "))
lista= [0]*num
for i in range(num):
    lista[i] = random.randint(1, num)

        
    
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


partition( lista, 0, len(lista)-1)
sort(lista,0,num-1)

def moda(lista):
    comple=0
    cont = 0
    comple+=1
    moda = ""
    comple+=1
    contador = 0
    comple+=1
    for i in range(len(lista) - 1):
        comple+=1
        if lista[i] == lista[i + 1]:
            comple+=1
            contador += 1
            comple+=1
            if contador > cont:
                comple+=1
                cont = contador
                comple+=1
                moda = str(lista[i])+", "
                comple+=1
            elif contador == cont:
                comple+=1
                moda+= str(lista[i])+", "
                comple+=1
        else:
            comple+=1
            contador = 1
            comple+=1
    comple+=1
    return comple

l1=1
l2=1
l3=1
l4=num
l5=1
l6=1
l7=1
l8=1
l9=1
l10=1
l11=1
l12=1
l13=1

lis=l1+l2+l3+l4+l5+l6+l7+l8+l9+l10+l11+l12+l13

print("Tamaño del arreglo: "+str(num)+"\nComplejidad: "+str(moda(lista))+"\nAlgoritmo: "+str(lis)+"\n")