'''Antes de comenzar el while principal, preguntar al usuario si desea configurar una alarma, esta alarma sonara una vez al día a la
hora que el usuario decida (no hace falta tener los minutos en cuenta). También el usuario podrá decidir que días de la semana quiere
que esta alarma suene o si quiere que suene una fecha en concreto. Cuando llegue el momento especificado en la alarma,
simplemente escribir una nueva linea de texto en el archivo y en pantalla. Esto representaría que la alarma ha sonado.'''


from time import sleep
import datetime

NIGHT_STARTS = 19
DAY_STARTS = 8
HOUR_DURATION = 1

def spin_question(question):
    answer = input(question +'(si/no)')
    while answer.lower() != 'si' and answer != 'no':
        answer = input('¿Te gustaria poner una alarma?(si/no)')
    return answer

def write_file_and_screen(text, file_name):
    with open(file_name, "a") as hours_file:
        hours_file.write("{}{}".format(text, "\n"))
        print(text)
days_week = {'lunes':0, 'martes': 1, 'miercoles': 2, 'jueves':3,'viernes': 4, 'sábado': 5, 'domingo': 6}

def main():
    current_time = datetime.datetime.now()
    is_night = False
    day_condition = ''
    alarm_hour = 0
    date_condition = ''
    alarm_date= ''

    if spin_question('¿Quieres poner una alarma?') == 'si':
        alarm_hour = int(input('¿A que hora quiere la alarma?'))
        if spin_question('¿Quiere que sea en una fecha en especifico?') == 'si':
            alarm_date = input('¿Cual es la fecha en la que deseas que suene? (formato dd/mm/yyyy): ')
            alarm_date = datetime.datetime.strptime(alarm_date, '%d/%m/%Y')
            date_condition = True
        elif spin_question('¿Quieres que se repita algun dia en especifico') == 'si':
            alarm_day = input('¿Que dia de la semana quieres que suene?')
            day_condition = True




    while True:
        sleep(HOUR_DURATION)
        current_time += datetime.timedelta(hours=1)
        light_changed = False

        if date_condition:
            if current_time.hour == alarm_hour and current_time.day == alarm_date.day and current_time.month == alarm_date.month:
                write_file_and_screen("Ha sonado la alarma", "horas.txt")



        elif day_condition:
            if current_time.hour == alarm_hour and current_time.weekday() == days_week[alarm_day]:
                write_file_and_screen("Ha sonado la alarma", "horas.txt")

        elif current_time.hour == alarm_hour:
            write_file_and_screen("Ha sonado la alarma", "horas.txt")


        if (current_time.hour >= NIGHT_STARTS or current_time.hour <= DAY_STARTS) and not is_night:
            is_night = True
            light_changed = True

        elif (current_time.hour > DAY_STARTS and current_time.hour < NIGHT_STARTS) and is_night:
            is_night = False
            light_changed = True

        if light_changed:
            if is_night:
                write_file_and_screen("Se ha hecho de noche", "horas.txt")
            else:
                write_file_and_screen("Se ha hecho de día", "horas.txt")

        write_file_and_screen("La hora actual es {}".format(current_time), "horas.txt")


if __name__ == "__main__":
    main()