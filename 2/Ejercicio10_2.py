# Francisco Jiménez Álvarez
# Ejercicio 10
# Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos
# circunferencias y las clasifique en uno de estos estados:
# exteriores, tangentes exteriores, secantes, tangentes interiores, interiores, concéntricas

import math

# Pedir los puntos centrales y radios de las circunferencias
x1 = float(input("Ingrese la coordenada x del centro de una circunferencia: "))
y1 = float(input("Ingrese la coordenada y del centro de una circunferencia: "))
r1 = float(input("Ingrese el radio de una circunferencia: "))

x2 = float(input("Ingrese la coordenada x del centro de otra circunferencia: "))
y2 = float(input("Ingrese la coordenada y del centro de otra circunferencia: "))
r2 = float(input("Ingrese el radio de otra circunferencia: "))

# Calcular la distancia entre los centros de las circunferencias
distanciaCentros = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Clasificar las circunferencias según los estados
if distanciaCentros > r1 + r2:
    print("Las circunferencias son exteriores.")
elif distanciaCentros == r1 + r2:
    print("Las circunferencias son tangentes exteriores.")
elif distanciaCentros < abs(r1 - r2):
    print("Las circunferencias son interiores.")
elif distanciaCentros == abs(r1 - r2):
    print("Las circunferencias son tangentes interiores.")
else:
    print("Las circunferencias son secantes.")
