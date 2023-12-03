#Comprobar el tipo de contenido de una variable
def comprobar_tipado(dato, tipo):
    comprobar = isinstance(dato, tipo)
    resultado = ""
    
    if comprobar:
       resultado = f"El tipo de dato de la variable es: {type(dato)}"
    else:
        resultado =  "Incorrecto"
    return resultado

mi_lista = ['Hola mundo', 77]
titulo = "Maestro en Python"
numero = 210
vardadero = True

print(comprobar_tipado(numero, int))