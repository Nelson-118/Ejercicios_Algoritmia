#Nombre: Programa para obtener iniciales en mayuscula

#Entradas:
#   Nombre: Nombre de la persona ,
#   Apellido: Apellido de la persona

#Salidas:
#   Iniciales: La primera letra de nombre y apellido

#Proceso: Solicitar el nombre y el apellido de la persona, extrae la primera letra de el nombre y el apelludo. Imprime en mayuscula las iniciales

#Pedir nombre y apellido
nombre= input("ingresa tu nombre; ")
apellido= input("ingresa tu apellido; ")

#Tomar la primera letra de cada uno y ponerla en mayuscula
iniciales= nombre[0].upper() + apellido[0].upper()


#Mostrar resultado
print("tus iniciales son", iniciales)

