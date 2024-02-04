# Francisco Jiménez Álvarez
# Ejercicio 14
# Vamos a crear un programa para trabajar con una pila. Una pila es una estructura de datos que nos permite guardar un conjunto de variables.
# La característica fundamental es que el último elemento que se añade al conjunto es el primero que se puede sacar.
# Para representar una pila vamos a utilizar una lista de cadenas de caracteres.
# Vamos a crear varias funciones para trabajar con la pila:
# LongitudPila: Función que recibe una pila y devuelve el número de elementos que tiene.
# EstaVaciaPila: Función que recibe una pila y que devuelve si la pila está vacía, no tiene elementos.
# EstaLlenaPila: Función que recibe una pila y que devuelve si la pila está llena.
# AddPila: función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila, si no está llena. si esta llena muestra un mensaje de error.
# SacarDeLaPila: Función que recibe una pila y devuelve el último elemento añadido y lo borra de la pila. Si la pila está vacía muestra un mensaje de error.
# EscribirPila: Función que recibe una pila y muestra en pantalla los elementos de la pila.
# Realiza un programa principal que nos permita usar las funciones anterior, que nos muestre un menú, con las siguientes opciones:
# Añadir elemento a la pila
# Sacar elemento de la pila
# Longitud de la pila
# Mostrar pila
# Salir

import Funciones.FuncionesEjercicio14 as F

# Variable
pila_jimenez = []

while True:
	print("\n1. Añadir elemento a la pila")
	print("2. Sacar elemento de la pila")
	print("3. Longitud de la pila")
	print("4. Mostrar pila")
	print("5. Salir\n")
	opcion_jimenez = int(input("Elige tu opción: "))
	if opcion_jimenez == 1:
		elemento_jimenez = input("Escribe la cadena que quieres añadir a la pila: ")
		F.AddPila(elemento_jimenez,pila_jimenez)
	elif opcion_jimenez == 2:
		print(F.SacarDeLaPila(pila_jimenez))
	elif opcion_jimenez == 3:
		print("Longitud: ",F.LongitudPila(pila_jimenez))
	elif opcion_jimenez == 4:
		F.EscribirPila(pila_jimenez)
	elif opcion_jimenez == 5:
		break
	else:
		print("Esta opción incorrecta")