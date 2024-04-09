import sys

def descomponer_numero(numero):
    numero_str = str(numero)
    longitud = len(numero_str)
    descomposicion = []
    
    for i, digito in enumerate(numero_str):
        valor = int(digito) * 10**(longitud - i - 1)
        descomposicion.append(valor)
    
    return descomposicion

def mostrar_descomposicion(numero):
    descomposicion = descomponer_numero(numero)
    
    for valor in descomposicion:
        print("{:04d}".format(valor))

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    mostrar_descomposicion(numero)
else:
    print("Uso: python descomposicion.py <numero>")



