#Ejemplo 8
#Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.

class Numeros:
    def __init__(self):
        pass
    def mayor(self):
        try:
            self.numero_mayor=int
            num1 = int(input('Ingrese el primer numero: '))
            num2 = int(input('Ingrese el segundo numero: '))
            num3 = int(input('Ingrese el tercer numero: '))

            if (num1>num2) and (num1>num3):
                self.numero_mayor=num1
                print('Mayor es N1:',self.numero_mayor)
            else:
                if (num2>num3):
                    self.numero_mayor=num2
                    print('Mayor es N2:',self.numero_mayor)
                else:
                    self.numero_mayor = num3
                    print('Mayor es N3:',self.numero_mayor)
        except:
            print('Error, ingrese solo valores númericos.')

Minumero=Numeros()
Minumero.mayor()
