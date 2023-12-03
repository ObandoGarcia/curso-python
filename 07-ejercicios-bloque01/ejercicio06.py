#Mostrar todos las tablas de multiplicar

for cabecera in range(1, 11):
    print(f"------------------Tabla del {cabecera}------------------")
    for numero in range(1, 11):
        print(f"{numero} X {cabecera} = {numero * cabecera}")
    
    print("\n")
    