# Francisco Jiménez Álvarez
# Ejercicio 8
# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto
# de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

# Obtener el sueldo base y el monto de las ventas del usuario
sueldoBase = float(input("Ingrese el sueldo base del vendedor: "))
venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))

# Calcular la comisión para cada venta (10% del monto de la venta)
comision1 = venta1 * 0.10
comision2 = venta2 * 0.10
comision3 = venta3 * 0.10

# Calcular el total de comisiones
totalComisiones = comision1 + comision2 + comision3

# Calcular el salario total (sueldo base + total de comisiones)
salarioTotal = sueldoBase + totalComisiones

# Mostrar el total de comisiones y el salario total del vendedor en el mes
print("Total de comisiones por las tres ventas: ", totalComisiones)
print("Salario total en el mes (sueldo base + comisiones): ", salarioTotal)