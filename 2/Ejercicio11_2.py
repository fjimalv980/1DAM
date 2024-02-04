# Francisco Jiménez Álvarez
# Ejercicio 11
# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
# El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.

# Pedir al usuario que ingrese los tres lados de un triángulo
lado1 = int(input("Ingrese un lado del triángulo: "))
lado2 = int(input("Ingrese otro lado del triángulo: "))
lado3 = int(input("Ingrese el tercer lado del triángulo: "))

# Calcular pitágoras e imprimir si es un triángulo rectángulo
if (lado1 + lado2 == lado3) or (lado2 + lado3 == lado1) or (lado1 + lado3 == lado2):
    print("El triángulo es rectángulo")

# Comprobar si el triángulo es isósceles e imprimirlo
elif (lado1 == lado2) and (lado1 != lado3) or (lado2 == lado3) and (lado2 != lado1):
    print("El triángulo es isósceles")

# Comprobar si el triángulo es equilátero e imprimirlo
elif (lado1 == lado2) and (lado1 == lado3):
    print("El triángulo es equilátero")

# Al no ser ninguna de las anteriores, imprimir que el triángulo es escaleno
else:
    print("El triángulo es escaleno")