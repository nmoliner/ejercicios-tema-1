# Función para mostrar el menú y obtener la opción del usuario
def mostrar_menu():
    print("Menu:")
    print("1. Sumar los dos números")
    print("2. Restar el segundo número del primero")
    print("3. Multiplicar los dos números")
    print("4. Salir")
    opcion = input("Elija una opción (1/2/3/4): ")
    return opcion

# Función para realizar la suma de dos números
def sumar(num1, num2):
    return num1 + num2

# Función para realizar la resta de dos números
def restar(num1, num2):
    return num1 - num2

# Función para realizar la multiplicación de dos números
def multiplicar(num1, num2):
    return num1 * num2

# Función principal del programa
def main():
    # Obtener dos números del usuario
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    # Variable para controlar el bucle del menú
    continuar = True

    while continuar:
        opcion = mostrar_menu()

        if opcion == '1':
            print("La suma de los dos números es:", sumar(num1, num2))
        elif opcion == '2':
            print("La resta del segundo número del primero es:", restar(num1, num2))
        elif opcion == '3':
            print("La multiplicación de los dos números es:", multiplicar(num1, num2))
        elif opcion == '4':
            print("Saliendo del programa...")
            continuar = False
        else:
            print("Opción inválida. Por favor, elija una opción válida (1/2/3/4).")

if __name__ == "__main__":
    main()
