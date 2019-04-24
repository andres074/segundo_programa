'''Escribe un programa que imprima por pantalla una frase aleatoria cada segundo.
La lista de frases de la que se seleccionará la frase aleatoria será distinta según el segundo en el que estemos:'''

import random
from time import sleep
strings_dicc = {1 : ['Estoy feliz','Viva la vida','Disfruta cada momento', 'Se Feliz','Viva con felicidad', 'Todo va de maravilla']
    ,2 : ['silla','mueble','mesa', 'servilletero','comoda', 'cama'], 3 :['fanta','limonada','cocacola', 'Horchata','Cuba', 'Sex on the beach']
    , 4 :['te odio','te voy a matar','me cagas', 'asco tu programa','te desprecio', 'me enervas'], 5: ['Mole','Pozole','Tacos', 'Pizza','Arrachera', 'Ceviche']
    , 6:['caca','culo','pedo', 'pis','bazinga', 'wabalabadubdub'], 7 : ['perro','gato','tigre', 'leon','elefante', 'jaguar']
    , 8 : ['vamos','tu puedes','con tokio', 'metele','si no vas por todo ¿A que vas?', 'Nunca te rindas']
    ,9 :['miau','guau','pio', 'muuu','kikiriki', 'brrr'], 10 :['miau','guau','pio', 'muuu','kikiriki', 'brrr']}


current_number = 1
while True:
    print(strings_dicc[current_number][random.randint(0,5)])
    current_number += 1
    sleep(1)
    if current_number > 10:
        current_number = 1







