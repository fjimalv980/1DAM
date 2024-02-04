# Francisco Jiménez Álvarez
# Ejercicio 1
# Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)

# Pedir un número al usuario
numero_jimenez = int(input("Ingrese un número positivo para calcular su factorial: "))

# Calcular factorial del número y mostrarlo en pantalla
factorial_jimenez=1

if numero_jimenez>0:
    while numero_jimenez>1:
        factorial_jimenez=numero_jimenez*factorial_jimenez
        numero_jimenez=numero_jimenez-1
    print(f"El factorial es: {factorial_jimenez}")
else:
    print("El número tiene que ser mayor a 0")