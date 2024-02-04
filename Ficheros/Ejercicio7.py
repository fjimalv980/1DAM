# Francisco Jiménez Álvarez
# Ejercicio 7
# El fichero cotizaciones.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada),
# Mínimo (precio mínimo de la acción durante la jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).
# Construir un programa que reciba el fichero de cotizaciones , devuelva un diccionario y lo imprima en la terminal con el mismo formato que el fichero. 
# A continuación se deberá crear una lista de diccionarios con el nombre de las columnas medibles, su máximo, su mínimo y su media aritmética. Esta lista se deberá guardar en un fichero llamado ejercicio7_primerapellido en formato csv.

import csv

# Leer el archivo cotizaciones.csv y crear diccionario
with open('cotizaciones.csv', newline='') as csvfile:
    lector_jimenez = csv.DictReader(csvfile)
    diccionario_jimenez = {}
    for row in lector_jimenez:
        diccionario_jimenez[row['Nombre']] = {'Final': row['Final'], 'Máximo': row['Máximo'], 'Mínimo': row['Mínimo'], 'Volumen': row['Volumen'], 'Efectivo': row['Efectivo']}

# Mostrar el diccionario
for clave, valor in diccionario_jimenez.items():
    print(clave, valor)

# Crear una lista de diccionarios con los datos pedidos
lista_jimenez = []
with open('cotizaciones.csv', newline='') as csvfile:
    lector_jimenez = csv.DictReader(csvfile)
    for columna_jimenez in lector_jimenez.fieldnames:
        diccionario_jimenez = {}
        diccionario_jimenez['Columna'] = columna_jimenez
        diccionario_jimenez['Máximo'] = max([float(row[columna_jimenez]) for row in lector_jimenez])
        csvfile.seek(0)
        diccionario_jimenez['Mínimo'] = min([float(row[columna_jimenez]) for row in lector_jimenez])
        csvfile.seek(0)
        diccionario_jimenez['Media'] = sum([float(row[columna_jimenez]) for row in lector_jimenez])/sum(1 for row in lector_jimenez)
        csvfile.seek(0)
        lista_jimenez.append(diccionario_jimenez)

# Crear archivo csv a partir de lista_jimenez
with open('ejercicio7_primerapellido.csv', 'w', newline='') as csvfile:
    escribir_jimenez = csv.DictWriter(csvfile, fieldnames=lista_jimenez[0].keys())
    escribir_jimenez.writeheader()
    for row in lista_jimenez:
        escribir_jimenez.writerow(row)
