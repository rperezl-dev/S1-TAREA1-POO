#Ejemplo 4
#Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen, presente un alumno aprueba
# si la calificación es mayor o igual que 7

class Examen():
    def __init__(self):
        self.calificacion=float

    def calificacion_exam(self):
        try:
            calificacion = float(input('Ingrese la califacion obtenida en el examen: '))
            if calificacion >= 7:
                print('¡Alumno aprobado!')
            else:
                print('¡Alumno Reprobado!')
        except:
            print('Error, ingrese solo valores númericos.')

Miexamen=Examen()
Miexamen.calificacion_exam()