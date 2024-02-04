# Francisco Jiménez Álvarez
# Ejercicio 4
# Crea un programa que pida al usuario dos números y muestre su división
# si el segundo no es cero, o un mensaje de aviso en caso contrario.

# Pedir al usuario que ingrese dos números
numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))

# Mostrar división (y error si el segundo es 0)
if numero2 != 0:
    print("Su división es: ", (numero1/numero2))
else:
    print("El segundo número tiene que ser distinto de 0. Reinicie el programa y vuelva a intentarlo")