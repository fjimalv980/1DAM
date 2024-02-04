# Francisco Jiménez Álvarez
# Ejercicio 2
# Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado. Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

# Inicializar lista de 5 números pedidos al usuarios
print("Ingresa 5 cadenas de caracteres: ")
lista_jimenez = [input() for numero_jimenez in range(5)]

# Copiar lista en otra
lista2_jimenez = lista_jimenez.copy()

# Dar
lista2_jimenez.reverse()

# Mostrar lista dada la vuelta
print(lista2_jimenez)