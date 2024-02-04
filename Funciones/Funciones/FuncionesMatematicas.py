import math

# Función para comprobar si es múltiple el segundo número con el primero
def esMultiplo(n1,n2):
    if n1%n2==0:
        return "Es múltiplo"
    else:
        return "No es múltiplo"
    
# Función para calcular la media
def temperaturaMedia(minima_jimenez, maxima_jimenez):
    # Devolver temperatura media
    return (minima_jimenez+maxima_jimenez)/2

# Función para calcular el área y el perímetro de una circunferencia a partir de un radio
def calcularAreaPerimetro(radio_jimenez):
    area_jimenez = math.pi*(radio_jimenez**2)
    perimetro_jimenez = 2*math.pi*radio_jimenez
    return (f"\nÁREA: {area_jimenez:.2f} cms2\nPERÍMETRO: {perimetro_jimenez:.2f} cms")

# Función para calcular el factorial de un número
def calcularFactorial(numero_jimenez):
    factorial_jimenez=1
    for num in range(numero_jimenez):
        factorial_jimenez=factorial_jimenez*(num+1)
    return factorial_jimenez

# Función para determinar el mayor y el menor
def Ordenar(mayor_jimenez, menor_jimenez):
    if mayor_jimenez<menor_jimenez:
        return menor_jimenez, mayor_jimenez
    else:
        mayor_jimenez, menor_jimenez

# Función para calcular el MCD de dos números
def calcularMCD(dividendo_jimenez, divisor_jimenez):

    # Comprobar y definir el número mayor y el menor
    dividendo_jimenez, divisor_jimenez = Ordenar(dividendo_jimenez, divisor_jimenez)
    resto_jimenez = dividendo_jimenez % divisor_jimenez
    if resto_jimenez == 0:
        return divisor_jimenez
    else:
        return calcularMCD(divisor_jimenez, resto_jimenez)

# Función para calcular cuántos segundos hay en unas horas, minutos y segundos
def calcularSegundos(horas_jimenez, minutos_jimenez, segundos_jimenez):
    return horas_jimenez*3600+minutos_jimenez*60+segundos_jimenez

# Función para convertir los segundos a horas, minutos y segundos
def pasar_a_HMS(segundos_jimenez):
    horas_jimenez = segundos_jimenez//3600
    segundos_jimenez = segundos_jimenez - horas_jimenez*3600
    minutos_jimenez = segundos_jimenez//60
    segundos_jimenez = segundos_jimenez - minutos_jimenez*60
    return horas_jimenez, minutos_jimenez, segundos_jimenez