#Ejemplo 14
#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por centinela.

from main import Validar
from random import randint

class Pseudocodigo:
    def __init__(self):
        self.suma = 0
        self.prod = 1
        self.numero = int

    def valor(self):
        num = val.validar_int('Ingrese un número entero: ')
        ciclo.predeterminado(num)

    def predeterminado(self, num):
        if num == '':
            print('Por defecto')
            self.numero = randint(-1, 101)
            print('El valor del número es:',self.numero)
        else: self.numero = num

    def calcular(self):
        while self.numero != -1:
            self.suma += self.numero
            self.prod *= self.numero
            print('')
            ciclo.valor()

    def mostrar(self):
        print('El resultado de la suma es:',self.suma)
        print('El resultado del producto es:',self.prod)

ciclo = Pseudocodigo()
val= Validar()
ciclo.valor()
ciclo.calcular()
ciclo.mostrar()