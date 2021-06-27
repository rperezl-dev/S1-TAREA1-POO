#Ejemplo 5
#Dado como dato la calificación de un alumno en un examen, escriba “aprobado” si su calificación es mayor o igual
# que 7 y “Reprobado” en caso contrario.

class Examen:
    def __init__(self):
        self.calificacion=float

    def calificacion_exam(self):
        try:
            calificacion = float(input('Ingrese la califacion del examen: '))
            if calificacion >= 7:
                print('Alumno aprobado con ', calificacion)
            else:
                print('Alumno reprobado con', calificacion)
        except:
            print('Error, ingrese solo valores númericos.')

Miexamen=Examen()
Miexamen.calificacion_exam()