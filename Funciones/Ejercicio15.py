# Francisco Jiménez Álvarez
# Ejercicio 15
# Vamos a realizar un programa similar al anterior para trabajar con una cola. Una cola es una estructura de datos que nos permite guardar un conjunto de variables.
# La característica fundamental es que el primer elemento que se añade al conjunto es el primero que se puede sacar.
# En realizada nos sirven todas las funciones del ejercicio anterior menos la función SacarDeLaCola que es la que tienes que modificar.

import Funciones.FuncionesEjercicio15 as F

# Variable
cola_jimenez = []

while True:
	print("\n1. Añadir elemento a la cola")
	print("2. Sacar elemento de la cola")
	print("3. Longitud de la cola")
	print("4. Mostrar cola")
	print("5. Salir\n")
	opcion_jimenez = int(input("Elige tu opción: "))
	if opcion_jimenez == 1:
		elemento_jimenez = input("Escribe la cadena que quieres añadir a la cola: ")
		F.AddCola(elemento_jimenez,cola_jimenez)
	elif opcion_jimenez == 2:
		print(F.SacarDeLaCola(cola_jimenez))
	elif opcion_jimenez == 3:
		print("Longitud: ",F.LongitudCola(cola_jimenez))
	elif opcion_jimenez == 4:
		F.EscribirCola(cola_jimenez)
	elif opcion_jimenez == 5:
		break
	else:
		print("Esta opción incorrecta")