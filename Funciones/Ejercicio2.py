# Francisco Jiménez Álvarez
# Ejercicio 2
# Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
# Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

from Funciones.FuncionesMatematicas import esMultiplo

# Pedir 2 números al usuario
num1_jimenez=int(input("Introduce un número: "))
num2_jimenez=int(input("Introduce otro número: "))

# Llamar función e imprimir resultado
print(esMultiplo(num1_jimenez, num2_jimenez))