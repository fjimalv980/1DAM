# Francisco Jiménez Álvarez
# Ejercicio 12
# Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.

# Pedir al usuario que ingrese lo que ahorra en un mes. Hacerlo 12 veces, para así ver lo ahorrado en un año
print("Ingresa mes por mes tus ahorros en los últimos 12 meses")

total_jimenez=0
for i in range(1, 13):
    ahorros_jimenez=float(input(f"El ahorro del mes {i} es: "))
    total_jimenez=total_jimenez+ahorros_jimenez

# Mostrar el total ahorrado en el año
print(f"El total ahorrado en el año es: {total_jimenez}€")