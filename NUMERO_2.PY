#Nombre: Determinar si el numero es negativo

#Entradas: 
#   Numero: ingresa un numero

#Salidas:
#   Numero: El numero es negativo o positivo
 
#Proceso: digita un numero, si el numero es menor a 0. El numero es negativo, si no el numero es positivo  
numero = int(input("ingresa un numero: "))
if numero < 0:
    print("el numero es negativo")
else:
    print("el numero es positivo")
