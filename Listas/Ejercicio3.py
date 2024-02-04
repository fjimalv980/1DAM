# Francisco Jiménez Álvarez
# Ejercicio 3
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

# Crear lista con 10 valores aleatorios
lista_jimenez=[]
print("Dime tus 5 notas: ")
for numero_jimenez in range(0, 5):
    nota_jimenez = float(input(f"Nota {numero_jimenez+1}: "))
    if nota_jimenez>=0 and nota_jimenez<=10:
        lista_jimenez.append(nota_jimenez)
    else:
        print("La nota no es válida. Introduce una nota entre 0 y 10")
        numero_jimenez = numero_jimenez - 1
    
# Hacer media
media_jimenez = sum(lista_jimenez)/5

# Mostrar notas, media, la más alta y la más baja
print(f"Todas las notas: {lista_jimenez}")
print(f"Nota media: {media_jimenez}")
print(f"Nota más alta: {max(lista_jimenez)}")
print(f"Nota más baja: {min(lista_jimenez)}")