# -*- coding: utf-8 -*-
# Un usuario ingresa 3 números: Encontrar el mayor

num1 = int(input("Ingresá el primer número: "))
num2 = int(input("Ingresá el segundo número: "))
num3 = int(input("Ingresá el tercer número: "))

if num1 > num3 and num1 > num2:
    print('El número 1 {} es el mayor'.format(num1))
else:
    if num2 > num3:
        print("El número 2 {} es el mayor".format(num2))
    else:
        print("El número 3 " + str(num3) + " es el mayor")
        if(num3 % 2 == 0):
            print('Y además es par')
        else:
            print('es impar')
