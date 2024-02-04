# Francisco Jiménez Álvarez
# Ejercicio 7
# Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
# Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

from Funciones.FuncionesComparacion import login
# Variables
contador_jimenez = 0

# Bucle para repetir 
while True:
	usuario_jimenez = input("\nIntroduce tu nombre de usuario: ")
	contraseña_jimenez = input("\nIntroduce tu contraseña: ")
	pase_jimenez, contador_jimenez = login(usuario_jimenez, contraseña_jimenez, contador_jimenez)
	if not pase_jimenez:
		print("\nError. El nombre de usuario o la contraseña es incorrecta.")
	if pase_jimenez or contador_jimenez == 3:
		break
	
if pase_jimenez:
	print("\nLogin correcto")
else:
	print("\nNo has podido entrar")
