# Francisco Jiménez Álvarez
# Ejercicio 12
# Escribe un programa en python que lea el fichero *movies.json con datos de películas. A continuación deberá crear un fichero primerapellido_pelicula1994.json con los títulos de las películas  que se hayan estrenado en 1994.
# *hay algunos títulos de películas que vienen con una mala codificación, no afectará a la resolución del ejercicio.

import json

# Abrir el archivo movies.json
with open('movies.json', 'r') as f:
    # Cargar el archivo en una variable
    datos_jimenez = json.load(f)

# Crear una lista vacía para los títulos estrenados en 1994
peliculas_1994_jimenez = []

#Bucle para comprobar y agragar peliculas a la lista
for pelicula_jimenez in datos_jimenez:
    # Si la película se estrenó en 1994, añadir su título a la lista
    if pelicula_jimenez['year'] == '1994':
        peliculas_1994_jimenez.append(pelicula_jimenez['title'])

# Crear un nuevo archivo JSON con los títulos de las películas estrenadas en 1994
with open('jimenez_pelicula1994.json', 'w') as f:
    json.dump(peliculas_1994_jimenez, f)