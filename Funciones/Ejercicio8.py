# Francisco Jiménez Álvarez
# Ejercicio 8
# Crear una función recursiva que permita calcular el factorial de un número. Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial.

from Funciones.FuncionesMatematicas import calcularFactorial

# Pedir número al usuario
numero_jimenez = int(input("Introduce un número: "))

# Llamar a la función y mostrar el resultado
print(f"El factorial de {numero_jimenez} es {calcularFactorial(numero_jimenez)}")