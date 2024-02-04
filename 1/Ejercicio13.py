# Francisco Jimñenez Álvarez
# Ejercicio 13
# Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
# Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?

# Pedir al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Calcular la raíz cuadrada y raíz cúbica
raiz_cuadrada = numero ** (1/2)
raiz_cubica = numero ** (1/3)

# Mostrar resultados de raíz cuadrada y cúbica
print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)
print("La raíz cúbica de", numero, "es:", raiz_cubica)