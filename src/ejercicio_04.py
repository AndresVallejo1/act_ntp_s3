Suma = 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break   
    Suma += numero
print(f"La suma total de los números ingresados es: {Suma}")