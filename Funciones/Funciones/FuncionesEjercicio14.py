# Función para devolver el contador de la pila
def LongitudPila(pila_jimenez):
    return len(pila_jimenez)

# Función para devolver si la pila está vacía
def EstaVaciaPila(pila_jimenez):
    return len(pila_jimenez) == 0

# Función para saber si la pila está llena
def EstaLlenaPila():
    return False

# Función para añadir elemento a la pila
def AddPila(cadena_jimenez, pila_jimenez):
    pila_jimenez.append(cadena_jimenez)

# Función para devolver el último elemento introducido en la pila
def SacarDeLaPila(pila_jimenez):
    if len(pila_jimenez) > 0:
        return pila_jimenez.pop()
    else:
        print("La pila está vacía, no se puede sacar ningún elemento")

# Función para mostrar los elementos de la pila
def EscribirPila(pila_jimenez):
    for i in pila_jimenez:
        print(i,end=" ")