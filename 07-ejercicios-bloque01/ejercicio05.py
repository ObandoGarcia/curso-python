#Mostrar todos los numeros entre dos numeros 

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))

if num1 < num2:
    for contador in range(num1, (num2 + 1)):
        print(contador)
else:
    print("El numero 1 debe ser menor al numero 2")