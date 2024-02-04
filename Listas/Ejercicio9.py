# Francisco Jiménez Álvarez
# Ejercicio 9
# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
# La temperatura media de cada día
# Los días con menos temperatura
# Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella.
# Si no existe ningún día se muestra un mensaje de información.

# Crear lista para las temperaturas mínimas y máximas de cada día
temperaturas_jimenez = []

# Pedir al usuario las temperaturas
for i in range(5):
    minima_jimenez = float(input(f"Ingrese la temperatura mínima del día {i + 1}: "))
    maxima_jimenez = float(input(f"Ingrese la temperatura máxima del día {i + 1}: "))
    temperaturas_jimenez.append((minima_jimenez, maxima_jimenez))

# Calcular y mostrar la temperatura media de cada día
print("Temperatura media de cada día:")

for i, (minima_jimenez, maxima_jimenez) in enumerate(temperaturas_jimenez):
    media_jimenez = (minima_jimenez + maxima_jimenez) / 2
    print(f"Día {i + 1}: {media_jimenez}")

# Encontrar la temperatura mínima
listaMinima_jimenez = min(temperaturas_jimenez)[0]
diasMinima_jimenez = [i + 1 for i, (minima_jimenez, maxima_jimenez) in enumerate(temperaturas_jimenez) if minima_jimenez == listaMinima_jimenez]

# Mostrar días con temperatura mínima
print("Días o día con menos temperatura:", diasMinima_jimenez)

# Pedir al usuario una temperatura y buscar los días en los cuales esa temperatura es la máxima
buscarMaxima_jimenez = float(input("Ingrese una temperatura para buscar los días con esa temperatura máxima: "))
diasMaxima_jimenez = [i + 1 for i, (minima_jimenez, maxima_jimenez) in enumerate(temperaturas_jimenez) if maxima_jimenez == buscarMaxima_jimenez]

if diasMaxima_jimenez:
    print(f"Los días o el día con esa temperatura máxima son: {diasMaxima_jimenez}")
else:
    print("Ningún día tiene esa temperatura máxima.")