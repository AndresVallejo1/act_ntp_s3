edades = []
while True:
    edad = int(input("Ingrese una edad (-1 para terminar): "))
    if edad == -1:
        break
    edades.append(edad) 
if edades:
    edad_mayor = max(edades)
    print(f"La edad mayor ingresada es: {edad_mayor}")
else:
    print("No se ingresaron edades válidas.")

