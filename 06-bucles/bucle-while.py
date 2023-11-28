#Bucle while itera un elemento iterable 

contador = 0

while contador <= 100:
    print(contador)
    contador += 1

#Ejerccion de contador con while
numero = int(input("Ingresa la tabla de multiplicar"))

cont = 1
while cont <= 10:
    print(f"{numero} X {cont} = {numero*cont}")
    cont += 1