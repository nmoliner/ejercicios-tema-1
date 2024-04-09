import sys

# Verificar que se hayan proporcionado los argumentos correctos
if len(sys.argv) != 3:
    print("Uso: python tabla.py <filas> <columnas>")
    sys.exit(1)

# Obtener los argumentos de filas y columnas
filas = int(sys.argv[1])
columnas = int(sys.argv[2])

# Verificar que los argumentos sean números enteros positivos del 1 al 9
if not (1 <= filas <= 9) or not (1 <= columnas <= 9):
    print("Error: Los argumentos deben ser números enteros positivos del 1 al 9.")
    sys.exit(1)

# Imprimir la tabla
for i in range(filas):
    for j in range(columnas):
        print(" * ", end='')
    print()

