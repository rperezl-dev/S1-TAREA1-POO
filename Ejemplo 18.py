#Ejemplo 18
#Aplicar las fases para la resolución de un problema para leer un vector de 20 números enteros y a continuación escribir
# en un vector A todos los números negativos y en un vector B todos los positivos o iguales a cero. Imprimir dichos vectores.

class Problema:
    def __init__(self):
        self.arrayA = []
        self.arrayB = []

    def calcular(self):
        numeros = []
        vueltas = 0
        for i in range(-10, 11):
            numeros.append(i)
            if numeros[vueltas] > 0:
                self.arrayA.append(numeros[vueltas])
            else:
                self.arrayB.append(numeros[vueltas])
            vueltas += 1

    def mostrar(self):
        print('Vector A: ', end='')
        for valor in self.arrayA:
            print(valor, end=', ')
        print('\nVector B: ', end='')
        for valor in self.arrayB:
            print(valor, end=', ')

Miarray = Problema()
Miarray.calcular()
Miarray.mostrar()