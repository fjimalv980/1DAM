# Francisco Jiménez Álvarez
# Ejercicio 2
# Escribir una función que pida un número entero entre 1 y 10, lea el fichero primerapellido-n.txt con la tabla de multiplicar de ese número,
# done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.

# Pedir número al usuario
numero_jimenez = int(input("Ingrese un número del 1 al 10: "))

# Comprobar si está entre 1 y 10
if numero_jimenez < 1 or numero_jimenez > 10:
    print("El número debe estar entre 1 y 10")
else:
    # Comprobar si la lista de ese número existe, mostrarla y si no mostrar el error
    nombreArchivo_jimenez = "jimenez" + str(numero_jimenez) + ".txt"
    try: 
        f = open(nombreArchivo_jimenez, 'r')
    except FileNotFoundError:
        print('No existe el fichero con la tabla del', numero_jimenez)
    else:
        print(f.read())
    f.close()