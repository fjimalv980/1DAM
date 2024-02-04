# Francisco Jiménez Álvarez
# Ejercicio 3
# Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, que utilizando la función anterior,
# vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

from Funciones.FuncionesMatematicas import temperaturaMedia

# Pedir días a introducir al usuario
dias_jimenez = int(input("¿Cuántos días quieres introducir?: "))

# Bucle para pedir temperatura mínima y máxima, y mostrar la temperatura media
for dia_jimenez in range(dias_jimenez):
    minima_jimenez = int(input("Introduce la temperatura mínima: "))
    maxima_jimenez = int(input("Introduce la temperatura máxima: "))
    # Llamar función para calcular la media y mostrarla
    print(f"\nLa temperatura media del día {dia_jimenez+1} es {temperaturaMedia(minima_jimenez, maxima_jimenez)}\n")