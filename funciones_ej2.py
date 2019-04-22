'''Escribe una funcion que dado un numero y un rango (otros dos numeros), compruebe que
ese numero está entre los dos (dentro del rango).'''

def number_in_range(primero,segundo,tercero):
    if primero in range(segundo,tercero+1):
        resultado= True
    else:
        resultado = False
    return resultado

print(number_in_range(2,0,10))
print(number_in_range(3,1,3))
print(number_in_range(6,2,6))
print(number_in_range(2,3,6))
print(number_in_range(9,7,8))