#Ejemplo 3
#Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. El vendedor desea saber cuánto dinero
# obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes
# tomando en cuenta su sueldo base y sus comisiones.

class Vendedor():
    def __init__(self):
        self.comision=0.1

    def sueldo(self):
        if (self.sueldo):
            try:
                sueldo_base = float(input("Ingrese el sueldo base: "))
                venta1 = float(input(f"Ingrese el precio de la venta 1: "))
                venta2 = float(input(f"Ingrese el precio de la venta 2: "))
                venta3 = float(input(f"Ingrese precio de la venta 3: "))
                comision = venta1 * self.comision + venta2 * self.comision + venta3 * self.comision
                print("Concepto por comisión de ventas: ", comision)
                print("Sueldo total a recibir: ", sueldo_base + comision)
            except:
                print('Error, ingrese solo valores númericos.')

Misueldo=Vendedor()
Misueldo.sueldo()