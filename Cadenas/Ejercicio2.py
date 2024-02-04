# Francisco Jiménez Álvarez
# Ejercicio 2
# Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.

# Pedir al usuario dos cadenas
cadena_jimenez = input("Escribe una cadena: ")
subcadena_jimenez = input("Escribe otra cadena: ")

# Comprobar y mostrar si las cadenas empiezan por la misma letra
if cadena_jimenez[0] == subcadena_jimenez[0]:
    print("Las cadenas empiezan por la misma letra")
else:
    print("Las cadenas NO empiezan por la misma letra")