# Francisco Jiménez Álvarez
# Ejercicio 2
# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

# Crear diccionario
diccionario_jimenez = {}

# Pedir al usuario una cadena
cadena_jimenez = input("Introduce una cadena: ")

# Contar caracteres de la cadena y guardarlos en el diccionario
for caracter_jimenez in cadena_jimenez:
	if caracter_jimenez in diccionario_jimenez:
		diccionario_jimenez[caracter_jimenez] += 1
	else:
		diccionario_jimenez[caracter_jimenez] = 1	

# Mostrar claves y valores del diccionario
for clave_jimenez, valor_jimenez in diccionario_jimenez.items():
	print (f"{clave_jimenez}: aparece {valor_jimenez} veces")