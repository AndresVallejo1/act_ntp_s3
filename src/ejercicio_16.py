import time 

minuto = 0
segundo = 0

while minuto < 1:
    print(f"{minuto:02}:{segundo:02}")
    segundo += 1
    if segundo == 60:
        break