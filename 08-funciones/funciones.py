#Definiendo funciones 
def mostrarNombres():
    print("Jose Manuel Obando")
        
#Parametros de la funcion
def mostrarNombre2(nombre):
    print(f"Me llamo: {nombre}")
    
#Parametros opcionales
def obtener_empleado(nombre, dni = None):
    print(nombre)
    if dni != None:
        print (dni)
    
#Devolucion de datos
def saludo(nombre):
    saludo = f"Hola, te saludo {nombre}"
    return saludo
