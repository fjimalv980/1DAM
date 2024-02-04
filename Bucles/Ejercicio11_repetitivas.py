# Francisco Jiménez Álvarez
# Ejercicio 11
# Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número.

import math


# Pedir al usuario que ingrese un número
numero_jimenez=int(input("Ingrese un número: "))
primo_jimenez=False

if numero_jimenez<2:
    print(f"{numero_jimenez} no es un número primo.")
    
else:
    primo_jimenez=True

    # Verificar hasta raíz cuadrada del número
    limite_jimenez=int(math.sqrt(numero_jimenez))+1

    # Verificar si es divisible por otro número
    for i in range(2, limite_jimenez):
        if numero_jimenez%i==0:
            primo_jimenez=False
            break
        
    # Mostrar en pantalla si el número es primo o no
    if primo_jimenez:
        print(f"{numero_jimenez} es un número primo.")
    else:
        print(f"{numero_jimenez} no es un número primo.")