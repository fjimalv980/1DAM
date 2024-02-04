# Francisco Jiménez Álvarez
# Ejercicio 12
# Escribir un programa que lea un año indicar si es bisiesto. 
# Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.

# Pedir al usuario que escriba un año
año = int(input("Ingrese un año: "))

# Comprobar si el año es bisiesto e imprimir sí o no
if (año % 4 == 0) and ((año % 100 != 0) or (año % 400 == 0)):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")