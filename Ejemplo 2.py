#Ejemplo 2
#En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar
# finalmente por su compra.

class Tienda:
    def __init__(self):
        self.descuento= 0.15

    def valor(self, precio):
        self.__precio_final=precio
        while True:
            if (self.__precio_final>0):
                try:
                    precio= float(input('Ingrese el precio de su compra: '))
                    precio_total = precio - precio * self.descuento
                    print('El precio final con descuento del 15% es: ',precio_total)
                except ValueError:
                    print('¡Error!')
                else:
                    return
Mitienda=Tienda()
Mitienda.valor(True)