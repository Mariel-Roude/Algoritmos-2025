def romano_a_decimal_recursivo(numero_romano, valores=None):
    if valores is None:
        valores = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
    
    if not numero_romano:
        return 0

    if len(numero_romano) == 1:
        return valores[numero_romano[0]]

    actual = valores[numero_romano[0]]
    siguiente = valores[numero_romano[1]]

    if actual < siguiente:
        return siguiente - actual + romano_a_decimal_recursivo(numero_romano[2:], valores)
    else:
        return actual + romano_a_decimal_recursivo(numero_romano[1:], valores)

print(romano_a_decimal_recursivo("MCMXCIX"))