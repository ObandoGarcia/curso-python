#Pedir numeros al usuario hasta que ingrese 111

contador = 1
while contador < 25:
    numero = int(input(f"Ingresa un numero: intento: {contador} "))
    if numero == 111:
        break
    else:
        print("No has adivinado")
