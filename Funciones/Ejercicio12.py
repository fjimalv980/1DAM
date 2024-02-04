# Francisco Jiménez Álvarez
# Ejercicio 12
# Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. De tal forma que al leer una fecha se asegura que es válida.

from Funciones.FuncionesComparacion import LeerFecha2, Calcular_Dia_Juliano

d,m,a = LeerFecha2()
print("El día juliano es: ",Calcular_Dia_Juliano(d,m,a))