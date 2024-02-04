# Francisco Jiménez Álvarez
# Ejercicio 6
# Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

from Funciones.FuncionesMatematicas import calcularAreaPerimetro

# Pedir el radio al usuario
radio_jimenez = float(input("Introduce el radio en cms: "))

# Llamar a la función y devolver área y perímetro
print(calcularAreaPerimetro(radio_jimenez))