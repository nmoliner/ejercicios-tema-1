try:
    resultado = 15 + "20"
except TypeError:
    raise Exception("Error: Cannot perform addition between an integer and a string.")
