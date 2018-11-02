
def input_usuario_con_confirmacion(pregunta):
    confirmacion= False
    dato_usuario = ''
    while not confirmacion:
        dato_usuario = input(pregunta)
        confirmacion_usuario = input('Haz dicho {}, ¿estas seguro? (Si/No) '.format(dato_usuario))
        if confirmacion_usuario == 'Si':
            confirmacion = True
    return dato_usuario

nombre = input_usuario_con_confirmacion('¿Cuál es tu nombre?')
print('Tu nombre es {}'.format(nombre))

numero = input_usuario_con_confirmacion('Elige un numero')
print('El numero que elegiste es {}'.format(numero))
      
