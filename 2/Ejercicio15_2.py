# Francisco Jiménez Álvarez
# Ejercicio 15
# El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y
# cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más,
# el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos
# de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
# Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

# Pedir al usuario el número de alumnos que van al viaje
alumnos = int(input("Ingrese el número de alumnos que van al viaje: "))

# Calcular precio que debe pagar cada alumno y mostrarlo en pantalla
if alumnos > 0:
    if alumnos >= 100:
        print("El costo de cada alumno es 65€ y el total a pagar a la compañía es",alumnos*65,"€")
    elif (alumnos >=50) and (alumnos <100):
        print("El costo de cada alumno es 70€ y el total a pagar a la compañía es",alumnos*70,"€")
    elif (alumnos >=30) and (alumnos < 50):
        print("El costo de cada alumno es 95€ y el total a pagar a la compañía es",alumnos*95,"€")
    else:
        print("El costo de cada alumno es",4000/alumnos,"€ y el total a pagar a la compañía es 4000€")
else:
    print("Con esa cantidad de alumnos no hay viaje que valga")