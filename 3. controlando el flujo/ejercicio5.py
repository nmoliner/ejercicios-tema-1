# Lista de números
numeros = [1, 3, 5, 7, 9]

# Solicitar al usuario un número entero del 0 al 9
while True:
    numero = int(input("Ingrese un número entero del 0 al 9: "))
    if numero >= 0 and numero <= 9:
        break
    else:
        print("Número incorrecto. Inténtelo nuevamente.")

# Comprobar si el número se encuentra en la lista
if numero in numeros:
    print("El número", numero, "se encuentra en la lista.")
else:
    print("El número", numero, "no se encuentra en la lista.")