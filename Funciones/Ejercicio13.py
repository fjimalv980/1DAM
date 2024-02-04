# Francisco Jiménez Álvarez
# Ejercicio 13
# Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.
# Vamos a crear las siguientes funciones para trabajar con funciones:
# Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando leas una fracción debes simplificarla.
# Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el numerador.
# Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
# Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y dominador por el MCD del numerador y denominador.
# Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.
# Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado.
# Crear un programa que utilizando las funciones anteriores muestre el siguiente menú:
# Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.
# Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.
# Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra la producto.
# Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra la cociente.
# Salir

import Funciones.FuncionesEjercicio13 as F

# Bucle para mostrar el menú de opciones y controlarlas
while True:
	print("\n1. Sumar fracciones")
	print("2. Restar fracciones")
	print("3. Multiplicar fracciones")
	print("4. Dividir fracciones")
	print("5. Salir")
	opcion_jimenez = int(input("\nElige una opción: "))
	if opcion_jimenez>=1 and opcion_jimenez <=4:
		print("\nFracción 1: ")
		numerador1_jimenez, denominador1_jimenez = F.Leer_fraccion()
		print("\nFracción 2: ")
		numerador2_jimenez, denominador2_jimenez= F.Leer_fraccion()
		if opcion_jimenez == 1:
			print("\nSumar fracciones")
			numerador_jimenez,denominador_jimenez = F.Sumar_fracciones(numerador1_jimenez, denominador1_jimenez, numerador2_jimenez, denominador2_jimenez)
			F.Escribir_fraccion(numerador_jimenez, denominador_jimenez)
		elif opcion_jimenez == 2:
			print("\nRestar fracciones")
			numerador_jimenez,denominador_jimenez = F.Restar_fracciones(numerador1_jimenez, denominador1_jimenez, numerador2_jimenez, denominador2_jimenez)
			F.Escribir_fraccion(numerador_jimenez,denominador_jimenez)
		elif opcion_jimenez == 3:
			print("\nMultiplicar fracciones")
			numerador_jimenez,denominador_jimenez = F.Multiplicar_fracciones(numerador1_jimenez, denominador1_jimenez, numerador2_jimenez, denominador2_jimenez)
			F.Escribir_fraccion(numerador_jimenez,denominador_jimenez)
		elif opcion_jimenez == 4:
			print("\nDividir fracciones")
			numerador_jimenez,denominador_jimenez = F.Dividir_fracciones(numerador1_jimenez, denominador1_jimenez, numerador2_jimenez, denominador2_jimenez)
			F.Escribir_fraccion(numerador_jimenez,denominador_jimenez)
		elif opcion_jimenez == 5:
			break
	else:
			print("\nEsta opción es incorrecta\n")