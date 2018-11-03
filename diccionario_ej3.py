
'''Crea un programa que cuente el número de veces que aparece una palabra en una string'''

agenda = {'Hola' : 0, 'me' : 0, 'llamo' : 0, 'pepe' : 0}

string_a_contar= 'Hola Hola me me me llamo llamo llamo pepe pepe pepe'

if 'Hola' in string_a_contar:
    agenda['Hola']+= 1
if 'me' in string_a_contar:
    agenda['me'] += 1
if 'llamo' in string_a_contar:
    agenda['llamo'] +=1
if 'pepe' in string_a_contar:
    agenda['pepe'] += 1

print('Hola = {} veces'
      ' me = {} veces'
      ' llamo = {} veces'
      ' pepe = {} veces'.format(agenda['Hola'],agenda['me'],agenda['llamo'],agenda['pepe']))
