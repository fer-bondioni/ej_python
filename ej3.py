# -*- coding: utf-8 -*-
# Calcular el promedio semanal de gastos en un mes, ingresando como datos:
# Semana número
# Gasto semanal
# El proceso termina cuando “semana número” es igual a 5.


semana = 1
gastoTotal = 0

while semana < 5:
    gasto = int(input("Ingrese gasto semanal: "))
    gastoTotal += gasto
    semana += 1

print(semana)
print("El promedio de gasto semanal es: {}".format(gastoTotal/(semana-1)))
