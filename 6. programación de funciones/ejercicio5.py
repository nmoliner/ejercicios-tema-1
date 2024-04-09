def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    else:
        return numero

resultado = recortar(15, 0, 10)
print(resultado)