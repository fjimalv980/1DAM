# Francisco Jiménez Álvarez
# Ejercicio 3
# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero primerapellido-n.txt
# con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el
# fichero no existe debe mostrar un mensaje por pantalla informando de ello.

# Pedir 2 números al usuario entre 1 y 10
n_jimenez = int(input("Introduce un número entre 1 y 10: "))
m_jimenez = int(input("Introduce otro: "))

# Comprobar si los números están entre 1 y 10
if n_jimenez < 1 or n_jimenez > 10 or m_jimenez < 1 or m_jimenez > 10:
    print("Los dos números deben estar entre 1 y 10")
else:
    # Crear variable para buscar el fichero
    nombre_jimenez="jimenez"+str(n_jimenez)+".txt"

    # Buscar y leer el fichero de la tabla n y mostrar la línea m
    try:
        with open(nombre_jimenez,"r") as fichero_jimenez:
            linea_jimenez = fichero_jimenez.readlines()
            print(linea_jimenez[m_jimenez-1])

    # Mensaje de error si no existe lo anterior
    except FileNotFoundError:
        print("El fichero no existe")