# Francisco Jiménez Álvarez
# Ejercicio 19
# Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta
# correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

# Pedir al usuario el número de respuestas correctas, incorrectas y en blanco
respuestasCorrectas = int(input("Ingrese el número de respuestas correctas: "))
respuestasIncorrectas = int(input("Ingrese el número de respuestas incorrectas: "))
respuestasBlanco = int(input("Ingrese el número de respuestas en blanco: "))

# Calcular la nota final
notaFinal = respuestasCorrectas * 5 - respuestasIncorrectas

# Mostrar el resultado obtenido por el estudiante
print("La nota final del estudiante es:", notaFinal)