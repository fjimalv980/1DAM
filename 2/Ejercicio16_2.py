# Francisco Jiménez Álvarez
# Ejercicio 16
# La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura,
# de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos,
# 70 céntimos, y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día,
# en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto
# una persona que realiza una llamada.

# Pedir al usuario el día y el tiempo de llamada
tiempo = int(input("Ingrese cuantos minutos duró la llamada: "))
domingo = str(input("¿La llamada es en domingo? Responde 's' para sí y 'n' para no: "))
if domingo == "n":
    turno = str(input("Ingrese el turno de la llamada (mañana o tarde): "))

# Calcular el precio de la llamada, sumando el impuesto
if tiempo > 0:
    if tiempo <= 5:
        coste = tiempo * 1
    elif (tiempo > 5) and (tiempo <= 8):
        coste = 5 + 0.8 * (tiempo - 5)
    elif (tiempo > 8) and (tiempo <=10):
        coste = 5 + 2.4 + 0.7 * (tiempo - 8)
    else:
        coste = 5 + 2.4 + 1.4 + 0.5 * (tiempo - 10)
else:
    print(input("Si quieres pagar por no hablar o hablar en negativo allá tú máquina"))
if domingo == 's':
    impuesto = coste * 0.03
elif turno == "mañana":
        impuesto = coste * 0.15
elif turno == "tarde":
        impuesto = coste * 0.1
else:
    print("Algún dato es incorrecto. ¿Sabes leer?")

# Mostrar en pantalla el precio de la llamada
if coste > 0:
    print(f"El precio de tu llamada es: {coste + impuesto}€")