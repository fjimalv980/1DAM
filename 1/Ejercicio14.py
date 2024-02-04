# Francisco Jimñenez Álvarez
# Ejercicio 14
# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

# Pedir al usuario un número de dos cifras
numero = int(input("Ingrese un número de dos cifras: "))

# Obtener las cifras individuales
unidades = numero % 10
decenas = numero // 10

# Invertir el número
numeroInvertido = unidades * 10 + decenas

# Mostrar el número invertido
print("El número invertido es:", numeroInvertido)