# Francisco Jiménez Álvarez
# Ejercicio 11
# Escribe un programa en python que lea el fichero gazpacho.json con datos su origen e ingredientes, a continuación deberá  crear otro fichero primerapellido_ingredientes.json con los todos los datos de sus ingredientes.

import json

# Abrir el archivo gazpacho.json
with open('gazpacho.json', 'r') as f:
    # Cargar el contenido del archivo en una variable
    datos_jimenez = json.load(f)

# Acceder a los datos e ingredientes
origen_jimenez = datos_jimenez['origen']
ingredientes_jimenez = datos_jimenez['ingredientes']

# Crear un diccionario con los datos de los ingredientes
diccionarioIngredientes_jimenez = {}
for ingrediente_jimenez in ingredientes_jimenez:
    diccionarioIngredientes_jimenez[ingrediente_jimenez['nombre']] = ingrediente_jimenez['cantidad']

# Crear un nuevo archivo JSON con los datos de los ingredientes
with open('jimenez_ingredientes.json', 'w') as f:
    json.dump(diccionarioIngredientes_jimenez, f)