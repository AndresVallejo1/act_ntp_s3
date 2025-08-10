""" Utilizando un ciclo while, simula un reloj digital que muestre cada segundo desde 00:00 hasta 00:59 en formato MM:SS, cada valor en una línea. """

import time 

minuto = 0
segundo = 0

while minuto < 1:
    print(f"{minuto:02}:{segundo:02}")
    segundo += 1
    if segundo == 60:
        break