# Francisco Jiménez Álvarez
# Ejercicio 10
# Escribir dos funciones que permitan calcular:
# La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
# La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
# Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos o salir del programa.

from Funciones.FuncionesMatematicas import calcularSegundos, pasar_a_HMS

# Declarar opción
opcion = 0

# Bucle para elegir opciones
while opcion!=3:
    # Mostrar menú
    print("\nMENÚ: ")
    print("1. Calcular segundos en un tiempo dado en horas, minutos y segundos")
    print("2. Calcular horas, minutos y segundos de un total de segundos")
    print("3. Salir")

    # Pedir al usuario la opción que quiere
    opcion = int(input("\nElige tu opción: "))

    if opcion==1:
        horas_jimenez = int(input("Introduce las horas: "))
        minutos_jimenez = int(input("Introduce los minutos: "))
        segundos_jimenez = int(input("Introduce los segundos: "))
        print(calcularSegundos(horas_jimenez, minutos_jimenez, segundos_jimenez)," segundos.")

    elif opcion ==2:
        segundos_jimenez = int(input("Introduce los segundos: "))
        horas_jimenez, minutos_jimenez, segundos_jimenez = pasar_a_HMS(segundos_jimenez)
        print(horas_jimenez,":",minutos_jimenez,":",segundos_jimenez)

    elif opcion == 3:
        break

    else:
        print("La opción es incorrecta")