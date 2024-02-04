# Francisco Jiménez Álvarez
# Ejercicio 1
# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1
# hasta el número indicado, y los valores sean los cuadrados de las claves.

# Crear diccionario y contador
diccionario_jimenez = {}
contador_jimenez = 1

# Pedir al usuario un número
numero_jimenez = int(input("Introduce un número: "))

# Añadir números con su cuadrado hasta el número introducido
while contador_jimenez < (numero_jimenez + 1):
    diccionario_jimenez[contador_jimenez]=contador_jimenez**2
    contador_jimenez += 1

# Mostrar claves y valores
for clave_jimenez, valor_jimenez in diccionario_jimenez.items():
    print(f"{clave_jimenez}: {valor_jimenez}")