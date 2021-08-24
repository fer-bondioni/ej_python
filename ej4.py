# -*- coding: utf-8 -*-
# Ingresar números hasta que el último sea cero. Calcular la cantidad de positivos.

cantidadPositivos = 1
number = 1

while number != 0:
    number = int(input('Insertá número: '))
    if(number > 0):
        cantidadPositivos = cantidadPositivos + 1

print(cantidadPositivos)
print("Escribiste: {} números positivos.".format(cantidadPositivos - 1))
