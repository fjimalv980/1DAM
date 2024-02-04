# Francisco Jiménez Álvarez
# Ejercicio 18
# Escriba un programa que permita crear una lista de palabras y que, a continuación de tres opciones:
# Contar: Me pide una cadena, y me dice cuantas veces aparece en la lista
# Modificar: Me pide una cadena, y otra cadena a modificar, y modifica todas alas apariciones de la primera por la segunda en la lista.
# Eliminar: Me pide una cadena, y la elimina de la lista.
# Mostrar: Muestra la lista de cadenas
# Terminar 

# Crear lista
lista_jimenez = []

# Pedir al usuario cadenas hasta que ingrese '*'
cadena_jimenez = input("Ingrese una cadena. Para terminar de ingresar cadenas ingresa un '*': ")
while cadena_jimenez != "*":
    # Añadir cadena a la lista
    lista_jimenez.append(cadena_jimenez)
    cadena_jimenez = input("Ingrese una cadena. Para terminar de ingresar cadenas ingresa un '*': ")

# Mostrar menú
while True:
    print("MENÚ:")
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Mostrar")
    print("5. Salir")

    # Pedir al usuario la opción
    opcion_jimenez = int(input("Dime tu opción:"))

    # Dependiendo de la opción elegida hacemos un if
    if opcion_jimenez == 1:
        # Pedir al usuario una cadena para buscarla
        cadena_jimenez = input("Introduce una cadena para buscarla: ")
        # Contar las apariciones de la cadena en la lista
        print(f"La cadena aparece {lista_jimenez.count(cadena_jimenez)} veces")

    elif opcion_jimenez == 2:
        # Pedir la cadena antigua y la nueva al usuario
        cadena_jimenez = input("Introduce una cadena para buscarla: ")
        cadena2_jimenez = input("Introduce una cadena para modificarla: ")
        # Modificar todas las apariciones de la cadena en la lista
        indice_jimenez = 0

        for i in lista_jimenez:
            if i == cadena_jimenez:
                lista_jimenez[indice_jimenez] = cadena2_jimenez
            indice_jimenez += 1

    elif opcion_jimenez == 3:
        # Pedir la cadena al usuario
        cadena_jimenez = input("Introduce una cadena para eliminarla: ")
        # Verificar si la cadena está en la lista
        if cadena_jimenez in lista_jimenez:
            # Eliminar todas las apariciones de la cadena en la lista
            while cadena_jimenez in lista_jimenez:
                lista_jimenez.remove(cadena_jimenez)
        else:
            print("Esta cadena no está en la lista.")

    elif opcion_jimenez == 4:
        # Mostrar todas las cadenas de la lista
        for i in lista_jimenez:
            print(i," ",end="")

    elif opcion_jimenez == 5:
        # Salir del programa
        break

    else:
        # Mostrar opción incorrecta
        print("Opción incorrecta")