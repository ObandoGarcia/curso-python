#For estructura iterativa que se repite n cantidad de veces
contador = 0

for contador in range(0, 5):
    print("Voy por el " + str(contador))
 
#Ejercicio de tabla de multiplicar   
numero = int(input("Ingrese la tabla de multiplicar a mostrar: "))

if numero < 1:
    numero = 1
    
for num in range(1, 11):
    print(f"{numero} X {num} = {numero * num}")