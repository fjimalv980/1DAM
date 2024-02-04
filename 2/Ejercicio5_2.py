# Francisco Jiménez Álvarez
# Ejercicio 5
# Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido
# “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.

# Pedir al usuario que ingrese un nombre y una contraseña
nombre = (input("Ingrese su nombre: "))
contraseña = (input("Ingrese su contraseña: "))

# Indicar si el nombre y contraseña son correctos
if (nombre=="pepe" and contraseña=="asdasd"):
    print("Bienvenido, has entrado al sistema")
else:
    print("Nombre o contraseña incorrectos")