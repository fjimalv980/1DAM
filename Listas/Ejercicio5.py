# Francisco Jiménez Álvarez
# Ejercicio 5
# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior ordene los elementos de menor a mayor.

import random

# Inicializar lista con 10 números aleatorios
numeros_jimenez = []

for i in range(10):
    numero_jimenez = random.randint(0, 100)
    numeros_jimenez.append(numero_jimenez)

# Ordenar lista de menor a mayor
numeros_jimenez.sort()

# Mostrar lista ordenada
print("Lista de menor a mayor:", numeros_jimenez)