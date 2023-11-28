#Funciones dentro de otras funciones
def obtner_nombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def obtner_apellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto

def devuelve_todo(nombre, apellido):
    texto = obtner_nombre(nombre) + obtner_apellido(apellido)
    return texto

#Llamado
print(devuelve_todo("Jose", "Obando"))