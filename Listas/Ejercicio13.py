# Francisco Jiménez Álvarez
# Ejercicio 13
# De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arreglos:
# Nombre: Lista para guardar los nombres de los conductores.
# kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor.
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha realizado.

# Pedir al usuario cuantos conductore tiene la empresa
cantidad_jimenez = int(input("¿Cuántos empleados tiene la empresa?: "))

# Pedir al usuario ingresar los nombres de los conductores
nombres_jimenez = []
for i in range(cantidad_jimenez):
    nombre_jimenez = input(f"Ingrese el nombre del conductor {i + 1}: ")
    nombres_jimenez.append(nombre_jimenez)

# Pedir al usuario los kilómetros para cada conductor y día de la semana
kms_jimenez = []
for i in range(len(nombres_jimenez)):
    kmsConductor_jimenez = []
    for dia_jimenez in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]:
        kmsDia_jimenez = int(input(f"Ingrese los kilómetros para {nombres_jimenez[i]} el {dia_jimenez}: "))
        kmsConductor_jimenez.append(kmsDia_jimenez)
    kms_jimenez.append(kmsConductor_jimenez)

# Lista para almacenar los kilómetros totales de cada conductor
totalKms_jimenez = []

# Calcular los kilómetros totales para cada conductor y agregarlos a la lista
for i in range(len(nombres_jimenez)):
    kmsTotales_jimenez = sum(kms_jimenez[i])
    totalKms_jimenez.append((nombres_jimenez[i], kmsTotales_jimenez))

# Mostrar la lista con los nombres de conductores y los kilómetros totales
for nombre_jimenez, kmsTotales_jimenez in totalKms_jimenez:
    print(f"{nombre_jimenez}: {kmsTotales_jimenez} kilómetros")
