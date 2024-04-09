# Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}

# Crea un conjunto llamado administradores con los administradores Juan y Marta
administradores = {"Juan", "Marta"}

# Borra al administrador Juan del conjunto de administradores
administradores.discard("Juan")

# Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios
administradores.add("Marcos")

# Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no
for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "es administrador")
    else:
        print(usuario, "no es administrador")

