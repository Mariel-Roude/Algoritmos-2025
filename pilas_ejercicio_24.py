class PersonajeMCU:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas

    def __str__(self):
        return f"{self.nombre} - {self.cantidad_peliculas} películas"


pila_personajes = [
    PersonajeMCU("Iron Man", 10),
    PersonajeMCU("Groot", 4),
    PersonajeMCU("Rocket Raccoon", 5),
    PersonajeMCU("Black Widow", 7),
    PersonajeMCU("Captain America", 9),
    PersonajeMCU("Doctor Strange", 4),
    PersonajeMCU("Gamora", 3),
    PersonajeMCU("Drax", 3),
]


def buscar_posiciones(pila, nombres):
    posiciones = {}
    for i, personaje in enumerate(reversed(pila), 1):
        if personaje.nombre in nombres:
            posiciones[personaje.nombre] = i
    for nombre in nombres:
        pos = posiciones.get(nombre, "No encontrado")
        print(f"{nombre} está en la posición {pos} desde la cima.")


def personajes_mas_de_cinco(pila):
    print("Personajes con más de 5 películas:")
    for personaje in pila:
        if personaje.cantidad_peliculas > 5:
            print(f"{personaje.nombre} - {personaje.cantidad_peliculas}")


def peliculas_black_widow(pila):
    for personaje in pila:
        if personaje.nombre == "Black Widow":
            print(f"Black Widow participó en {personaje.cantidad_peliculas} películas.")
            return
    print("Black Widow no está en la pila.")


def personajes_por_letra(pila):
    print("Personajes cuyos nombres empiezan con C, D o G:")
    for personaje in pila:
        if personaje.nombre[0].upper() in "CDG":
            print(personaje.nombre)


if __name__ == "__main__":
    print("=== POSICIÓN DE ROCKET Y GROOT ===")
    buscar_posiciones(pila_personajes, ["Rocket Raccoon", "Groot"])
    print("\n=== PERSONAJES CON MÁS DE 5 PELÍCULAS ===")
    personajes_mas_de_cinco(pila_personajes)
    print("\n=== PELÍCULAS DE BLACK WIDOW ===")
    peliculas_black_widow(pila_personajes)
    print("\n=== PERSONAJES CON C, D O G ===")
    personajes_por_letra(pila_personajes)