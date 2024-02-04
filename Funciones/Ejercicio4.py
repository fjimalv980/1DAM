# Francisco Jiménez Álvarez
# Ejercicio 4
# Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional
# tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

from Funciones.FuncionesEscribir import convertirEspaciado
# Pedir cadena al usuario
texto_jimenez = input("Introduce una cadena: ")

# Llamar función y mostrarla
print(convertirEspaciado(texto_jimenez))