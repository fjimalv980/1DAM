# Francisco Jiménez Álvarez
# Ejercicio 9
# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

def calcularPrecioFinal():
    # Calcular el descuento del 15%
    descuento = totalCompra * 0.15
    # Calcular el precio final restando el descuento del total de la compra
    precioFinal = totalCompra - descuento
    return precioFinal

# Pedir al usuario que ingrese el total de la compra
totalCompra = float(input("Ingrese el total de la compra: "))

# Calcular el precio final llamando a la función y mostrar el resultado
precioFinal = calcularPrecioFinal()
print("El precio final con el 15% de descuento es: ", precioFinal)