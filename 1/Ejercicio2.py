# Francisco Jiménez Álvarez
# Ejercicio 2
# Calcular el perímetro y área de un rectángulo dada su base y su altura.

# Pedir lados
print('Dime la altura y base del rectángulo')

altura=float(input())
base=float(input())

# Imprimir el resultado directamente con las fórmulas
print('El perímetro del rectángulo es:',(altura+base)*2,'m')
print('El área del rectángulo es:',altura*base,'m2')