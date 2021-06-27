#Ejemplo 1
#En ejemplos anteriores, diseñamos un pseudocódigo para encontrar la superficie de un círculo para un radio cualquiera.
# El Flujograma que representa a dicho ejemplo es el siguiente:

class Circulo:
    def __init__(self):
        self.pi = 3.1416
        self.superficie = float
        self.radio = float

    def valor_radio(self):
        self.radio = float(input('Ingrese el radio de un círculo: '))

    def calcular_superficie(self):
        self.superficie = round((self.pi * self.radio ** 2),2)

    def mostrar(self):
        print(f'la superficie de un círculo con un radio de {self.radio} es:', self.superficie)

Mi_superfice_circulo = Circulo()
Mi_superfice_circulo.valor_radio()
Mi_superfice_circulo.calcular_superficie()
Mi_superfice_circulo.mostrar()