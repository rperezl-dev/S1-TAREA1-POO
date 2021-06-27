#Ejemplo 13
#Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, utilizando un bucle controlado por el usuario."""

from main import Validar
from random import randint

class Pseudocodigo:
    def __init__(self):
        self.suma = 0
        self.prod = 1
        self.numero = int
        self.resp = str

    def valor(self):
        if self.numero == int:
            return input('Ingrese un caracter determinado: ')
        num = val.validar_int('Ingrese un número entero: ')
        ciclo.predeterminado(num)

    def predeterminado(self, num):
        if num == '':
            print('Por defecto')
            self.numero = randint(0, 101)
            print('El valor del número es:',self.numero)
        else:
            self.numero = num

    def calcular(self):
        self.resp = ciclo.valor()
        while self.resp != 'N' and self.resp != 'n':
            self.numero = 0
            ciclo.valor()
            self.suma += self.numero
            self.prod *= self.numero
            self.numero= int
            print('Desea continuar (S/N) o (s/n)?\n')
            self.resp = ciclo.valor()
            if self.resp == 'N':
                break

    def mostrar(self):
        print('El resultado de la suma es:', self.suma)
        print('El resultado del producto es:', self.prod)

ciclo = Pseudocodigo()
val = Validar()
ciclo.calcular()
ciclo.mostrar()