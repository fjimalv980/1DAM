# Francisco Jiménez Álvarez
# Ejercicio 5
# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

from Funciones.FuncionesComparacion import calcularMaxMin

# Preguntar al usuario cuántos números va a tener la lista
longitudLista_jimenez = int(input("Introduce la cantidad de números en la lista: "))

# Pedir lista de números al usuario
lista_jimenez = [input("\nIntroduce un número: ") for numero_jimenez in range(longitudLista_jimenez)]

# Llamar función y mostrarla
print("\n"+calcularMaxMin(lista_jimenez))