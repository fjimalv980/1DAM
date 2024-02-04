# Francisco Jiménez Álvarez
# Ejercicio 15
# Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol. Para ello vamos a utilizar dos tablas:
# Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de los equipos de cada partido. En la quiniela se indican 15 partidos.
# Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna
# de la tabla anterior, y en la segunda los goles del otro equipo.
# El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
# ¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?

# Crear listas de equipos y resultados
equipos_jimenez = []
resultados_jimenez = []

# Pedir al usuario los nombres de los equipos y los resultados de cada partido
for i in range(15):
    equipo1_jimenez = input("Nombre del equipo local: ")
    equipo2_jimenez = input("Nombre del equipo visitante: ")
    goles1_jimenez = int(input("Goles del equipo local: "))
    goles2_jimenez = int(input("Goles del equipo visitante: "))
    equipos_jimenez.append([equipo1_jimenez, equipo2_jimenez])
    resultados_jimenez.append([goles1_jimenez, goles2_jimenez])

# Imprimimos la quiniela de la jornada
print("Quiniela de la jornada:")
for i in range(15):
    print(f"Partido {i+1}: {equipos_jimenez[i][0]} vs {equipos_jimenez[i][1]} - Resultado: {resultados_jimenez[i][0]}-{resultados_jimenez[i][1]}")

# Para guardar los resultados de todas las jornadas de la temporada en lugar de tener solo dos tablas, se necesitaría otra tabla para
# cada jornada de la temporada. Cada tabla adicional tendría las mismas dos columnas que la tabla de resultados original, pero con una
# fila para cada partido en esa jornada. La tabla de equipos seguiría siendo la misma, pero se necesitaría agregar una nueva columna
# para indicar la jornada a la que pertenece cada partido.