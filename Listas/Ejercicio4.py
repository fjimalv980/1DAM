# Francisco Jiménez Álvarez
# Ejercicio 4
# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los elementos introducidos).

# Inicializar lista vacía
lista_jimenez = []

# Pedir al usuario números para rellenar la lista hasta que ponga uno negativo
print("Crea una lista de números hasta que pongas uno negativo")

while True:
    numero_jimenez = int(input("Introduce un número: "))
    if numero_jimenez < 0:
        break
    lista_jimenez.append(numero_jimenez)

# Mostrar los números de la lista
print("La lista introducida es introducido es:")
for i in lista_jimenez:
    print(i)