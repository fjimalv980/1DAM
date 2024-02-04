# Francisco Jiménez Álvarez
# Ejercicio 1
# Algoritmo que pida dos números e indique
# si el primero es mayor que el segundo o no.

# Pedir al usuario dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Comparar los números y mostrar el resultado
if numero1 > numero2:
    print(numero1, "es mayor que", numero2)
elif numero1 < numero2:
    print(numero1, "es menor que", numero2)
else:
    print("Ambos números son iguales.")