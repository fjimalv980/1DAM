# Francisco Jiménez Álvarez
# Ejercicio 11
# Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo)

# Pedir dos números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Calcular la distancia entre los dos números con valor absoluto
distancia = abs(numero1 - numero2)

# Imprimir la distancia entre los dos números
print("La distancia entre los números ingresados es: ", distancia)