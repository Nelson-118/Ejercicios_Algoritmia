#Nombre: Verificar la temperatura

#Entradas: 
#   Temperatura: escribe la temperatura a la que estamos

#Salidas:
#   Temperatura: La temperatura es la adecuada o la no adecuada

#Proceso: Verifica la temperatura, si la temperatura es menor o igual a 0. Es la temperatura adecuada para la congelacion, si no. No es la temperatura adecuada para la congelacion
temperatura = float(input("escribe la temperatura a la que estamos: "))
if temperatura <= 0:
    print("si es la temperatura adecuada para la congelacion")
else:
    print("no es la temperatura adecuada para la congelacion")