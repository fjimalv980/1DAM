# Francisco Jiménez Álvarez
# Ejercicio 17
# Crear un programa que añada números a una lista hasta que introducimos un número negativo. A continuación debe crear una nueva lista igual
# que la anterior pero eliminando los números duplicados. Muestra esta segunda lista para comprobar que hemos eliminados los duplicados.

# Listas
lista_jimenez = []
listaLimpia_jimenez = []

# Pedir al usuario los números de la lista
numero_jimenez = int(input("Introduce un número (para terminar introduce uno negativo): "))
while numero_jimenez>=0:
    lista_jimenez.append(numero_jimenez)
    numero_jimenez = int(input("Introduce un número (para terminar introduce uno negativo): "))

# Comprobar la lista y meter en la segunda lista los que no están repetidos
for numero_jimenez in lista_jimenez:
    if numero_jimenez not in listaLimpia_jimenez:
        listaLimpia_jimenez.append(numero_jimenez)

# Mostrar la segunda lista
for numero_jimenez in listaLimpia_jimenez:
    print(numero_jimenez," ",end="")
print()
