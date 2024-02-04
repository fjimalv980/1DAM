# Francisco Jiménez Álvarez
# Ejercicio 17
# Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena)
# de la cara opuesta al resultado obtenido.
# Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
# Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.

# Pedir al usuario que ingrese el número del dado
numero = int(input("Ingrese el número que ha salido en el dado: "))

# Obtener el número de la cara opuesta y mostrarlo en pantalla en letras
if (numero > 0) and (numero < 7):
    if numero == 1:
        print("El lado opuesto es: SEIS")
    elif numero == 2:
        print("El lado opuesto es: CINCO")
    elif numero == 3:
        print("El lado opuesto es: CUATRO")
    elif numero == 4:
        print("El lado opuesto es: TRES")
    elif numero == 5:
        print("El lado opuesto es: DOS")
    else:
        print("El lado opuesto es: UNO")
else:
    print("ERROR: número incorrecto.")