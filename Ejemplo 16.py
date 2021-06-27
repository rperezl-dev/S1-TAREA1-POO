#Ejemplo 16
#Aplicar los pasos de la metodología para la solución de un problema para leer un número entero N y calcular el resultado
# de la siguiente serie:
#                          1 – 1/2 + 1/3 – 1/4 + ... +/- 1/N.
#Resolveremos el problema utilizando bucle Repeat controlado por contador y usando banderas.

from main import Validar
from random import uniform as randfloat

class Problema:

    def __init__(self):
        self.numero = int
        self.serie = 0

    def valor(self):
        num = val.validar_float('Ingrese un número entero: ')
        repetir_ciclo.predeterminado(num)

    def predeterminado(self, num):

        if num == '':
            print('Por defecto')
            self.numero = round(randfloat(0, 101), 2)
            print('El valor del número es:', self.numero)
        else:
            self.numero = num

    def calcular(self):
        cont = 1
        bandera = True
        while cont < self.numero:
            if bandera:
                self.serie += (1 / cont)
                bandera = False
            else:
                self.serie -= (1 / cont)
                bandera = True
            cont += 1

    def mostrar(self):
        print('La solución del problema es:', round(self.serie, 2))

repetir_ciclo = Problema()
val = Validar()
repetir_ciclo.valor()
repetir_ciclo.calcular()
repetir_ciclo.mostrar()