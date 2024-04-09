# Leer los dos números por teclado
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Determinar si los dos números son iguales
son_iguales = numero1 == numero2

# Determinar si los dos números son diferentes
son_diferentes = numero1 != numero2

# Determinar si el primero es mayor que el segundo
primero_mayor = numero1 > numero2

# Determinar si el segundo es mayor o igual que el primero
segundo_mayor_igual = numero2 >= numero1

# Mostrar los resultados
print("Los dos números son iguales:", son_iguales)
print("Los dos números son diferentes:", son_diferentes)
print("El primero es mayor que el segundo:", primero_mayor)
print("El segundo es mayor o igual que el primero:", segundo_mayor_igual)