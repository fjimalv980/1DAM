# Francisco Jiménez Álvarez
# Ejercicio 15
# Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente.
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses.

# Calcular y mostrar cuánto paga cada mes uno por uno
i=0
pago_jimenez=5
total_jimenez=0
while i<20:
    i+=1
    print(f"El mes {i} tengo que pagar {pago_jimenez*2}€")
    pago_jimenez=pago_jimenez*2
    total_jimenez=total_jimenez+pago_jimenez

# Mostrar el total pagado en los 20 meses
print(f"El total pagado en los 20 meses es: {total_jimenez}€")