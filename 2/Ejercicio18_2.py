# Francisco Jiménez Álvarez
# Ejercicio 18
# Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

#  Pedir al usuario un día de la semana en formato número, dependiendo del día que sea en la semana
dia = int(input("Ingrese el número del día de la semana que quieras, siendo el 1 'lunes' y 7 'domingo': "))

# Escribir en pantalla el día de la semana en letras
if (dia < 8) and (dia > 0):
    if dia == 1:
        print("El día de la semana es: LUNES")
    elif dia == 2:
        print("El día de la semana es: MARTES")
    elif dia == 3:
        print("El día de la semana es: MIÉRCOLES")
    elif dia == 4:
        print("El día de la semana es: JUEVES")
    elif dia == 5:
        print("El día de la semana es: VIERNES")
    elif dia == 6:
        print("El día de la semana es: SÁBADO")
    else:
        print("El día de la semana es: DOMINGO")
else:
    print("El número es incorrecto. No pertenece a ningún día de la semana")