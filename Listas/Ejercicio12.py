# Francisco Jiménez Álvarez
# Ejercicio 12
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’.
# Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
  # 111111111111111
  # 100000000000001
  # 100000000000001
  # 100000000000001
  # 111111111111111
# Visualiza el contenido de la matriz en pantalla.

# Crear la tabla
filas_jimenez = 5
columnas_jimenez = 15
marco_jimenez = [[0] * columnas_jimenez for i in range(filas_jimenez)]

# Inicializar la tabla con 0 y 1
for i in range(filas_jimenez):
    for j in range(columnas_jimenez):
        if i == 0 or i == filas_jimenez - 1 or j == 0 or j == columnas_jimenez - 1:
            marco_jimenez[i][j] = 1

# Mostrar la tabla en pantalla
for i in range(filas_jimenez):
    for j in range(columnas_jimenez):
        print(marco_jimenez[i][j], end='')
    print()
