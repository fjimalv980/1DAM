# Francisco Jiménez Álvarez
# Ejercicio 16
# Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una
# velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas
# velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

# Pedir al usuario la distancia entre los vehículos en kilómetros
distancia = float(input("Ingrese la distancia entre los dos vehículos en km: "))

# Pedir al usuario las velocidades de los vehículos en km/h
v1 = float(input("Ingrese la velocidad del vehículo más lento en km/h: "))
v2 = float(input("Ingrese la velocidad del vehículo más rápido en km/h: "))

# Calcular en horas el tiempo que tarda el vehículo más lento en alcanzar al vehículo más rápido
tiempoHoras = distancia / (v2 - v1)

# Convertir el tiempo de horas a minutos
tiempoMinutos = tiempoHoras * 60

# Mostrar el tiempo en minutos
print("El vehículo más rápido alcanzará al otro en", tiempoMinutos, "minutos.")