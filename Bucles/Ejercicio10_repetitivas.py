# Francisco Jiménez Álvarez
# Ejercicio 10
# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

# Mostrar las tablas de multiplicar del 1 al 5
i=0
base_jimenez=1

while base_jimenez<6:
    while i<10:
        i+=1
        print(f"{base_jimenez}*{i}={base_jimenez*i}")

    base_jimenez+=1
    i=0