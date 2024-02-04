# Francisco Jiménez Álvarez
# Ejercicio 3
# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.

# Pedir al usuario un número
numero_jimenez=int(input("Ingrese un número: "))

i=0
suma_jimenez=0

while numero_jimenez!=0:
    i+=1
    suma_jimenez=numero_jimenez+suma_jimenez
    numero_jimenez=int(input("Ingrese un número: "))

if i!=0:
    print(f"La suma de todos los números introducidos es: {suma_jimenez}")
    print(f"La media de todos los números introducidos (sin contar el 0) es: {suma_jimenez/i}")
else:
    print("La suma y la media es 0, ya que solo introdujiste 0, que es el final del bucle")