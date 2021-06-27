#Ejemplo 10
#Un ejemplo en el cual usamos el operador lógico AND sería:
#Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas
# como C1 y C2. El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario
# es rechazado.

class Escuela():
    def __init__(self):
        pass
    def examen(self):
        try:
            C1=float(input('Ingrese la calificacion obtenida en el primer examen: '))
            C2=float(input('Ingrese la calificacion obtenida en el segundo examen: '))
            if (C1>=80 and C2>=80):
                print('¡Aceptado!')
            else:
                print('¡Rechazado!')
        except:
            print('Error, ingrese solo valores númericos.')

Miescuela=Escuela()
Miescuela.examen()


#Un ejemplo usando el operador lógico OR sería:
#Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones denotadas
# como C1 y C2. El aspirante que obtenga una calificación mayor que 90 en cualquiera de los exámenes es aceptado;
# en caso contrario es rechazado.

class Escuela:
    def __init__(self):
        pass
    def examen(self):
        try:
            C1=float(input('Ingrese la calificacion obtenida en el primer examen: '))
            C2=float(input('Ingrese la calificacion obtenida en el segundo examen: '))
            if (C1>=90 or C2>=90):
                print('¡Aceptado!')
            else:
                print('¡Rechazado!')
        except:
            print('Error, ingrese solo valores númericos.')

Miescuela=Escuela()
Miescuela.examen()