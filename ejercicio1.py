#Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales:

# Valores literales
valores = ["Hola Mundo", [1, 10, 100], -25, 1.167, ["Hola", "Mundo"]]

# Iterar sobre los valores y mostrar su tipo
for valor in valores:
    print(f"El tipo de dato de {valor} es {type(valor).__name__}")

Check for Updates