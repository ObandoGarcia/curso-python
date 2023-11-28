#Listas en Python
frutas = ["manzana", "pera", "uva", "mango", "cereza"]

#Acceder a los indices de las listas
print(frutas[-1])
print(frutas[1:3])

#Añadir elementos a la lista
frutas.append("Ciruela")

#Recorrer elementos de la lista
for fruta in frutas:
    print(fruta)

#Sacar el indice de la lista
for f in frutas:
    print(f"{frutas.index(f)}. {f}")
    
#Agregar elementos con while
peliculas = []
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Ingresa una nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)