# Francisco Jiménez Álvarez
# Ejercicio 20
# Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio
# de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:
# Zona	Ubicación	Costo/gramo
# 1	América del Norte	24.00 euros
# 2	América Central	20.00 euros
# 3	América del Sur	21.00 euros
# 4	Europa	10.00 euros
# 5	Asia	18.00 euros
# Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad.
# Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

# Pedir al usuario el peso del paquete y la zona dónde quiere enviarlo, denegando el envío si el peso es mayor a 5 kg
peso = int(input("Ingrese el peso del paquete en gramos: "))
if (peso <= 5000) and (peso > 0):
    zona = int(input("Ingrese el número dependiendo de la zona de destino del paquete. 1'América del norte', 2'América central', 3'América del sur', 4'Europa' y 5'Asia': "))
    if (zona < 1) or (zona > 7):
        print("La zona no es correcta")
else:
    print("El peso no es aceptado, lo siento")
    zona = 0

# Calcular precio dependiendo de la zona y mostrarlo en pantalla
if zona == 1:
    print(f"El precio es: {peso*24} €")
elif zona == 2:
    print(f"El precio es: {peso*20} €")
elif zona == 3:
    print(f"El precio es: {peso*21} €")
elif zona == 4:
    print(f"El precio es: {peso*10} €")
elif zona == 5:
    print(f"El precio es: {peso*18} €")

# Cabe aclarar que creo que hay un error en el enunciado del ejercicio, ya que pone precio por gramo, e imagino que sería por kg.
#  Pero he hecho lo que ponía.