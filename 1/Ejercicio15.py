# Francisco Jiménez Álvarez
# Ejercicio 15
# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

# Pedir al usuario que ingrese los valores de las variables A y B
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))

# Intercambiar los valores usando una variable temporal
cambio = A
A = B
B = cambio

# Mostrar los valores intercambiados
print("Tras el intercambio, el valor de A es:", A)
print("Tras el intercambio, el valor de B es:", B)