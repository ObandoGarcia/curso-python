persona = {
    "nombre" : "Jose",
    "apellidos" : "Robles",
    "web" : "joseobando.com"
}

#print(persona["apellidos"])

#Combinar lista asociativa
contactos = [
    {
        "nombre" : "Antonio",
        "email" : "obandogarcia10635@gmail.com"
    },
    {
        "nombre" : "Obando",
        "email" : "rene@gmail.com" 
    },
    {
        "nombre" : "Ana",
        "email" : "angabriel@gmail.com"
    }
]

#print(contactos[0]["nombre"])
for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")