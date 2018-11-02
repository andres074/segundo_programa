'''Escribe una función que te devuelva una string asignada al revez'''

def reverse_string(string_to_reverse):
    new_string = ''
    letter_posicion = len(string_to_reverse)-1
    while letter_posicion >=0:
        new_string += string_to_reverse[letter_posicion]
        letter_posicion -= 1
    return new_string


print(reverse_string('Hola mundo'))
print(reverse_string('Me llamo Juan'))
print(reverse_string('Me pica la nalga'))
print(reverse_string('Me la pelan los programadores'))
print(reverse_string('La neta esta madre esta chingon'))
