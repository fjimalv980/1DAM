# Francisco Jiménez Álvarez
# Ejercicio 2
# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido,a demás de los intentos que te quedan
# (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

import random

# Generar un número al azar
numAzar_jimenez = random.randint(1,100)

# Pedir al usuario que lo intente acertar. Decir si es cierto, menor o mayor a su número y decir los intentos restantes
print("Acierta mi número. Dime números del 1 al 100 y te diré si es correcto, menor o mayor que el tuyo. Tienes 10 intentos.")

numero_jimenez=int(input("Dime un número del 1 al 100: "))
intentos=1

while numero_jimenez!=numAzar_jimenez and intentos<10:
    intentos+=1
    if numero_jimenez<1 or numero_jimenez>100:
        print("Has perdido un intento por parguela, te he dicho del 1 al 100")
    else:
        if numero_jimenez<numAzar_jimenez:
            print("El número es mayor que el tuyo")
        elif numero_jimenez>numAzar_jimenez:
            print("El número es menor que el tuyo")
    numero_jimenez=int(input("Dime un número del 1 al 100: "))

if numero_jimenez==numAzar_jimenez:
    print("Felicidades has acertado el número")
    print(f"Has realizado {intentos} intentos")
else:
    print(f"Lo siento, has sobrepasado el límite de 10 intentos. El número era {numAzar_jimenez}")