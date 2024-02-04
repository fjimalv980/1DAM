# Francisco Jiménez Álvarez
# Ejercicio 4
# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

# Pedir al usuario cuantos números quiere introducir
cantidad_jimenez=int(input("¿Cuántos números quieres que te compruebe?: "))

# Pedir números al usuario dependiendo de la cantidad pedida y mostrar la cantidad de positivos, negativos y ceros introducidos
i=0
positivos_jimenez=0
negativos_jimenez=0
ceros=0

if cantidad_jimenez>0:
    while cantidad_jimenez>i:
        numero_jimenez=int(input("Introduce un número: "))
        if numero_jimenez==0:
            ceros+=1
        elif numero_jimenez<0:
            negativos_jimenez+=1
        else:
            positivos_jimenez+=1
        i+=1

    print(f"Negativos: {negativos_jimenez}")
    print(f"Positivos: {positivos_jimenez}")
    print(f"Ceros: {ceros}")
else:
    print("Deberías haber introducido una cantidad tangible")