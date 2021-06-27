#Ejemplo 6
#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600,
# en caso contrario no tendrá aumento.

class Empleado:
    def __init__(self):
        self.aumento=0.10

    def sueldo_empleado(self):
        try:
            self.sueldo=float(input('Ingrese el sueldo: $ '))
            if (self.sueldo < 600):
                incremento=self.sueldo * self.aumento
                nuevo_sueldo=self.sueldo+incremento
                print('El nuevo sueldo con incremento del 10% es de: $',nuevo_sueldo)
            else:
                print('Sueldo normal sin aumento: $', self.sueldo)
        except:
            print('Error, ingrese solo valores númericos.')

Miempleado=Empleado()
Miempleado.sueldo_empleado()