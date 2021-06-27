#Ejemplo 19
#Se tiene información sobre las calificaciones de 6 exámenes de un grupo de 30 alumnos. Los datos sobre estos exámenes
# se proporcionan de la siguiente manera:
#                      Cal1,1 Cal1,2 .......Cal1,6
#                      Cal2,1 Cal2,2 .......Cal2,6
#                      ..............
#                      Cal30,1 Cal30,2 .....Cal30,6
#   Donde Cali,j es una variable real que expresa la calificación que obtuvo el alumno i en el examen j.
#                            1 £ i £ 30, 1£ j £ 6
#Calcular lo siguiente:
#a) El promedio de calificaciones de cada uno de los 6 exámenes.
#b) El promedio de cada alumno.
#c) El tipo (número) de examen que tuvo el mayor promedio de calificación.
#Escriba también dicho promedio.

from main import Validar
from random import uniform as randfloat

class Info_calificaciones:

    def __init__(self):
        self.lista_calificaciones = []
        self.lista_alumnos = []
        self.ALUMNOS= 30
        self.CALIF_REQUERIDAS = 6
        self.prom_leccion = []

    def valor(self):
        for alumno in range(1, 31):
            alum_provisional = input('Nombre del alumno {}: '.format(alumno))
            self.lista_alumnos.append(alum_provisional)

            for calificacion in range(1, 7):
                print('Escriba la calificación del alumno "{}" en el exámen "{}"'.format(alum_provisional, calificacion))
                num = val.validar_float('Nota #{}: '.format(calificacion))
                alumnos.predeterminado(num)
                if calificacion == 1:
                    self.lista_calificaciones.append([self.calif_provisional])
                else:
                    self.lista_calificaciones[alumno - 1].append(self.calif_provisional)
            print('')

    def predeterminado(self, num):
        if num == '':
            print('Por defecto')
            self.calif_provisional = round(randfloat(0, 10.0), 2)
            print('El valor del número es:', self.calif_provisional)
        else:
            self.calif_provisional = num

    def calcular(self):
        for leccion_num in range(6):
            suma_calificaciones = 0
            for nota in self.lista_calificaciones:
                suma_calificaciones += nota[leccion_num]
            prom = round((suma_calificaciones / self.ALUMNOS), 2)
            print('Promedio de exámen {}: {}'.format(leccion_num + 1, prom))
        print('')
        for numero, alumno in enumerate(self.lista_alumnos):
            suma_calificaciones = sum(self.lista_calificaciones[numero])
            prom = round((suma_calificaciones / self.CALIF_REQUERIDAS), 2)
            print('{} su promedio es: {}'.format(alumno, prom))

        self.mayor = 0
        for leccion_num in range(6):
            suma_calificaciones = 0
            for nota in self.lista_calificaciones:
                suma_calificaciones += nota[leccion_num]
            prom = round((suma_calificaciones / self.ALUMNOS), 2)
            if self.mayor < prom:
                self.mayor = prom
            self.prom_leccion.append(prom)

    def mostrar(self):
        print('')
        print('El exámen', self.prom_leccion.index(self.mayor) + 1,'obtuvo el mayor promedio:', self.mayor)

alumnos = Info_calificaciones()
val = Validar()
alumnos.valor()
alumnos.calcular()
alumnos.mostrar()