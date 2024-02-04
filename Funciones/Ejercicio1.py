# Francisco Jiménez Álvarez
# Ejercicio 1
# Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista:
# deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =.

from Funciones.FuncionesEscribir import escribirCentrado

# Pedir cadena al usuario
cadena_jimenez=input("Introduce una cadena: ")

# Llamar funciones y mostrar resultado
print(escribirCentrado(cadena_jimenez))