#Las cadenas de texto son parecidas a las listas
cadena = "Hola mundo"
print( cadena[0])

for c in cadena:
    print(c)

#Hcer minúscula
print (cadena.lower())

#volver mayúscula la cadena del primer elemento
print(cadena.capitalize())

#preguntar si la cadena empieza con algo en particular
print(cadena.startswith("Hola"))
print(cadena.endswith("mundo"))
print(cadena.isalpha())
print(cadena.isdigit())
print(cadena.strip()) #elimina espacios

#Transforma un string en una lista por un separador
frutas = "Durazno, Manzanas, Papaya"
print(frutas.split(","))
lista = frutas.split(",")
#unir por un caracter
cadena2 = "-".join(lista)
print(cadena2)
