#Nombre: Determinar si el año es bisiesto

#Entradas:
#   Año: esribe el año

#Salidas:
#   Año: El año es bisiesto o no

#Proceso: Solicitar el año, divide el año entre 4 el resultado es 0, divide el año entre 100 es diferente a 0, divide el año en 400 es igual a 0. Imprime el año


   
año = int(input("escribe el año: "))
if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
  print("el año es bisiesto")
else:
    print("el año no es bisiesto")
    