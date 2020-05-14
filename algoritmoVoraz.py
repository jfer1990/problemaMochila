#Autor: Juan Fernando Rodríguez Díaz
from algoritmos import *
def retornaLista(cadena):
    lista = list()
    if (len(cadena))%2 == 0:
        for x,y in zip(cadena[0::2],cadena[1::2]):
            x = int(x)
            y = int(y)
            lista.append((x,y))
        return lista
    else:
        return False



entrada =input("Ingrese un peso y un valor: ").split()
peso = int(input("Ingrese el peso maximo"))
lista = retornaLista(entrada)
print(max(lista,peso))



