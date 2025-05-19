class TrajeIronMan:
    def __init__(self, modelo, pelicula, estado):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return f"Modelo: {self.modelo}, Película: {self.pelicula}, Estado: {self.estado}"


pila_trajes = [
    TrajeIronMan("Mark I", "Iron Man", "Dañado"),
    TrajeIronMan("Mark III", "Iron Man", "Destruido"),
    TrajeIronMan("Mark XLIV", "Avengers: Age of Ultron", "Impecable"),
    TrajeIronMan("Mark XLV", "Avengers: Age of Ultron", "Destruido"),
    TrajeIronMan("Mark XLIV", "Avengers: Endgame", "Dañado"),
    TrajeIronMan("Mark XLVI", "Captain America: Civil War", "Impecable"),
    TrajeIronMan("Mark XLVII", "Spider-Man: Homecoming", "Impecable"),
]


def buscar_hulkbuster(pila):
    peliculas = []
    for traje in pila:
        if traje.modelo == "Mark XLIV":
            peliculas.append(traje.pelicula)
    if peliculas:
        print("El modelo Mark XLIV fue utilizado en:")
        for pelicula in peliculas:
            print("-", pelicula)
    else:
        print("El modelo Mark XLIV no fue utilizado.")


def mostrar_dañados(pila):
    print("Trajes dañados:")
    for traje in pila:
        if traje.estado == "Dañado":
            print(traje)


def eliminar_destruidos(pila):
    nueva_pila = []
    print("Trajes destruidos eliminados:")
    while pila:
        traje = pila.pop()
        if traje.estado == "Destruido":
            print(traje.modelo)
        else:
            nueva_pila.append(traje)
    while nueva_pila:
        pila.append(nueva_pila.pop())


def agregar_traje(pila, modelo, pelicula, estado):
    for traje in pila:
        if traje.modelo == modelo and traje.pelicula == pelicula:
            print(f"No se puede agregar {modelo} en {pelicula}: ya existe.")
            return
    pila.append(TrajeIronMan(modelo, pelicula, estado))
    print(f"Modelo {modelo} agregado correctamente.")


def mostrar_trajes_peliculas(pila, peliculas_buscadas):
    print("Trajes usados en las películas indicadas:")
    for traje in pila:
        if traje.pelicula in peliculas_buscadas:
            print(traje.modelo, "-", traje.pelicula)


if __name__ == "__main__":
    print("=== BUSCAR HULKBUSTER ===")
    buscar_hulkbuster(pila_trajes)
    print("\n=== TRAJES DAÑADOS ===")
    mostrar_dañados(pila_trajes)
    print("\n=== ELIMINAR TRAJES DESTRUIDOS ===")
    eliminar_destruidos(pila_trajes)
    print("\n=== AGREGAR TRAJE NUEVO ===")
    agregar_traje(pila_trajes, "Mark LXXXV", "Avengers: Endgame", "Impecable")
    print("\n=== TRAJES EN PELÍCULAS SELECCIONADAS ===")
    mostrar_trajes_peliculas(pila_trajes, ["Spider-Man: Homecoming", "Captain America: Civil War"])
