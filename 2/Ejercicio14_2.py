# Francisco Jiménez Álvarez
# Ejercicio 14
# La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B,
# y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar
# cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
# se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B,
# se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2.
# Realice un algoritmo para determinar la ganancia obtenida.

# Pedir al usuario el tipo y el tamaño de la uva y el precio del kilo
tipo = str(input("Ingrese el tipo de la uva, siendo 'A' o 'B': "))
tamaño = str(input("Ingrese el tamaño de la uva (1 o 2): "))
precioInicial = float(input("Ingrese el precio del kilo en euros: "))

# Calcular precio total del kilo de uvas según tipo y tamaño
if tipo == "A":
    if tamaño == "1":
        precioFinal = precioInicial + 0.2
    elif tamaño == "2":
        precioFinal = precioInicial + 0.3
    else:
        print("Esa uva no la tenemos")
        precioFinal = 0
elif tipo == "B":
    if tamaño == "1":
        precioFinal = precioInicial - 0.3
    elif tamaño == "2":
        precioFinal = precioInicial - 0.5
    else:
        print("Esa uva no la tenemos")
        precioFinal = 0
else:
    print("Esa uva no la tenemos")
    precioFinal = 0

# Imprimir ganancia por kilo de uva
if precioFinal > 0:
    print(f"La ganancia por kilo de uva es: {precioFinal} euros")
else:
    print("No hay ganancias, ya que se habrá introducido un dato inválido")