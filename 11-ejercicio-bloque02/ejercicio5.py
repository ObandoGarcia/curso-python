#Crear una lista con el contenido de una tabla
tabla = [
    {
        "categoria" : "ACCION",
        "Juegos" : [
            "GTA", "COD", "PUGB"
        ]
    },
    {
        "categoria" : "AVENTURA",
        "Juegos" : [
            "PRINCE", "ASSASINS", "CRASH"
        ]
    },
    {
        "categoria" : "DEPORTES",
        "Juegos" : [
            "FIFA", "PRO", "MOTO GP"
        ]
    }
]

for categoria in tabla:
    print(f"Categoria: {categoria['categoria']}")
    for juego in categoria['Juegos']:
        print(f"Juego: {juego}")