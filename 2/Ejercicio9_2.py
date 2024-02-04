# Francisco Jiménez Álvarez
# Ejercicio 9
# Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)

# Pide al usuario tres números
numero1 = int (input("Ingresa el primer número: "))
numero2 = int (input("Ingresa el segundo número: "))
numero3 = int (input("Ingresa el tercer número: "))

# Comprobar e imprimir números de mayor a menor
if numero1 >= (numero2 and numero3):
    if numero2 >= numero3:
        print ("El orden de los números de mayor a menor es: ",numero1,",",numero2,",",numero3)
    else:
        print ("El orden de los números de mayor a menor es: ",numero1,",",numero3,",",numero2)
elif numero2 >= (numero1 and numero3):
    if numero1 >= numero3:
        print ("El orden de los números de mayor a menor es: ",numero2,",",numero1,",",numero3)
    else:
        print ("El orden de los números de mayor a menor es: ",numero2,",",numero3,",",numero1)
else:
    if numero1 >= numero2:
        print ("El orden de los números de mayor a menor es: ",numero3,",",numero1,",",numero2)
    else:
        print ("El orden de los números de mayor a menor es: ",numero3,",",numero2,",",numero1)