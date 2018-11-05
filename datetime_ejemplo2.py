import datetime

manana = datetime.datetime.now() + datetime.timedelta(days=1)
manana_medianche = datetime.datetime(year=manana.year, month=manana.month, day=manana.day)
hoy = datetime.datetime.now()
faltante_manana = manana_medianche - hoy

print('lo que falta para mañana son {} horas '.format(int(faltante_manana.total_seconds()/3600)))
print('Mañana es {}'.format(manana.strftime(' %d del mes %m del año %y')))

