import io
import pathlib
import shutil
import os

#abrir archivo
ruta = str(pathlib.Path().absolute()) + "/13-ficheros/fichero_texto.txt"
archivo = io.open(ruta, "a+")

archivo.write("Soy un texto de ejemplo\n")

archivo.close()

#abrir archivo
ruta = str(pathlib.Path().absolute()) + "/13-ficheros/fichero_texto.txt"
archivo_lectura = io.open(ruta, "r")

#contenido = archivo_lectura.read()
#print(contenido)

#Agregar elemento es lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

print(lista)

ruta_original = ruta = str(pathlib.Path().absolute()) + "/13-ficheros/fichero_texto.txt"
#Copiar
#shutil.copyfile()

#os.remove(ruta)

#comprobar si existe
print(os.path.abspath("./"))

#comprobar si existe
if os.path.isfile(os.path.abspath("./") + "fichero_texto.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")