def usar_la_fuerza(mochila, indice=0):

   
    if indice >= len(mochila):
        return False, indice

   
    if mochila[indice] == "sable de luz":
        return True, indice + 1

   
    return usar_la_fuerza(mochila, indice + 1)


mochila = ["comida", "agua", "herramientas", "sable de luz", "ropa"]
encontrado, objetos_sacados = usar_la_fuerza(mochila)

if encontrado:
    print(f"Sable de luz encontrado después de sacar {objetos_sacados} objetos.")
else:
    print("No se encontró un sable de luz en la mochila.")