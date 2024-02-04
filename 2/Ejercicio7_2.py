# Francisco Jiménez Álvarez
# Ejercicio 7
# Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas:
# El exponente sea positivo, sólo tienes que imprimir la potencia.
# El exponente sea 0, el resultado es 1.
# El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

from math import pow

# Pedir al usuario un número y su exponente
base = float(input("Ingresa un número: "))
exponente = int(input("Ingresa su exponente: "))

# Calcular potencia con exponente negativo
if exponente<0:
    print("Su potencia es: ",pow(1/base,abs(exponente)))
# Calcular potencia con exponente 0
elif exponente==0:
    print("Su potencia es: 1")
# Calcular potencia con exponente positivo
else:
    print("Su potencia es: ",pow(base,exponente))