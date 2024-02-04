# Función para devolver el contador de la cola
def LongitudCola(cola_jimenez):
    return len(cola_jimenez)

# Función para devolver si la cola está vacía
def EstaVaciaCola(cola_jimenez):
    return len(cola_jimenez) == 0

# Función para saber si la cola está llena
def EstaLlenaCola():
    return False

# Función para añadir elemento a la cola
def AddCola(cadena_jimenez, cola_jimenez):
    cola_jimenez.append(cadena_jimenez)

# Función para devolver el último elemento introducido en la cola
def SacarDeLaCola(cola_jimenez):
    if not EstaVaciaCola(cola_jimenez):
        return cola_jimenez.pop(0)
    else:
        print("La cola está vacía, no se puede sacar ningún elemento")
        return ""

# Función para mostrar los elementos de la cola
def EscribirCola(cola_jimenez):
    for i in cola_jimenez:
        print(i,end=" ")