# Francisco Jiménez Álvarez
# Ejercicio 14
# Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
# Las cantidades totales de cada articulo.
# La cantidad de artículos en la sucursal 2.
# La cantidad del articulo 3 en la sucursal 1.
# La recaudación total de cada sucursal.
# La recaudación total de la empresa.
# La sucursal de mayor recaudación.

# Inicializar listas para almacenar precios y cantidades por artículo y sucursal
precios_jimenez = []
cantidadesSucursal_jimenez = [[], [], [], []]

# Leer los precios de los 5 artículos
for i in range(5):
    precio_jimenez = float(input(f"Ingrese el precio del artículo {i + 1}: "))
    precios_jimenez.append(precio_jimenez)

# Leer las cantidades vendidas por cada sucursal y artículo
for sucursal_jimenez in range(4):
    for articulo_jimenez in range(5):
        cantidad_jimenez = int(input(f"Ingrese la cantidad vendida del artículo {articulo_jimenez + 1} en la sucursal {sucursal_jimenez + 1}: "))
        cantidadesSucursal_jimenez[sucursal_jimenez].append(cantidad_jimenez)

# Mostrar las cantidades totales de cada artículo
print("\nCantidades totales de cada artículo:")
for articulo_jimenez in range(5):
    cantidadTotal_jimenez = sum(cantidadesSucursal_jimenez[j][articulo_jimenez] for j in range(4))
    print(f"Artículo {articulo_jimenez + 1}: {cantidadTotal_jimenez} unidades")

# Mostrar la cantidad de artículos en la sucursal 2
cantidadSucursal2_jimenez = sum(cantidadesSucursal_jimenez[1])
print(f"\nCantidad de artículos en la sucursal 2: {cantidadSucursal2_jimenez} unidades")

# Mostrar la cantidad del artículo 3 en la sucursal 1
cantidadArticulo3Sucursal1_jimenez = cantidadesSucursal_jimenez[0][2]
print(f"\nCantidad del artículo 3 en la sucursal 1: {cantidadArticulo3Sucursal1_jimenez} unidades")

# Mostrar la recaudación total de cada sucursal
print("\nRecaudación total de cada sucursal:")
recaudacionSucursal_jimenez = [sum(precios_jimenez[i] * cantidadesSucursal_jimenez[j][i] for i in range(5)) for j in range(4)]
for j in range(4):
    print(f"Sucursal {j + 1}: ${recaudacionSucursal_jimenez[j]:.2f}")

# Informar la recaudación total de la empresa
recaudacionEmpresa_jimenez = sum(recaudacionSucursal_jimenez)
print(f"\nRecaudación total de la empresa: ${recaudacionEmpresa_jimenez:.2f}")

# Determinar la sucursal de mayor recaudación
sucursalMayorRecaudacion_jimenez = recaudacionSucursal_jimenez.index(max(recaudacionSucursal_jimenez)) + 1
print(f"\nLa sucursal de mayor recaudación es la Sucursal {sucursalMayorRecaudacion_jimenez}")
