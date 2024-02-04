# Francisco Jiménez Álvarez
# Ejercicio 9
# Escribe un programa en python que lea el fichero json pedidos.json con datos de órdenes, deberá mostrar en la terminal todos las órdenes de pedidos que no se hayan entregado.

import json

# Abrir pedidos.json
with open('pedidos.json', 'r') as f:
    datos_jimenez = json.load(f)

# Bucle para buscar y mostrar los pedidos no entregados
for orden_jimenez in datos_jimenez['ordenes']:
    if not orden_jimenez['delivery']:
        print(f'Orden: {orden_jimenez}')