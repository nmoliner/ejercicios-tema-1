matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 6],
    [3, 3, 3, 9],
    [4, 4, 4, 12]
]

for fila in matriz:
    fila[3] = sum(fila[:3])

print(matriz)