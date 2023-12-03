#Metodos predefinidos
cantantes = ['A', 'B', 'C', 'D', 'E']
numeros = [11, 20, 34, 4, 5]

#Ordenar lista
numeros.sort()

#Agregar elementos
cantantes.insert(1, "David Disval")

#Eliminar elementos
cantantes.pop(1)

#Eliminar por el valor
cantantes.remove('B')

#Dar la vuelta
numeros.reverse()

#Buscar un elemento dentro de la lista
print("D" in cantantes)

#Veces aparece un elemento
print(numeros.count(34))

#indice de una lista
print(cantantes.index("E"))

#Unir dos listas
cantantes.extend(numeros)
