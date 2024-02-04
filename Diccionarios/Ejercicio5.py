# Francisco Jiménez Álvarez
# Ejercicio 5
# Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:
# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir
# modificarlo si no es correcto. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
# Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.

# Crear diccionario de la agenda
agenda_jimenez = {}

# Bucle del menú
while True:
    print("Menú:")
    print("1. Añadir/Modificar contacto")
    print("2. Buscar contacto")
    print("3. Borrar contacto")
    print("4. Listar contactos")
    print("5. Salir")

    # Pedir al usuario una opción
    opcion_jimenez = int(input("Elige una opción: "))

    # Switch de las opciones del menú
    if opcion_jimenez == 1:
        # Pedir nombre del contacto
        nombre_jimenez = input("Introduce el nombre: ")

        # Comprobar si el nombre está en la lista
        if nombre_jimenez in agenda_jimenez:
            # Mostrar el nombre y el número y preguntar si quiere modificar el teléfono
            print(f"El teléfono de {nombre_jimenez} es {agenda_jimenez[nombre_jimenez]}")
            modificar_jimenez = input("¿Quieres modificar el teléfono? (si/no): ")
            if modificar_jimenez.lower() == "si":
                telefono_jimenez = input("Introduce el nuevo teléfono: ")

                # Agregar el teléfono a la lista
                agenda_jimenez[nombre_jimenez] = telefono_jimenez

        # Pedir el teléfono si no existe el contacto en la lista
        else:
            telefono_jimenez = input("Introduce el teléfono: ")

            # Agregar el teléfono a la lista
            agenda_jimenez[nombre_jimenez] = telefono_jimenez

    elif opcion_jimenez == 2:
        # Pedir cadena para buscar contacto
        cadena_jimenez = input("Introduce una cadena para buscar el contacto: ")

        # Bucle para comprobar si hay un contacto que empiece por esa cadena, y si es así, mostrarlo
        for nombre_jimenez, telefono_jimenez in agenda_jimenez.items():
            if nombre_jimenez.startswith(cadena_jimenez):
                print(f"Nombre: {nombre_jimenez}\tTeléfono: {telefono_jimenez}")

    elif opcion_jimenez == 3:
        # Pedir nombre del contacto que quiere borrar
        nombre_jimenez = input("Introduce el contacto que quieres borrar: ")

        # Comprobar si está en la lista, si es así preguntar si quiere borrarlo
        if nombre_jimenez in agenda_jimenez:
            preguntar_jimenez = input("¿Quieres borrar este contacto? (si/no): ")

            # Borrar contacto
            if preguntar_jimenez.lower() == "si":
                del agenda_jimenez[nombre_jimenez]
                print(f"{nombre_jimenez} ha sido borrado de la agenda.")

        # Mostrar mensaje de que no se encuentra el contacto
        else:
            print(f"{nombre_jimenez} no se encuentra en la agenda.")

    elif opcion_jimenez == 4:
        # Mostrar todos los contactos de la agenda
        print("Contactos: ")
        for nombre_jimenez, telefono_jimenez in agenda_jimenez.items():
            print(f"Nombre: {nombre_jimenez}\tTeléfono: {telefono_jimenez}")

    elif opcion_jimenez == 5:
        # Salir del programa
        print("Has salido")
        break

    else:
        # Mostrar opción no válida
        print("Opción no válida. Inténtalo de nuevo.")