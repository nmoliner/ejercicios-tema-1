while True:
    num = int(input("Introduce un número impar: "))
    if num % 2 != 0:
        break
    else:
        print("El número introducido no es impar. Inténtalo de nuevo.")

print("¡Has introducido un número impar correctamente!")