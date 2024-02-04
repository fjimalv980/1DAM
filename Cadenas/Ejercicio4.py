# Francisco Jiménez Álvarez
# Ejercicio 4
# Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.

# Pedir al usuario una frase
frase_jimenez = input("Ingrese una frase: ")

# Contar cuantas palabras hay en la frase
palabras_jimenez = frase_jimenez.split()

# Mostrar la cantidad de palabras que hay
cantidad_palabras = len(palabras_jimenez)

if cantidad_palabras != 1:
    print(f"La frase tiene {cantidad_palabras} palabras.")

# Si es una palabra saldrá en singular 'palabra'
else:
    print(f"La frase tiene {cantidad_palabras} palabra.")