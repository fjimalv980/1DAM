# Francisco Jiménez Álvarez
# Ejercicio 15
# Escribe un programa en python que lea el fichero json libreria.json con datos de nuestra librería, recibe por teclado un límite inferior y superior para el precio y muestre en la terminal todos los libros cuyo precio esta en ese intervalo.

import json

# Abrir el archivo libreria.json
with open('libreria.json', 'r') as f:
    # Cargar el contenido del archivo en una variable
    datos_jimenez = json.load(f)

# Pedir al usuario los límites inferior y superior del precio
inferior_jimenez = float(input("Ingresa el límite inferior del precio: "))
superior_jimenez = float(input("Ingresa el límite superior del precio: "))

# Recorrer el archivo
for libro_jimenez in datos_jimenez['bookstore']['book']:
    # Guardar el precio del libro
    precio = float(libro_jimenez['price'])

    # Comprobar si el precio del libro está entre los límites
    if inferior_jimenez <= precio <= superior_jimenez:
        # Mostrar el título del libro
        print(f"{libro_jimenez['title']['__text']} | {libro_jimenez['author']} - {precio}")