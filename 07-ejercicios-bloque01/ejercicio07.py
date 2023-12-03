#Mostrar todos los numeros impares entre dos numeros 

numero1 = int(input("Ingrese el numero 1: "))
numero2 = int(input("Ingrese el numero 2: "))

if numero1 < numero2:
    for num in range(numero1, (numero2 + 1)):
        if num % 2 == 0:
            print(f"{num} es PAR")
        else:
            print(f"{num} es impar")
else:
    print("El numero 1 debe ser menor al numero 2")