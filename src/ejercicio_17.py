while True:
    numero = input("Ingrese un número entero positivo: ")
    if numero.isdigit() and int(numero) >= 0:
        break
    print("Por favor, ingrese un número entero positivo válido.")

    suma_digitos = sum(int(digito) for digito in numero)
print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
