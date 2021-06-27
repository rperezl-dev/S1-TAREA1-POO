
class Validar:

    def __init__(self):
        self.mensaje = str

    def validar_float(self, mensaje):
        self.mensaje = mensaje

        while True:
            try:
                verificar_valor = input(self.mensaje).replace(' ', '')
                if verificar_valor == '':
                    return ''
                else:
                    verificar_valor = float(verificar_valor)
                    verificar_valor = round(verificar_valor, 2)
                    break
            except ValueError:
                print('Error, ingrese un valor correcto.\n')
        return verificar_valor

    def validar_int(self, mensaje):
        self.mensaje = mensaje
        while True:
            try:
                verificar_valor = input(self.mensaje).replace(' ', '')
                if verificar_valor == '':
                    return ''
                if '.' in verificar_valor:
                    verificar_valor = float(verificar_valor)
                verificar_valor = int(verificar_valor)
                break
            except ValueError:
                print('Error, ingrese un valor correcto.\n')
        return verificar_valor