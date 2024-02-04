# Francisco Jiménez Álvarez
# Ejercicio 13
# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

# Pedir al usuario una fecha (día, mes y año)
dia = int(input("Ingrese el día de la fecha: "))
mes = int(input("Ingrese el mes de la fecha: "))
año = int(input("Ingrese el año de la fecha: "))

# Comprobar si la fecha es correcta e imprimir sí o no
if (dia < 32) and (dia > 0) and (mes < 13) and (mes > 0):
    if ((dia < 31) and ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11))) or ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)):
        print("La fecha es correcta")
    elif ((dia == 29) and (mes == 2) and (año % 4 == 0) and ((año % 100 != 0) or (año % 400 == 0))) or (dia < 29):
        print("La fecha es correcta")
    else:
        print("La fecha no es correcta")
else:
    print("La fecha no es correcta")