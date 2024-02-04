# Francisco Jiménez Álvarez
# Ejercicio 3
# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

# Importar librería para operaciones matemáticas
import math

#Pedir catetos de un triángulo rectángulo
print('Dame los catetos del triángulo rectángulo')

cateto1=float(input("Dame la longitud de un cateto"))
cateto2=float(input("Dame la longitud del otro cateto"))

#Operación e impresión del cálculo de la hipotenusa
print('La hipotenusa del triángulo mide',math.sqrt(cateto1**2 + cateto2**2))