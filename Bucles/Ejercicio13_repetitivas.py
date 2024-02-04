# Francisco Jiménez Álvarez
# Ejercicio 13
# Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y
# requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas.

# Pedir al usuario las horas trabajadas cada día de los 6 trabajados y calcular el total de horas trabajadas en la semana
print("Introduce día por día las horas trabajadas cada uno de los 6 días")
i=0
totalHoras_jimenez=0
while i<7:
    i+=1
    horas_jimenez=float(input(f"Las horas trabajadas el día {i} fueron: "))
    totalHoras_jimenez=totalHoras_jimenez+horas_jimenez

# Pedir el sueldo por hora
sueldo_jimenez=float(input("La cantidad de euros que cobras por hora son: "))

# Mostrar el total ganado en la semana
print(f"El total ganado en la semana es {totalHoras_jimenez*sueldo_jimenez}€")