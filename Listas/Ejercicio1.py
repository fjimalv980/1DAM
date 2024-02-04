# Francisco Jiménez Álvarez
# Ejercicio 1
# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

import random

# Crear lista con 10 valores aleatorios
lista_jimenez = [random.randint(1, 10) for numero_jimenez in range(10)]

# Mostrar cada número de la lista, su cuadrado y su cubo
for numero_jimenez in lista_jimenez:
    cuadrado_jimenez = numero_jimenez ** 2
    cubo_jimenez = numero_jimenez ** 3
    print(f"Número: {numero_jimenez}, Cuadrado: {cuadrado_jimenez}, Cubo: {cubo_jimenez}")