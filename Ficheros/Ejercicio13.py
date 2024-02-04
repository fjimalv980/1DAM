# Francisco Jiménez Álvarez
# Ejercicio 13
# Escribe un programa en python que lea el fichero *movies.json con datos de películas. A continuación deberá crear un fichero primerapellido_peliculasaventuras.json con los títulos de las películas cuyo género incluya aventura.
# *hay algunos títulos de películas que vienen con una mala codificación, no afectará a la resolución del ejercicio.

import json

# Abrir el archivo movies.json
with open('movies.json', 'r') as f:
    # Cargar el contenido del archivo en una variable
    datos_jimenez = json.load(f)

# Crear una lista vacía de los títulos de las películas de aventura
peliculasAventura_jimenez = []

# Bucle para comprobar y agragar películas de aventura a la lista
for pelicula_jimenez in datos_jimenez:

    if 'Adventure' in pelicula_jimenez['genres']:
        peliculasAventura_jimenez.append(pelicula_jimenez['title'])

# Crear un nuevo archivo JSON con las películas de aventura
with open('jimenez_peliculasaventuras.json', 'w') as f:
    json.dump(peliculasAventura_jimenez, f)