#Mostrar el porcentaje de de un numero

numero = int(input("Ingresa el numero: "))
porcentaje = int(input(f"Que prcentaje quieres sacar de {numero}?"))

operacion = (numero * (porcentaje / 100))
print(f"El {porcentaje}% de {numero} es {operacion}")