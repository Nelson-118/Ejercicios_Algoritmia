#Nombre: Determinar si la persona puede votar

#Entradas: 
#   Edad: escriba la edad
#   Nacionalidad: Escriba su nacionalidad

#Salidas:
#   Edad: El numero es mayor o igual a 18
#   Nacionalidad: La nacionalidad es colombiana

#Proceso: Digita la edad y escribe su nacionalidad, si la edad es mayor o igual a 18 y la nacionalidad es colombiana. La persona puede votar
edad = int(input("escriba la edad: "))
nacionalidad = str(input("escriba su nacionalidad: "))

if edad >= 18 and nacionalidad == "colombiana":
    print("puede votar")
else:
    print("no puede votar")
    