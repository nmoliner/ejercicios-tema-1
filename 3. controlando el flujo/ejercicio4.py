cantidad_numeros = int(input("Ingrese la cantidad de números que desea introducir: "))

suma = 0

for i in range(cantidad_numeros):
    numero = float(input("Ingrese un número: "))
    suma += numero

media = suma / cantidad_numeros

print("La media aritmética de los números ingresados es:", media)
