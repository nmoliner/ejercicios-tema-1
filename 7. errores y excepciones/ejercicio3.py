colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }

try:
    colores['blanco']
except KeyError:
    print("El color 'blanco' no está definido en el diccionario de colores.")
