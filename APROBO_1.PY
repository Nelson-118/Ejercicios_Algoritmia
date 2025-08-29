#Nombre: Determinar si el estudiante aprobo o reprobo

#Entradas:
#   Nota: Escribe una Nota

#Salidas:
#   Nota: El estudiante aprobo o reprobo

#Proceso: Solicitar la nota de un estudiante, si la nota es igual o mayor a 60. El estudiante aprobo si es menor reprobo
nota = int(input("escribe una nota: "))
if nota >= 60:
    print("el estudiante aprobo")
else:
    print("el estudiante reprobo")