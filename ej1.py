# -*- coding: utf-8 -*-
from math import sqrt
number = int(input('Ingresá un número: '))
if number > 0:
    calculatedNumber = sqrt(number)
    print('La raíz del número {} es: {}'.format(number, calculatedNumber))
elif(number < 0):
    print('El cuadrado del número {} es {}'.format(number, calculatedNumber))
else:
    print("Ingresaste un valor equivocado")
