# Francisco Jiménez Álvarez
# Ejercicio 17
# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. Para esto, se registran los días que trabajó y las horas de cada día.
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la empresa por los N empleados.

# Pedir sueldo por hora de los trabajadores
sueldo_jimenez=float(input("Dime los euros por hora que cobran tus trabajadores: "))

# Pedir cuantos trabajadores quiero calcular
trabajadores_jimenez=int(input("Dime de cuántos trabajadores quieres que calcule su sueldo: "))

# Pedir y mostrar horas trabajadas por cada empleado
i=0
j=0
totalHoras_jimenez=0
gastoTotal_jimenez=0

while i<trabajadores_jimenez:
    i+=1
    dias_jimenez=int(input(f"¿Cuántos días trabajó el trabajador {i}?: "))
    while j<dias_jimenez:
        j+=1
        horas_jimenez=float(input(f"Las horas de trabajo del trabajador {i} el día {j} son: "))
        totalHoras_jimenez=totalHoras_jimenez+horas_jimenez
    j=0
    print(f"El total de horas de trabajo del trabajador {i} son: {totalHoras_jimenez}")
    print(f"Su sueldo en la semana es: {totalHoras_jimenez*sueldo_jimenez}€")
    gastoTotal_jimenez=(totalHoras_jimenez*sueldo_jimenez)+gastoTotal_jimenez
    totalHoras_jimenez=0


# Mostrar el gasto total en empleados de la empresa en la semana
print(f"El gasto semanal de la empresa en trabajadores es: {gastoTotal_jimenez}€")