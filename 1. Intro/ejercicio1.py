cadena_corrupta = "zeréP nauJ,01"

# Revertir la cadena
cadena_revertida = cadena_corrupta[::-1]

# Dividir la cadena en nombre y nota
nombre, nota = cadena_revertida.split(',')

# Formatear la cadena en el formato deseado
cadena_formateada = f"{nota} ha sacado un Nota de {nombre}."

print(cadena_formateada)
