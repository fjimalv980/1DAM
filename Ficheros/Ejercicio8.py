# Francisco Jiménez Álvarez
# Ejercicio 8
# Escribe un programa en python que lea el fichero json colores.json con datos de colores, deberá mostrar en la terminal todos los nombres de colores, sus códigos rgba y hexadecimal respectivamente.

import json

# Abrir colores.json
with open('colores.json', 'r') as f:
    datos_jimenez = json.load(f)

# Recorrer colores.json y guardar datos en variables
for colorInfo_jimenez in datos_jimenez['colors']:
    color_jimenez = colorInfo_jimenez['color']
    rgbaCodigo_jimenez = colorInfo_jimenez['code']['rgba']
    hexCodigo_jimenez = colorInfo_jimenez['code']['hex']

    # Imprimir resultado
    print(f'Color: {color_jimenez}, Código RGBA: {rgbaCodigo_jimenez}, Código Hexadecimal: {hexCodigo_jimenez}')
