#Mostrar las tablas de multiplicar por funciones
def tabla(numero):
    print(f"Tabla de multiplicar de {numero}")
    
    for num in range(1, 11):
        operacion = numero * num
        print(f"{numero} X {num} = {operacion}")
        
    print("\n")
    
tabla(4)