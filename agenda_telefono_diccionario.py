

salida = False
agenda = dict()

while not salida:
    consulta = input('¿Que acción deseas realizar? Añadir un numero (A), Consultar un numero (C),Salir (S) ')

    # Añadiendo un numero
    if consulta == 'A':
        print('Vamos a añadir un número')
        print('-------------------------')
        nombre = input('Nombre: ')
        numero = input('Numero: ')
        agenda[nombre] = numero

    # Consultando un numero:
    elif consulta == 'C':
        print('Vamos a consultar un número')
        print('-------------------------')
        nombre = input('¿De quien quieres saber el número? ')
        print(agenda[nombre])

    # Saliendo del programa
    elif consulta == 'S':
        print('Usted ha salido')
        salida = True