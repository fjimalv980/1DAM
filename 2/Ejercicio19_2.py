# Francisco Jiménez Álvarez
# Ejercicio 19
# Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.

#  Pedir al usuario un mes del año en formato número, dependiendo del mes que sea en el año
mes = int(input("Ingrese el número del mes del año que quieras, siendo el 1 'Enero' y 12 'Diciembre': "))

# Escribir en pantalla el día de la semana en letras
if (mes < 13) and (mes > 0):
    if (mes == 2):
        print("El mes tiene 28 días y en año bisiesto 29")
    elif (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
        print("El mes tiene 30 días")
    else:
        print("El mes tiene 31 días")
else:
    print("El número es incorrecto. No pertenece a ningún mes del año")