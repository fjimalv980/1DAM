# Francisco Jiménez Álvarez
# Ejercicio 5
# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
# C = (F-32)*5/9

# Obtener la temperatura en grados Fahrenheit del usuario
fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))

# Convertir grados Fahrenheit a grados Celsius usando la fórmula
celsius = (fahrenheit - 32) * 5 / 9

# Mostrar el resultado
print("La temperatura en grados Celsius es:", celsius)