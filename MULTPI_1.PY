#Nombre: Multiplo de 5

#Entradas:
#   Numero1: escribe el numero

#Salidas:
#   Numero1: El numero es multiplo o no es multiplo de 5

#Proceso: Digita un numero, si el numero se divide en 5 y el resultado es 0. Es multiplo de 5, si el resultado no es 0. No es multiplo de 5
numero1 = int(input("escribe un numero: "))
if numero1 % 5 == 0:
    print("el numero es multiplo de 5")
else:
    print("el numero no es multiplo de 5")
