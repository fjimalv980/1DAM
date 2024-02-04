# Francisco Jiménez Álvarez
# Ejercicio 7
# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
# Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

# Obtener la cantidad de minutos del usuario
minutos = int(input("Ingrese la cantidad de minutos: "))

# Calcular las horas y minutos
horas = minutos // 60
minutosRestantes = minutos % 60

# Mostrar el resultado
print(f"{minutos} minutos son {horas} horas y {minutosRestantes} minutos.")