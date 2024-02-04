# Francisco Jiménez Álvarez
# Ejercicio 20
# Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos
# cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

# Pedir al usuario la cantidad de monedas de cada tipo
monedas2euros = int(input("Ingrese la cantidad de monedas de 2 euros: "))
monedas1euro = int(input("Ingrese la cantidad de monedas de 1 euro: "))
monedas50centimos = int(input("Ingrese la cantidad de monedas de 50 céntimos: "))
monedas20centimos = int(input("Ingrese la cantidad de monedas de 20 céntimos: "))
monedas10centimos = int(input("Ingrese la cantidad de monedas de 10 céntimos: "))

# Calcular el dinero total en euros y céntimos
dineroEuros = (monedas2euros * 2) + (monedas1euro * 1) + (monedas50centimos * 0.5) + (monedas20centimos * 0.2) + (monedas10centimos * 0.1)

# Convertir euros a céntimos
dineroCentimos = dineroEuros * 100

# Imprimir el dinero total en euros y céntimos
print("Tienes", dineroEuros, "euros y", dineroCentimos, "céntimos.")