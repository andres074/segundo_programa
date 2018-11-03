
'''Crea un programa que al decirle el nombre de un color nos devuelva su traducción en inglés'''

traduccion_colores = {'rojo' : 'red','amarillo': 'yellow', 'rosa' : 'pink', 'negro' : 'black', 'azul' : 'blue', 'verde' : 'green',
                      'morado' : 'purple', 'cafe' : 'brown', 'blanco' : 'white'}

color = input('¿Que color quieres traducir a ingles? ').lower()
print(traduccion_colores[color])
