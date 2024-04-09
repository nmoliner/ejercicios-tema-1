def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

# Testing the function
print(relacion(5, 10))  # Output: -1
print(relacion(10, 5))  # Output: 1
print(relacion(5, 5))   # Output: 0

