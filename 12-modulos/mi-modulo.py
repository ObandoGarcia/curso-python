import main
import datetime

print(main.hola_mundo("Jose Manuel"))

print(datetime.date.today())
fecha = datetime.datetime.now()

fecha_personalizada = fecha.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)

