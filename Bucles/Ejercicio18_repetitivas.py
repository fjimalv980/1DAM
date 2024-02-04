# Francisco Jiménez Álvarez
# Ejercicio 18
# Hacer un programa que muestre un cronometro, indicando las horas, minutos y segundos.

# Bucles de las horas, minutos y segundos
minutos_jimenez=0
horas_jimenez=0
for segundos_jimenez in range(0,61):
    print(f"{horas_jimenez}:{minutos_jimenez}:{segundos_jimenez}")
    segundos_jimenez+=1
    if segundos_jimenez==60:
        minutos_jimenez+=1
        segundos_jimenez=0

    if minutos_jimenez==60:
        minutos_jimenez=0
        horas_jimenez=1

    if horas_jimenez==60:
        horas_jimenez=0