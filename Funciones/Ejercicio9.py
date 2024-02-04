# Francisco Jiménez Álvarez
# Ejercicio 9
# Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:
# Se divide el número mayor entre el menor.
# Si la división es exacta, el divisor es el MCD.
# Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
# Crea un programa principal que lea dos números enteros y muestre el MCD.

from Funciones.FuncionesMatematicas import calcularMCD

# Pedir dos números al usuario
numero1_jimenez = int(input("Introduce un número: "))
numero2_jimenez = int(input("Introduce otro número: "))

# Llamar a la función y mostrar el resultado
print("El MCD es: ", calcularMCD(numero1_jimenez, numero2_jimenez))