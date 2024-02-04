# Francisco Jiménez Álvarez
# Ejercicio 4
# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

# Pedir dos números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Realizar las operaciones
suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2

# Verificar si el segundo número es 0 para evitar la división por cero
if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por 0"

# Mostrar los resultados
print("Suma: ", suma)
print("Resta: ", resta)
print("Producto: ", producto)
print("División: ", division)