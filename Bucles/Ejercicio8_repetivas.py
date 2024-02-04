# Francisco Jiménez Álvarez
# Ejercicio 8
# Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# He informa si hemos introducido algún número igual a los límites del intervalo.

# Pedir límite inferior y superior al usuario
inferior_jimenez=int(input("Ingrese el límite inferior del intervalo: "))
superior_jimenez=int(input("Ingrese el límite superior del intervalo: "))

# Si el límite inferior es mayor que el superior se vuelve a pedir
while inferior_jimenez>superior_jimenez:
    inferior_jimenez=int(input("Ingrese el límite inferior del intervalo: "))

# Pedir al usuario que ingrese números y para terminar el 0
print("Ingresa números y para parar introduce un 0")
fuera_jimenez=0
suma_jimenez=0
dentro_jimenez=False

numero_jimenez=int(input())
while numero_jimenez!=0:
    numero_jimenez=int(input())
    if numero_jimenez==inferior_jimenez or numero_jimenez==superior_jimenez:
        dentro_jimenez=True
    elif numero_jimenez<inferior_jimenez or numero_jimenez>superior_jimenez:
        fuera_jimenez+=1
    else:
        suma_jimenez=suma_jimenez+numero_jimenez

# Mostrar en pantalla la suma de los números dentro del intervalo, la cantidad de números fuera del intervalo y si hay o no algún número igual a un límite
print(f"La suma de los números dentro de los intervalos es: {suma_jimenez}")
print(f"La cantidad de números fuera del intervalo es: {fuera_jimenez}")
if dentro_jimenez==True:
    print("Has introducido algún número igual a un límite del intervalo")
else:
    print("No has introducido ningún número igual a un límite del intervalo")