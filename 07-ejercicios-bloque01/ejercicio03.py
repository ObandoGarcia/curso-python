#Imprimir por pantalla los cuadrados de los primeros 60 numeros naturales
contador = 0
while contador <= 60:
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador += 1
    
#Con for
for num in range(1, 61):
    cuadrado = num * num
    print(f"El cuadrado de {num} es {cuadrado}")