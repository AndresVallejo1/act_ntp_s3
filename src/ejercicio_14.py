import random

numero = random.randint(1, 10)
intentos= 0

while True:
    adivinanza = int(input("Adivina el numero del 1 al 10. \n Con intentos infinitos hasta adivinar: "))
    if adivinanza == numero:
        print(f"¡Felicidades! Has adivinado el número y realizaste {intentos + 1} intentos.")
        break
    else:
        print("Inténtalo de nuevo.")
        intentos += 1


