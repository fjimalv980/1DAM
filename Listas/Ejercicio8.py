# Francisco Jiménez Álvarez
# Ejercicio 8
# Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno.
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
# Todos lo alumnos mayores de edad.
# Los alumnos mayores (los que tienen más edad)

# Crear lista vacía para los alumnos
alumnos_jimenez = []
edades_jimenez = []

# Pedir al usuario nombres y edades y obligar que estén entre 1 y 100 años
print("Ingrese el nombre y la edad de cada alumno (Para terminar de introducir alumnos escribe '*'):")
while True:
    nombre_jimenez = input("Nombre: ")
    if nombre_jimenez == "*":
        break
    edad_jimenez = int(input("Edad: "))
    if edad_jimenez > 0 and edad_jimenez < 101:
        alumnos_jimenez.append(nombre_jimenez)
        edades_jimenez.append(edad_jimenez)
    else:
        print("Has introducido una edad incorrecta. Vuelve a introducir el alumno y su edad:")

# Mostrar todos los alumnos mayores de edad
print("Alumnos mayores de edad: ")
for i in range(len(edades_jimenez)):
    if edades_jimenez[i] >= 18:
        print(f"Nombre: {alumnos_jimenez[i]}  {edades_jimenez[i]} años")

# Buscar los alumnos mayores y guardarlos en una lista
mayor_jimenez = max(edades_jimenez)
mayores_jimenez = [alumnos_jimenez[i] for i in range(len(alumnos_jimenez)) if edades_jimenez[i] == mayor_jimenez]

# Mostrar los alumnos mayores
print("Alumnos mayores: ")
for i in mayores_jimenez:
    print(i)