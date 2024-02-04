# Francisco Jiménez Álvarez
# Ejercicio 7
# Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

# Pide al usuario un número
numero_jimenez=int(input("Ingrese un número: "))

# Mostrar la tabla de multiplicar del número
i=0
while i<10:
    i+=1
    print(f"{numero_jimenez}*{i}={numero_jimenez*i}")