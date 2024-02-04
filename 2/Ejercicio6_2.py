# Francisco Jiménez Álvarez
# Ejercicio 6
# Programa que lea una cadena por teclado y compruebe si la primera letra es una letra mayúscula.

# Pedir al usuario que ingrese una cadena
cadena = input("Ingresa una cadena: ")

# Comprobar si la primera letra es mayúscula
if (cadena[0].isupper()):
    print("La primera letra es mayúscula")
else:
    print("La primera letra es minúscula")