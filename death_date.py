
import datetime
import random

MAX_LIFESPAN = 100

SMOKER_PENALIZATION = 10
DRINKER_PENALIZATION = 7
SEDENTARI_PENALIZATION = 3
BAD_NUTRITION = 10
CITY_CONTAMINATION = 15

days_week = {0: 'lunes', 1: 'martes', 2: 'miercoles', 3: 'jueves', 4: 'viernes', 5: 'sábado', 6: 'domingo'}

def str_with_underscore(message):
    print(message)
    print(len(message) * '-')

def spin_question(question):
    answer = input(question + '(si/no/tal vez) ')
    years_to_lost = 0
    while answer.lower() != 'si' and answer.lower() != 'no' and answer.lower() != 'tal vez':
        answer = input(question + '(si/no/tal vez) ')
    if answer.lower() == 'si':
        years_to_lost += DRINKER_PENALIZATION
    elif answer.lower() == 'tal vez':
        years_to_lost += DRINKER_PENALIZATION/2
    return years_to_lost

str_with_underscore('Vamos a descubrir el día de tu muerte')

birthday_date = input('¿Cual es tu fecha de nacimiento? (formato dd/mm/yyyy): ')
birthday_date = datetime.datetime.strptime(birthday_date, '%d/%m/%Y')
edad_actual = datetime.datetime.now() - birthday_date

years_lost = 0
years_lost += spin_question('¿ingieres bebidas alcoholicas? ')
years_lost += spin_question('¿Fumas? ')
years_lost += spin_question('¿Haces ejercisio?')
years_lost += spin_question('¿Te alimentas de una manera correcta?')
years_lost += spin_question('¿Vives en un ambiente rodeado de contaminacíon?')

if not edad_actual.days/365 > 40:
    base_lifespan = random.randint(MAX_LIFESPAN/2, MAX_LIFESPAN)
else:
    base_lifespan = random.randint(int(edad_actual.days/365), MAX_LIFESPAN)
lifespan = base_lifespan - years_lost
date_death = birthday_date + datetime.timedelta(days=lifespan * 365)
days_left = date_death - datetime.datetime.now()

print('La fecha de tu muerte sera {},tus dias restantes son {}, el día de tu partida sera el  {} '.format(date_death.strftime('%d/%m/%Y'), days_left.days,days_week[date_death.weekday()]))
