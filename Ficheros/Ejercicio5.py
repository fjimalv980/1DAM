# Francisco Jiménez Álvarez
# Ejercicio 5
# Realice un programa que reciba de nuevo el fichero calificaciones.csv para añadir a cada lista de cada alumno un nuevo elemento, será la Nota Final del curso.
# El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%. Si el alumno ha realizado alguna recuperación ordinaria,
# para el cálculo de la nota final se tomará esta como última nota del alumno. Se deberá mostrar finalmente en la terminal la lista ordenada y será guardada en un fichero que se llamará calificacionfinal.csv

import csv

# Abrir el archivo calificaciones.csv cargar contenido en una lista de listas
with open('calificaciones.csv', 'r') as f:
    reader_jimenez = csv.reader(f)
    datos_jimenez = [row for row in reader_jimenez]

# Calcular la nota final de cada alumno
for i in range(1, len(datos_jimenez)):
    parcial1_jimenez = float(datos_jimenez[i][3])
    parcial2_jimenez = float(datos_jimenez[i][4])
    practicas_jimenez = float(datos_jimenez[i][7])
    ordinarioPracticas_jimenez = float(datos_jimenez[i][8]) if datos_jimenez[i][8] else None
    notaFinal_jimenez = 0.3 * (parcial1_jimenez + parcial2_jimenez) + 0.4 * practicas_jimenez
    if ordinarioPracticas_jimenez is not None:
        notaFinal_jimenez = ordinarioPracticas_jimenez
    datos_jimenez[i].append(notaFinal_jimenez)

# Ordenar la lista de alumnos dependiendo de la nota final
datos_jimenez = sorted(datos_jimenez[1:], key=lambda x: float(x[-1]), reverse=True)
datos_jimenez.insert(0, ['Apellidos', 'Nombre', 'Asistencia', 'Parcial1', 'Parcial2', 'Ordinario1', 'Ordinario2', 'Practicas', 'OrdinarioPracticas', 'Nota Final'])

# Guardar la lista ordenada en un archivo llamado calificacionfinal.csv
with open('calificacionfinal.csv', 'w', newline='') as f:
    writer_jimenez = csv.writer(f)
    writer_jimenez.writerows(datos_jimenez)

# Mostrar lsita ordenada
for row in datos_jimenez:
    print(row)
