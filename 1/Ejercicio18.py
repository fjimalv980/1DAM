# Francisco Jiménez Álvarez
# Ejercicio 18
# Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

# Pedir al usuario su nombre y apellidos
nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")

# Obtener las iniciales
inicialNombre = nombre[0]
inicialApellido1 = apellido1[0]
inicialApellido2 = apellido2[0]

# Mostrar las iniciales
print("Las iniciales de su nombre son:", inicialNombre, inicialApellido1, inicialApellido2)