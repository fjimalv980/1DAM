# Francisco Jimñenez Álvarez
# Ejercicio 12
# Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

# Importar librería para operaciones matemáticas
import math

# Pedir al usuario las coordenadas del primer punto
x1 = float(input("Ingrese la coordenada x del primer punto: "))
y1 = float(input("Ingrese la coordenada y del primer punto: "))

# Pedir al usuario las coordenadas del segundo punto
x2 = float(input("Ingrese la coordenada x del segundo punto: "))
y2 = float(input("Ingrese la coordenada y del segundo punto: "))

# Calcular la distancia entre los dos puntos usando la fórmula de distancia euclidiana
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Imprimir la distancia entre los dos puntos
print("La distancia entre los puntos (", x1, ",", y1, ") y (", x2, ",", y2, ") es: ", distancia)