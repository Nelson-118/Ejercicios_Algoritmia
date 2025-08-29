#Nombre: Triangulos
 
#Etradas: 
#   Lado1: Escribe el lado1 de el triangulo
#   Lado2: Escribe el lado2 de el triangulo
#   Lado3: Escribe el lado3 de el triangulo

#Salidas:
#   Print: Mostrar el tipo de triangulo

#Proceso: Digita cada lado de el triangulo, si los 3 lados son iguales. El triangulo es equilatero, si 2 lados son iguales y 1 lado diferente. Es un triangulo isosceles, si los 3 lados son diferentes. Es un triangulo escaleno
lado1 = int(input("escribe el lado1 de el triangulo: "))
lado2 = int(input("escribe el lado2 de el triangulo: "))
lado3 = int(input("escribe el lado3 de el triangulo: "))
if lado1 == lado2 and lado2 == lado3:
    print("es un triangulo equilatero")
elif lado1 == lado2 and lado2 != lado3:
    print("es un triangulo isosceles")
elif lado1 != lado2 and lado2 != lado3:
    print("es un triangulo escaleno")