# Francisco Jiménez Álvarez
# Ejercicio 1
# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre primer apellido-n.txt la tabla de multiplicar de ese número, done n es el número introducido.

# Pedir número al usuario
numero_jimenez = int(input("Ingrese un número del 1 al 10: "))

# Comprobar si está entre 1 y 10
if numero_jimenez < 1 or numero_jimenez > 10:
    print("El número debe estar entre 1 y 10")
else:
    # Crear archivo y escribirlo con la tabla de multiplicar del número dado
    nombreArchivo_jimenez = "jimenez" + str(numero_jimenez) + ".txt"
    with open(nombreArchivo_jimenez, 'w') as fichero_jimenez:
        for i in range(1, 11):
            resultado_jimenez = numero_jimenez * i
            fichero_jimenez.write(f"{numero_jimenez} x {i} = {resultado_jimenez}\n")

    # Mostrar que ha sido creado el fichero
    print(f"La tabla de multiplicar del número {numero_jimenez} ha sido guardada en el archivo {nombreArchivo_jimenez}")