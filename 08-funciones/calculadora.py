#Funciones de una calculadora
def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1  / numero2
    cadena = ""
    
    cadena += "Suma: " + str(suma)
    cadena += "\n"
    cadena += "Resta: " + str(resta)
    cadena += "\n"
    cadena += "Multiplicacio: " + str(multiplicacion)
    cadena += "\n"
    cadena += "Division" + str(division) 
    
    return cadena

