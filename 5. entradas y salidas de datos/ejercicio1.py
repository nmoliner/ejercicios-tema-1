# Alineado a la derecha en 20 caracteres
resultado1 = "{:>20}".format("Hola Mundo")

# Truncamiento en el cuarto carácter (índice 3)
resultado2 = "{:.3}".format("Hola Mundo")

# Alineamiento al centro en 20 caracteres con truncamiento en el segundo carácter (índice 1)
resultado3 = "{:^20.1}".format("Hola Mundo")

# Formateo a 5 números enteros rellenados con ceros
resultado4 = "{:05d}".format(150)

# Formateo a 7 números enteros rellenados con espacios
resultado5 = "{:7d}".format(7887)

# Formateo a 3 números enteros y 3 números decimales
resultado6 = "{:06.3f}".format(20.02)

# Imprimir resultados
print("Resultado 1:", resultado1)
print("Resultado 2:", resultado2)
print("Resultado 3:", resultado3)
print("Resultado 4:", resultado4)
print("Resultado 5:", resultado5)
print("Resultado 6:", resultado6)
