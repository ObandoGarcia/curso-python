#IF anidados
nombre = "Jose Obando"
ciudad = "Izalco"
continente = "EU"
edad = 78
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if continente != "America":
        print("El usuario no es Americano")
    else:
        print(f"Es Americano y de {continente}")
else:
    print(f"{nombre} no es mayor de edad")