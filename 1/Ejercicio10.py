# Francisco Jiménez Álvarez
# Ejercicio 10
# Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.

# Pedir al usuario que ingrese las calificaciones parciales
parcial1 = float(input("Ingrese la calificación del primer parcial: "))
parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
parcial3 = float(input("Ingrese la calificación del tercer parcial: "))

# Pedir al usuario que ingrese la calificación del examen final y del trabajo final
examenFinal = float(input("Ingrese la calificación del examen final: "))
trabajoFinal = float(input("Ingrese la calificación del trabajo final: "))

# Calcular el promedio de las calificaciones parciales
promedioParciales = (parcial1 + parcial2 + parcial3) / 3

# Calcular la calificación final según la fórmula dada
calificacionFinal = 0.55 * promedioParciales + 0.30 * examenFinal + 0.15 * trabajoFinal

# Mostrar la calificación final
print("La calificación final del alumno en la materia de Algoritmos es: ", calificacionFinal)