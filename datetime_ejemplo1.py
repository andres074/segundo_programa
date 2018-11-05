
import datetime

year = int(input('¿Cual es el año?'))
month = int(input('¿Cual es el mes?'))
day = int(input('¿Cual es el día ?'))

usser_date = datetime.datetime(year=year, month=month, day=day)

time_remainig= usser_date - datetime.datetime.now()

print('El tiempo restante para esa fecha es {} días y {} horas '.format(time_remainig.days, int(time_remainig.seconds/3600)))
print('mañana es {}'.format(datetime.datetime.now()+datetime.timedelta(days=1)))
