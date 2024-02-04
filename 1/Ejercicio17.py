# Francisco Jiménez Álvarez
# Ejercicio 17
# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

# Pedir al usuario la hora de partida y el tiempo de viaje en segundos
HH = int(input("Ingrese las horas de partida: "))
MM = int(input("Ingrese los minutos de partida: "))
SS = int(input("Ingrese los segundos de partida: "))
T = int(input("Ingrese el tiempo de viaje en segundos: "))

# Calcular la hora de llegada
tiempoPartidaSegundos = HH * 3600 + MM * 60 + SS  # Convertir la hora de partida a segundos
tiempoLlegadaSegundos = tiempoPartidaSegundos + T  # Sumar el tiempo de viaje en segundos

# Calcular las nuevas horas, minutos y segundos
HHLlegada = tiempoLlegadaSegundos // 3600
MMLlegada = (tiempoLlegadaSegundos % 3600) // 60
SSLlegada = tiempoLlegadaSegundos % 60

# Imprimir la hora de llegada
print("La hora de llegada a la ciudad B es: {:02d}:{:02d}:{:02d}".format(HHLlegada, MMLlegada, SSLlegada))