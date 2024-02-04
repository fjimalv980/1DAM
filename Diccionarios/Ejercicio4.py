# Francisco Jiménez Álvarez
# Ejercicio 4
# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido.
# Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres
# de los alumnos y los valores serán listas con las notas de cada alumno.
# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos
# un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
# Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

# Crear diccionario de los alumnos y sus notas
alumnosNotas_jimenez = {}

# Pedir al usuario el número de alumnos
numeroAlumnos_jimenez = int(input("Introduce el número de alumnos: "))

# Bucle para agregar alumnos a la lista
for alumno_jimenez in range(numeroAlumnos_jimenez):
    nombre_jimenez = input("Introduce el nombre del alumno: ")
    
    # Comprobar si el alumno ya está en el diccionario
    if nombre_jimenez in alumnosNotas_jimenez:
        print("¡Error! Ese alumno ya está incluido.")
    
    notas_jimenez = []

    # Bucle para introducir notas del alumno
    while True:
        nota_jimenez = float(input(f"Introduce una nota del alumno {nombre_jimenez} (número negativo para terminar): "))
        if nota_jimenez < 0:
            break
        notas_jimenez.append(nota_jimenez)
    
    # Agregar nombre y notas del alumno al diccionario
    alumnosNotas_jimenez[nombre_jimenez] = notas_jimenez

# Mostrar la lista de alumnos con sus notas y la nota media de cada uno
for alumno_jimenez, notas_jimenez in alumnosNotas_jimenez.items():
    notaMedia_jimenez = sum(notas_jimenez) / len(notas_jimenez)
    print(f"Alumno: {alumno_jimenez}\tNotas: {notas_jimenez}\tNota Media: {notaMedia_jimenez}")