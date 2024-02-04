# Función para devolver el número mínimo y el máximo de una lista
def calcularMaxMin(lista_jimenez):
    # Comprobar maximo y minimo de la lista y devolverlo
    maximo_jimenez = max(lista_jimenez)
    minimo_jimenez = min(lista_jimenez)
    return "El número mínimo de la lista es "+minimo_jimenez+" y el máximo es "+maximo_jimenez

# Función para comparar si una contraseña y un usuario son las correctas
def login(usuario_jimenez, contraseña_jimenez, contador_jimenez):
	contador_jimenez+=1
	if usuario_jimenez == "usuario1" and contraseña_jimenez == "asdasd":
		return (True, contador_jimenez)
	else:
		return (False, contador_jimenez)

# Función para saber si un año es bisiesto
def EsBisiesto(año_jimenez):
	return (año_jimenez % 4 == 0 and not (año_jimenez % 100 == 0)) or año_jimenez % 400 == 0

# Función para pedir un mes y un año y devolver cuántos días tiene. Se tiene en cuenta también los años bisiestos
def DiasDelMes(mes_jimenez,año_jimenez):
	if mes_jimenez in [1,3,5,7,8,10,12]:
		return 31
	elif mes_jimenez in [4,6,9,11]:
		return 30
	elif mes_jimenez == 2:
		if EsBisiesto(año_jimenez):
			return 29
		else:
			return 28
	else:
		return 0

# Función que recibe un día, mes y año y calcula el día juliano
def Calcular_Dia_Juliano(dia_jimenez,mes_jimenez,año_jimenez):
	dj = 0
	for m in range(1,mes_jimenez):
		dj = dj + DiasDelMes(m,año_jimenez)
	dj = dj + dia_jimenez
	return dj

# Función para validar si una fecha está dada correctamente
def ValidarFecha(dia_jimenez,mes_jimenez,año_jimenez):
	if dia_jimenez<1 or dia_jimenez>DiasDelMes(mes_jimenez,año_jimenez):
		return False
	else:
		return True
	
# Función que lee por teclado el día, mes y el año y lo devuelve
def LeerFecha():
	dia_jimenez = int(input("Introduce el día: "))
	mes_jimenez = int(input("Introduce el mes: "))
	año_jimenez = int(input("Introduce el año: "))
	return dia_jimenez, mes_jimenez, año_jimenez

# Función igual que la anterior pero con modificaciones para el ejercicio 12 para validar la fecha
def LeerFecha2():
	while True:
		dia_jimenez = int(input("Introduce el día:"))
		mes_jimenez = int(input("Introduce el mes:"))
		año_jimenez = int(input("Introduce el año:"))
		if not ValidarFecha(dia_jimenez,mes_jimenez,año_jimenez):
			print("La fecha no es válida\n")
		else:
			break
	return dia_jimenez, mes_jimenez, año_jimenez