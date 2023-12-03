#Hacer una lista de 8 numeros enteros, ordenarla, mostrar longitud, buscar elemento
numeros = [1, 3, 1, 5, 6, 74]

#Mostrar los numeros de la lista
def mostra_lista(lista):
    resultado = ""
    
    for elemento in lista:
        resultado += str(elemento)
        resultado += "\n"
    
    return resultado
    
#Ordenar
numeros.sort()

#Mostrar la longitud
print(len(numeros))

print(mostra_lista(numeros))

#Buscar elementos de la lista
busqueda = int(input("Introduce un numero"))
comprobar = isinstance(busqueda, int)

while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce un numero"))
else:
    print(f"Has introducido el {busqueda}")
    
search = numeros.index(busqueda)

