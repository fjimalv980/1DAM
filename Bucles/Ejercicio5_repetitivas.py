# Francisco Jiménez Álvarez
# Ejercicio 5
# Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.

# Pide al usuario un carácter
caracter_jimenez=(input("Ingrese un carácter, si es vocal en minúscula te lo diré. Si introduces más de un carácter no contará como vocal. Introduce un espacio para terminar: "))

# Comprobar si es un carácter y si es vocal o no, e imprimirlo en la pantalla hasta introducirse un espacio
while caracter_jimenez!=" ":
    if caracter_jimenez=="a" or caracter_jimenez=="e" or caracter_jimenez=="i" or caracter_jimenez=="o" or caracter_jimenez=="u":
        print("VOCAL")
    else:
        print("NO VOCAL")
    caracter_jimenez=(input("Ingrese otro carácter o espacio para terminar: "))