# Función que recoge una cadena y la centra en pantalla
def escribirCentrado(texto):
    # Calcular longitud
    longitud_jimenez = len(texto)
    # Definir espacios a escribir
    espacios_jimenez = (40-  longitud_jimenez // 2) * " "
    # Devolver de la forma que queremos
    return (espacios_jimenez + texto + "\n" + espacios_jimenez + "=" * longitud_jimenez)

# Función para eliminar espacios iniciales de un texto y luego separar todos los caracteres con un espacio
def convertirEspaciado(texto):
    # Eliminar los espacios del texto con replace() y devolverlo con las letras espaciadas
    return " ".join(texto.replace(" ", ""))