#Ejemplo 11
#Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.

class Cuadrado:
    def __init__(self):
        pass
    def suma(self):
        self.Suma=0
        for i in range(1,101):
            self.Suma+= i * i

    def mostrar(self):
        print('La suma de los cuadrados de los primeros 100 enteros es:', self.Suma)

Micuadrado=Cuadrado()
Micuadrado.suma()
Micuadrado.mostrar()

