#Crear un programa que anada valores a una lista mientras < 120
coleccion = []

for contador in range(0, 121):
    coleccion.append(f"Elemento-{contador}")
    print(coleccion[contador])
    
print(coleccion)