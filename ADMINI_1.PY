#Nombre: Determinar el codigo para entrar con permisos de administrador

#Entradas: 
#   Codigo: escribe el codigo para ingresar con permisos de administrador

#Salidas:
#   Codigo: El usuario tiene permisos de administrador o no tiene permisos de administrador

#Proceso: Digite el codigo, si el codigo es 1927. Tiene permisos de administrador, si el codigo no es 1927. No tiene permisos de administrador
codigo = str(input("escribe el codigo para ingresar con permisos de administrador: "))
if codigo == "1927":

    print("tiene permiso de administrador")
else:
    print("no tiene permiso de administrador")