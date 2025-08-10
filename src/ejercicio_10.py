""" Mediante un ciclo while, solicita al usuario que escriba palabras. El proceso termina cuando el usuario escriba la palabra “fin”. Al final, muestra cuántas palabras se leyeron (sin contar “fin”). """

palabras = 0
while True:
    palabra = input("Escribe una palabra o 'fin' para terminar: ")
    if palabra.lower() == "fin":
        print("Finalizando el proceso...")
        break
    palabras += 1
    print(f"Fueron escritas en total {palabras} palabras.")