#Nombre: Escribe si el rol es admin o usuario

#Entradas:
#   Rol: escribe el rol como admin/usurio

#Salidas:
#   Rol: Si el Rol es admin tiene acceso permitido
#   Rol: Si el Rol es usuario u otro tiene acceso restringido

#Proceso: Solicitar el rol, si el rol es admin. Tiene acceso permitido, si el rol es usuario u otro. Tiene acceso restringido
rol = str(input("escribe tu rol como admin/usuario: "))
if rol == "admin":
    print("acceso permitido")
elif rol == "usuario":
    print("acceso restringido")
else:
    print("acceso restringido")
