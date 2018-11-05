'''Crea un programa que te diga cuando falta para tu cumpleaños y que día de la semana será.'''
import datetime

year = int(input('¿En que año cae tu siguiente cumpleaños?'))
month = int(input('¿En que mes cumples años?'))
day = int(input('¿En que dia cumples años?'))
usser_date = datetime.datetime(year = year,month=month,day=day)
time_remaining = usser_date - datetime.datetime.now()
total_time = datetime.datetime.now() + time_remaining
dias = {0: 'lunes', 1: 'martes', 2: 'miercoles', 3: 'jueves', 4: 'viernes', 5: 'sabado', 6: 'domingo'}

print('Para tu cumpleaños faltan {} dias y {} horas  y caera en {}  '.format(time_remaining.days, int(time_remaining.seconds/3600),dias[total_time.weekday()]))