
'''Crea un programa que te diga, introduciendo cualquier fecha, cuantas horas han pasado desde ese momento.

'''

import datetime

year = int(input('¿Introduce año?'))
month = int(input('¿introduce mes?'))
day = int(input('¿introduce dia ?'))
usser_date = datetime.datetime(year = year,month=month,day=day)
time_past = datetime.datetime.now() - usser_date

print('Han pasado {} horas'.format(int(time_past.total_seconds()/3600)))