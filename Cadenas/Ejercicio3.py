# Francisco Jiménez Álvarez
# Ejercicio 3
# Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.

# Pedir al usuario una cadena
cadena_jimenez = input("Ingrese una cadena: ")

# Pedir al usuario un carácter y validar que sea un solo carácter
caracter_jimenez = input("Ingrese un carácter: ")

while len(caracter_jimenez) != 1:
    print("Por favor, ingrese un solo carácter.")
    caracter_jimenez = input("Ingrese un carácter: ")

# Contar cuántas veces está el carácter en la cadena
cantidad_jimenez = cadena_jimenez.count(caracter_jimenez)

# Mostrar cuántas veces aparece el carácter en la cadena
print(f"El carácter '{caracter_jimenez}' aparece {cantidad_jimenez} veces en la cadena.")