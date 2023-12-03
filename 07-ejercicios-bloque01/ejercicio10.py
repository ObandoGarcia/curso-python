#Pedir la nota de 15 alunmos, y mostrar cuantos han aprobado y cuantos han reprobado

contador = 1
aprobados = 0
reprobados = 0

numero_alumnos = int(input("Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"Ingrese la nota del alumno {contador}"))
    if nota >= 5:
        aprobados += 1
    else:
        reprobados += 1
        
    contador += 1
    
print(f"El numero de alumnos aprobados es {aprobados}")
print(f"El numero de alumnos reprobados es {reprobados}")