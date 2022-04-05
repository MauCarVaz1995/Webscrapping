#Listas indexadas
numeros = [3, 5, 6, 6, 7]
print(numeros[0])
#el ultimo elemento de la lista
print(numeros[-1])
#añadiendo elemento al final
numeros.append(10)
#eliminar elementos de una lista por valor
numeros.remove(6)
print(numeros)
#eliminando por índice
numeros.pop(1)
print(numeros)
#Cambiar elementos
numeros[0] = 10
print(numeros)
#preguntar
print(6 in numeros)
#ordenar en ascendente sort
numeros.sort()
numeros.reverse()
#recorrer una colección através de los valores
for elem in numeros:
    print(elem)

#con un indice a través de un indice
for i in range(len(numeros)):
    print(numeros[i] )

#los dos textos hacen exactamente lo mismo
