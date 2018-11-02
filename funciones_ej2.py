'''Escribe una funcion que dado un numero y un rango (otros dos numeros), compruebe que
ese numero está entre los dos (dentro del rango).'''

def number_in_range(primero,segundo,tercero):
    if primero in range(segundo,tercero+1):
        print('Tu número esta dentro del rango')
    else:
        print('Tu numero no esta dentro del rango')

number_in_range(2,0,10)
number_in_range(1,1,3)
number_in_range(6,2,6)
number_in_range(2,3,6)
number_in_range(9,7,8)