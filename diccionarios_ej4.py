
'''Crea una función que muestre por pantalla un texto y tantas barritas de subrayado como larga
sea la string.'''

def rallitas_string(string_usuario):
    string_rallitas = ''
    for letra in string_usuario:
        string_rallitas += '-'
    print(string_usuario)
    print(string_rallitas)

oracion = input('Elige la oración que quieres cambiar ')

rallitas_string(oracion)
