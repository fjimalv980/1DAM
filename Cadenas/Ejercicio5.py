# Francisco Jiménez Álvarez
# Ejercicio 5
# Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las iniciales en mayúsculas.

# Pedir al usuario su nombre y apellidos
nombre_jimenez = print(input("Escribe tu nombre y apellidos: "))

# Dividir la cadena en palabras
palabras_jimenez = nombre_jimenez.split()

# Obtener las iniciales en mayúsculas
iniciales_jimenez = [palabras_jimenez[0].upper() for palabra in palabras_jimenez]

# Mostrar el resultado
print(f"Las iniciales en mayúsculas son: {resultado}")