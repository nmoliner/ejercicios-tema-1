lista = [1, 2, 3, 4, 5]

try:
    lista[10]
except IndexError:
    print("Error: Index out of range. Please provide a valid index within the range of the list.")

