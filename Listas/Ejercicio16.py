# Francisco Jiménez Álvarez
# Ejercicio 16
# Vamos a crear un programa que tenga el siguiente menú:

# Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
# Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# Longitud de la lista: te muestra el número de elementos de la lista.
# Eliminar el último número: Muestra el último número de la lista y lo borra.
# Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
# Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
# Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
# Mostrar números: Muestra los números de la lista
# Salir
lista_jimenez = []
while True:
    # Mostrar opciones
    print("MENÚ:")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")

    # Pedir al usuario la opción
    opcion_jimenez = int(input("Elige una opción: "))
    # Dependiendo de la opción elegida ejecutamos un if o otro
    if opcion_jimenez == 1:
        # Pedir número al usuario
        numero_jimenez = int(input("Introduce un número: "))
        # Añadir el número a la lista
        lista_jimenez.append(numero_jimenez)
        # Mostrar mensaje de confirmación
        print(f"El número {numero_jimenez} ha sido añadido a la lista.")

    elif opcion_jimenez == 2:
        # Pedir el número y la posición al usuario
        numero_jimenez = int(input("Introduce un número: "))
        posicion_jimenez = int(input("Introduce una posición: "))
        # Verificar si la posición existe en la lista
        if posicion_jimenez > len(lista_jimenez):
            print("La posición no existe en la lista.")
        else:
            # Añadir el número a la lista en la posición indicada
            lista_jimenez.insert(posicion_jimenez - 1, numero_jimenez)
            # Mostrar un mensaje de confirmación
            print(f"El número {numero_jimenez} ha sido añadido a la lista en la posición {posicion_jimenez}.")

    elif opcion_jimenez == 3:
        # Mostrar la longitud de la lista
        print(f"La longitud de la lista es {len(lista_jimenez)}.")

    elif opcion_jimenez == 4:
        # Verificar si la lista está vacía
        if len(lista_jimenez) == 0:
            print("La lista está vacía.")
        else:
            # Eliminar el último número de la lista
            ultimoNumero_jimenez = lista_jimenez.pop()
            # Mostrar el número eliminado
            print(f"El número {ultimoNumero_jimenez} ha sido eliminado de la lista.")

    elif opcion_jimenez == 5:
        # Pedir la posición al usuario
        posicion_jimenez = int(input("Introduce una posición: "))
        # Verificar si la posición existe en la lista
        if posicion_jimenez > len(lista_jimenez):
            print("La posición no existe en la lista.")
        else:
            # Eliminar el número de la lista en la posición indicada
            numeroEliminado_jimenez = lista_jimenez.pop(posicion_jimenez - 1)
            # Mostrar un mensaje de confirmación
            print(f"El número {numeroEliminado_jimenez} ha sido eliminado de la lista.")

    elif opcion_jimenez == 6:
        # Pedir el número al usuario
        numero_jimenez = int(input("Introduce un número: "))
        # Contar las apariciones del número en la lista
        apariciones_jimenez = lista_jimenez.count(numero_jimenez)
        # Mostrar el resultado
        print(f"El número {numero_jimenez} aparece {apariciones_jimenez} veces en la lista.")

    elif opcion_jimenez == 7:
        # Pedir el número al usuario
        numero_jimenez = int(input("Introduce un número: "))
        # Buscar las posiciones del número en la lista
        posiciones_jimenez = [i + 1 for i, x in enumerate(lista_jimenez) if x == numero_jimenez]
        # Verificar si el número aparece en la lista
        if len(posiciones_jimenez) == 0:
            print(f"El número {numero_jimenez} no aparece en la lista.")
        else:
            # Mostrar las posiciones del número
            print(f"El número {numero_jimenez} aparece en las posiciones {posiciones_jimenez}.")

    elif opcion_jimenez == 8:
        # Mostrar los números de la lista
        print("Los números de la lista son:")
        for numero_jimenez in lista_jimenez:
            print(numero_jimenez)

    elif opcion_jimenez == 9:
        # Salir y mostrar mensaje de despedida
        print("¡Good bye my lover, good bye my friend!")
        break

    else:
        # Mostrar mensaje de error
        print("Opción inválida. Inténtalo de nuevo.")