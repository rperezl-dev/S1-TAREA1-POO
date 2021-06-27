#Ejemplo 7
#Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa,
# sabiendo que cuando las horas de trabajo exceden de 40, el resto  se consideran horas extras y que éstas se pagan al doble
# de una hora normal cuando no exceden de 8;  si las horas extras exceden de 8 se pagan las primeras 8 al  doble de lo que se
# paga por una hora normal y el resto al triple.

class Trabajador:
    def __init__(self):
        self.trabajador=True

    def dinero(self):
        try:
            ht = int(input('Ingrese las horas trabajadas: '))
            ph = int(input('Ingrese el pago por hora normal: $ '))
            if(ht > 40):
                he = ht - 40
                if (he > 8):
                    het = he - 8
                    phe = ph * 2 * 8 + ph * 3 * het
                else:
                    phe = ph * 2 * he

                pt = ph * 40 + phe
            else:
                pt = ph * ht
            print('El pago total de horas trabajadas es: $',pt)
        except:
            print('Error, ingrese solo valores númericos.')


Midinero = Trabajador()
Midinero.dinero()


#Ejercicio realizado en clase.

class Tarea:
    def __init__(self):
        pass
    def pagoJornadaExtra(self):
        horas_trabajadas, horas_extras, horas_extras_triple=0,0,0
        valor_hora, pago_horas_extras, pago_total=0,0,0
        horas_trabajadas=int(input('Ingrese horas trabajadas: '))
        valor_hora=float(input('Ingrese valor hora: '))
        if(horas_trabajadas>40):
            horas_extras=horas_trabajadas-40
            if(horas_extras >8):
                horas_extras_triple=horas_extras-8
                pago_horas_extras= valor_hora *2*8 +valor_hora*3*horas_extras_triple
            else:
                pago_horas_extras=valor_hora*2*horas_extras
            pago_total=valor_hora *40 + pago_horas_extras

        else:
            pago_total= valor_hora*horas_trabajadas
        print(''' Horas Trabajadas:{} Horas Extras:{} Horas Triple:{} Valor Hora:{}
        Pago Valor Extra:{} Pago Total:{}'''.format(horas_trabajadas,horas_extras,horas_extras_triple,valor_hora,pago_horas_extras,pago_total))

tarea=Tarea()
tarea.pagoJornadaExtra()