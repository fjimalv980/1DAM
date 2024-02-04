# Francisco Jiménez Álvarez
# Ejercicio 6
# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

# Pedir dos números al usuario
numero1_jimenez=int(input("Ingrese un número: "))
numero2_jimenez=int(input("Ingrese otro número: "))

# Mostrar todos los números pares entre los dos números introducidos por el usuario
if numero1_jimenez>numero2_jimenez:
    numero1_jimenez, numero2_jimenez = numero2_jimenez, numero1_jimenez

print(f"Números pares entre {numero1_jimenez} y {numero2_jimenez}:")
for numero1_jimenez in range(numero1_jimenez+1, numero2_jimenez, + 1):
    if numero1_jimenez % 2 == 0:
        print(numero1_jimenez)