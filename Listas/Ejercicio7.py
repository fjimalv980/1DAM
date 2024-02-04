# Francisco Jiménez Álvarez
# Ejercicio 7
# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

# Variables de listas
lista1_jimenez = []
lista2_jimenez = []
lista3_jimenez = []

# Pedir al usuario valores de lista1
print("Ingresa 5 valores para la lista1:")
for i in range(5):
    valor_jimenez = int(input(f"Valor {i+1}: "))
    lista1_jimenez.append(valor_jimenez)

# Pedir al usuario valores de lista2
print("Ingresa 5 valores para la lista2:")
for i in range(5):
    valor_jimenez = int(input(f"Valor {i+1}: "))
    lista2_jimenez.append(valor_jimenez)

# Calcular la suma de lista1 y lista2
for i in range(5):
    valor_jimenez = lista1_jimenez[i] + lista2_jimenez[i]
    lista3_jimenez.append(valor_jimenez)

# Imprimir el resultado
print(f"La suma de la lista1 y la lista2 es: {lista3_jimenez}")