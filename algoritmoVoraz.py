#Autor: Juan Fernando Rodríguez Díaz
from productos import producto
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

print("Registe ingresando: nombre del producto \"espacio\" peso \"espacio\" valor. O escriba \"stop\" para parar")
lista = []
while True:
    entrada = input()
    if entrada == "stop":
        break
    entrada = entrada.split()
    lista.append(producto(entrada[0],entrada[1],entrada[2]))
entrada = []
for i in lista:
    entrada.append((int(i.getPeso()),int(i.getValor())))
peso = int(input("Ingrese el peso maximo"))
print(max(entrada,peso))



