# Francisco Jiménez Álvarez
# Ejercicio 10
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# Carga la tabla con valores numéricos enteros.
# Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

import random

# Crear una tabla de 5x5 e inicializarla con números aleatorios del 0 al 9
tabla_jimenez = [[random.randint(0, 9) for k in range(5)] for k in range(5)]

# Mostrar la tabla
print("Tabla:")
for fila_jimenez in tabla_jimenez:
    for i in fila_jimenez:
        print(i, end='  ')
    print()

# Calcular y mostrar la suma de cada fila
for i, fila_jimenez in enumerate(tabla_jimenez):
    sumaFila_jimenez = sum(fila_jimenez)
    print(f"Suma de la fila {i + 1}: {sumaFila_jimenez}")

# Calcular y mostrar la suma de elementos de cada columna
numeroFilas_jimenez = len(tabla_jimenez)
numeroColumnas_jimenez = len(tabla_jimenez[0])

for j in range(numeroColumnas_jimenez):
    sumaColumna_jimenez = sum(tabla_jimenez[i][j] for i in range(numeroFilas_jimenez))
    print(f"Suma de la columna {j + 1}: {sumaColumna_jimenez}")
