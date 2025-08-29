#Nombre: Determinar si el numero es mayor o menor

#Entradas:
#   Numero: escribe el numero

#Salidas:
#   Numero: El numero es mayor o menor

#Proceso: Solicitar numero, Si el numero es mayor o igual a 100. El numero es mayor, si el numero es menor o igual a -100. El numero es mayor

numero = int(input("escribe un numero: "))
if numero >= 100:
    print("el numero es mayor a 100")
elif numero <= -100:
    print("el numero es menor a -100")
    