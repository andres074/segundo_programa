
'''Crea un programa que sea capaz de guardar los nombres de tus amigos y sus años de nacimiento.'''

salida = False
agenda = dict()

while not salida:
    nombre = input('Nombre: ')
    nacimiento = input('Año de nacimiento ')
    agenda[nombre] = nacimiento
    print('Datos añadidos ')
    prgunta_salida = input('¿Deseas salir? (SI) ').lower()
    if prgunta_salida == 'si':
        salida = True

print(agenda)

print('El programa ha finalizado')