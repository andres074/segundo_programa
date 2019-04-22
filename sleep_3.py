'''Crea un programa que pregunte al usuario que adivine un numero del 1 al 10, pero ese numero se va a
generar aleatoriamente. Hacer esperar al usuario 3 segundos antes de dar la respuesta.'''
import random
from time import sleep
while True:

    number_to_guess = random.randint(1,10)

    usser_number= input('Adivina el numero del 1 al 10 : ')
    sleep(3)
    if usser_number == number_to_guess:
        print('Felizidades , Haz ganado')
    else:
        print('Haz perdido, la respuesta correcta era {}'.format(number_to_guess))
    sleep(3)
