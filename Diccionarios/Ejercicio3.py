# Francisco Jiménez Álvarez
# Ejercicio 3
# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas.
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir
# de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa
# nos preguntará si queremos hacer otra consulta.

# Crear el diccionario con las frutas y sus precios
precios_jimenez = {
    "platano": 2,
    "manzana": 2.5,
    "naranja": 1.5,
    "pera": 3,
    "melon": 5
}

# Crear bucle para pedir consultas
while True:
    # Pedir al usuario la fruta y la cantidad vendida
    fruta_jimenez = input("Ingrese el nombre de la fruta ('*' para terminar): ").lower()
    
    # Comprobamos si el usuario quiere terminar el programa
    if fruta_jimenez == "*":
        print("¡Muchas gracias por su visita!")
        break

    if fruta_jimenez in precios_jimenez:
        cantidad_jimenez = int(input("Ingrese la cantidad vendida: "))
        precioTotal_jimenez = precios_jimenez[fruta_jimenez] * cantidad_jimenez
        print(f"El precio total de {cantidad_jimenez} {fruta_jimenez}s es: {precioTotal_jimenez} euros")
    else:
        print("¡Error! Esa fruta no está en la lista de precios.")

    # Preguntamos al usuario si quiere hacer otra consulta
    preguntar_jimenez = input("¿Quieres hacer otra consulta? (s/n): ")
    if preguntar_jimenez.lower() != "s":
        print("¡Muchas gracias por su visita!")
        break