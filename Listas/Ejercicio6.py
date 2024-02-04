# Francisco Jiménez Álvarez
# Ejercicio 6
# Crea un programa que pida al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

# Inicializar listas de los  días y los nombres de los meses
listaDias_jimenez = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nombreMeses_jimenez = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Pedir al usuario el número del mes
numeroMes_jimenez = int(input("Dime el número correspondiente al mes que quieres saber: "))

# Obligar a elegir entre el 1 y el 12
if numeroMes_jimenez < 13 and numeroMes_jimenez > 0:

    # Elección del nombre y días correspondientes de la lista
    nombreMes_jimenez = nombreMeses_jimenez[numeroMes_jimenez - 1]
    diasMeses_jimenez = listaDias_jimenez[numeroMes_jimenez - 1]

    # Mostrar el resultado
    print(f"El mes {numeroMes_jimenez} es {nombreMes_jimenez} y tiene {diasMeses_jimenez} días.")

else:
    print("El número no pertenece a ningún mes. Tienes que elegir del 1 al 12.")