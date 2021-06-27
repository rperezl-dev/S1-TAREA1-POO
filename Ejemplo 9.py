#Ejemplo 9
#Diseñar un algoritmo tal que dados como datos dos variables de tipo entero, obtenga el resultado de la siguiente función:
"""
                     --
                    |
                   |  100 * V          si num == 1
                  <   100 ^ V          si num == 2
                   |  100 / V          si num == 3, para V < > 0
                   |     0             cualquier otro valor de num
                   --                                                             """

class Datos:
    def __init__(self):
        pass
    def operacion(self):
        try:
            self.Val=int
            num=int(input('Ingrese una variable entera: '))
            V=int(input('Ingrese el valor de V: '))

            if (num == 1):
                self.Val = 100 * V
            elif (num == 2):\
                self.Val=100*V
            elif (num == 3):
               self.Val=100/V
            else:
                self.Val=0
            print('El valor de la funcion es: ',self.Val)
        except:
            print('Error, ingrese solo valores númericos.')

Misdatos=Datos()
Misdatos.operacion()