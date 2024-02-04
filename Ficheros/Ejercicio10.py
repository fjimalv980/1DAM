# Francisco Jiménez Álvarez
# Ejercicio 10
# Escribe un programa en python que lea el fichero json pedidos.json con datos de ordenes, a continuación deberá  crear otro fichero primerapellido_clientes.json con los todos los datos de los clientes.

import json

# Abrir pedidos.json
with open('pedidos.json', 'r') as f:
    datos_jimenez = json.load(f)

# Recopilar datos y guardarlos en una lista
clientes_jimenez = [orden_jimenez['cliente'] for orden_jimenez in datos_jimenez['ordenes']]

# Crear archivo primerapellido_clientes.json con la lista anterior
with open('jimenez_clientes.json', 'w') as f:
    json.dump(clientes_jimenez, f)
