#Ejemplo 15
#Determinar si un número entero proporcionado por el usuario es primo. Un número primo es un entero que no tiene más
# divisores que él mismo y la unidad. Elaborar Pseudocódigo:

class Numero:
    def __init__(self):
        pass
    def primo(self):
        primo=True
        divisor=2
        try:
            num=int(input('Ingrese un numero entero: '))
            while (divisor <num) and (primo==True):
                resp=num % divisor
                if (resp==0):
                    primo = 'F'
                divisor=divisor+1
            if (primo==True):
                print('Numero',num,'es primo.')
            else:
                print('Numero', num, 'no es primo.')
        except:
            print('Error, ingrese solo valores númericos.')
Minumero=Numero()
Minumero.primo()