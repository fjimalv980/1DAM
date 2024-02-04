# Función que recibe dos números y los devuelve ordenados de mayor a menor
def Ordenar(mayor_jimenez, menor_jimenez):
    if mayor_jimenez < menor_jimenez:
        return menor_jimenez, mayor_jimenez
    else:
        return mayor_jimenez, menor_jimenez
    
# Función para leer la fracción
def Leer_fraccion():
    numerador_jimenez = int(input("Numerador: "))
    denominador_jimenez = int(input("Denominador: "))
    numerador_jimenez, denominador_jimenez = Simplificar_fraccion(numerador_jimenez, denominador_jimenez)
    return numerador_jimenez, denominador_jimenez

# Función para recibir una fracción y mostrarla. Si el denominador es 1 no se muestra este
def Escribir_fraccion(numerador_jimenez, denominador_jimenez):
    if denominador_jimenez != 1:
        print(numerador_jimenez/denominador_jimenez)
    else:
        print (numerador_jimenez)

# Función que recibe dos números y devuelve el MCD de Euclides
def Calcular_mcd(numero1_jimenez, numero2_jimenez):
    numero1_jimenez, numero2_jimenez = Ordenar(numero1_jimenez, numero2_jimenez)
    resto_jimenez = numero1_jimenez % numero2_jimenez
    if resto_jimenez == 0:
        return numero2_jimenez
    else:
        return Calcular_mcd(numero2_jimenez, resto_jimenez)
    
# Función que recibe una fracción y la devuelve simplificada
def Simplificar_fraccion(numerador_jimenez, denominador_jimenez):
    mcd_jimenez = Calcular_mcd(numerador_jimenez, denominador_jimenez)
    numerador_jimenez = numerador_jimenez / mcd_jimenez
    denominador_jimenez = denominador_jimenez / mcd_jimenez
    return numerador_jimenez, denominador_jimenez

# Función para sumar dos fracciones y simplificar el resultado
def Sumar_fracciones(numerador1_jimenez, denominador1_jimenez, numerador2_jimenez, denominador2_jimenez):
    numerador_jimenez = numerador1_jimenez*denominador2_jimenez + denominador1_jimenez*numerador2_jimenez
    denominador_jimenez = denominador1_jimenez*denominador2_jimenez
    numerador_jimenez, denominador_jimenez = Simplificar_fraccion(numerador_jimenez, denominador_jimenez)
    return numerador_jimenez, denominador_jimenez

# Función para restar dos fracciones y simplificar el resultado
def Restar_fracciones(numerador1_jimenez, denominador1_jimenez, numerador2_jimenez, denominador2_jimenez):
    numerador_jimenez = numerador1_jimenez*denominador2_jimenez - denominador1_jimenez*numerador2_jimenez
    denominador_jimenez = denominador1_jimenez*denominador2_jimenez
    numerador_jimenez, denominador_jimenez = Simplificar_fraccion(numerador_jimenez, denominador_jimenez)
    return numerador_jimenez, denominador_jimenez

# Función para multiplicar fracciones y simplificar el resultado
def Multiplicar_fracciones(numerador1_jimenez, denominador1_jimenez, numerador2_jimenez, denominador2_jimenez):
    numerador_jimenez = numerador1_jimenez*numerador2_jimenez
    denominador_jimenez = denominador1_jimenez*denominador2_jimenez
    numerador_jimenez, denominador_jimenez = Simplificar_fraccion(numerador_jimenez, denominador_jimenez)
    return numerador_jimenez, denominador_jimenez

# Función para multiplicar fracciones y simplificar el resultado
def Dividir_fracciones(numerador1_jimenez, denominador1_jimenez, numerador2_jimenez, denominador2_jimenez):
    numerador_jimenez = numerador1_jimenez*denominador2_jimenez
    denominador_jimenez = denominador1_jimenez*numerador2_jimenez
    numerador_jimenez, denominador_jimenez = Simplificar_fraccion(numerador_jimenez, denominador_jimenez)
    return numerador_jimenez, denominador_jimenez