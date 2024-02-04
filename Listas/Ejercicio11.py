# Francisco Jiménez Álvarez
# Ejercicio 11
# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
# Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
# Muestra el contenido de la tabla en pantalla.

# Crear tabla diagonal
diagonal_jimenez = []

# Mostrar la tabla inicializando los valores en listas por filas
print("Diagonal:")
for i in range(0,5):
    fila_jimenez=[]
    for j in range(0,5):
        # Inicializar 1 si está en diagonal
        if i == j or i == (4-j):
            fila_jimenez.append(1)
        # Inicializar 0 si no está en diagonal
        else:
            fila_jimenez.append(0)
    diagonal_jimenez.append(fila_jimenez)

# Mostrar tabla
for fila_jimenez in diagonal_jimenez:
    for i in fila_jimenez:
        print(i," ",end="")
    print()