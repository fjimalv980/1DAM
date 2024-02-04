# Francisco Jiménez Álvarez
# Ejercicio 9
# Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia.

# Pedir al usuario que ingrese un número real y luego su exponente
base_jimenez=float(input("Ingrese un número que será la base de una potencia: "))
exponente_jimenez=int(input("Ingrese ahora el exponente: "))

# Volver a pedir el exponente si no es positivo
while exponente_jimenez<1:
    exponente_jimenez=int(input("Ingrese un exponente positivo: "))

i=0
potencia=1
while i<exponente_jimenez:
    potencia=potencia*base_jimenez
    i+=1

# Mostrar la potencia en pantalla
print(f"La potencia es: {potencia}")