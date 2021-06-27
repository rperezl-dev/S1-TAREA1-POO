#Ejemplo 17
#Calcular el factorial de N números enteros leídos de teclado. El problema consistirá en realizar una estructura de N iteraciones
# aplicando el factorial de un número.

from main import Validar
from random import randint

class Numero:

    def __init__(self):
        self.iteraciones = int
        self.numero = int
        self.factorial = int

    def valor(self, procedimiento='no hay iteraciones'):
        if procedimiento == 'iteraciones':
            num = val.validar_int('Ingrese el número de iteraciones: ')
            num_factorial.procedimiento(num, 'iteraciones')

        else:
            num = val.validar_int('Ingrese un número: ')
            num_factorial.procedimiento(num)

    def procedimiento(self, num, procedimiento='no hay iteraciones'):
        if num == '' and procedimiento == 'iteraciones':
            print('Por defecto')
            if procedimiento == 'iteraciones':
                self.iteraciones = randint(0, 100)
                print('El valor del número es:', self.iteraciones)
        else:
            self.iteraciones = num

        if num == '' and procedimiento == 'no hay iteraciones':
            print('Por defecto')
            if procedimiento == 'no hay iteraciones':
                self.numero = randint(0, 100)
                print('El valor del número es:', self.numero)
        else:
            self.numero = num

    def calcular(self):
        for _ in range(1, self.iteraciones + 1):
            num_factorial.valor()
            self.factorial = 1

            for i in range(1, self.numero + 1):
                self.factorial *= i
            num_factorial.mostrar()

    def mostrar(self):
        print('El número entero', self.numero, ' tiene como factorial al número', self.factorial, '\n')

num_factorial = Numero()
val = Validar()
num_factorial.valor('iteraciones')
num_factorial.calcular()