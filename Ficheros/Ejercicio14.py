# Francisco Jiménez Álvarez
# Ejercicio 14
# Escribe un programa en python que lea el fichero json libreria.json con datos de nuestra librería y muestre en la terminal cuántos libros hay en la librería.

import json

# Abrir el archivo libreria.json
with open('libreria.json', 'r') as f:
    # Cargar el contenido del archivo en una variable
    datos_jimenez = json.load(f)

# Acceder a la lista de libros de la librería y contar los libros
numeroLibros_jimenez = len(datos_jimenez['bookstore']['book'])

# Mostrar la cantidad de libros
print(f"La librería tiene {numeroLibros_jimenez} libros.")