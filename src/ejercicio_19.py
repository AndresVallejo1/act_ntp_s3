frase = "programacion es divertida"
vocales = "aeiou"
contador = 0

for letra in frase.lower():
    if letra in vocales:
        contador += 1
print(f"Total de vocales en la frase: {contador}")  
