
'''Crea un programa que te diga la fecha de hace 5 días respecto a hoy, y el día de la semana.'''
import datetime

pasado_5dias = datetime.datetime.now() - datetime.timedelta(days=5)

dias = {0: 'lunes', 1: 'martes', 2: 'miercoles', 3: 'jueves', 4: 'viernes', 5: 'sabado', 6: 'domingo'}

print(' Hace 5 días fue {} y calló en {}'.format(pasado_5dias.strftime('%d del mes %m del año %y'), dias[pasado_5dias.weekday()]))
