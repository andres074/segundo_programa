
'''Crea una función que muestre por pantalla un texto y tantas barritas de subrayado como larga
sea la string.'''

def rallitas_string(string_usuario):
    for letra in string_usuario:
        string_usuario = string_usuario.replace(letra, '-')
    return string_usuario

oracion = input('Elige la oración que quieres cambiar')

print(oracion)
print(rallitas_string(oracion))
