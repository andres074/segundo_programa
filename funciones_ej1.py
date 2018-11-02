'''Escribe una función que encuentre el numero más grande entre 3 numeros.'''

def numero_mayor(primero,segundo,tercero):
    numero_grande = primero
    if numero_grande < segundo:
        numero_grande = segundo
    if numero_grande < tercero:
        numero_grande = tercero
    return numero_grande
print(numero_mayor(2,4,6))
print(numero_mayor(6,7,8))
print(numero_mayor(1231,545,6364,))
print(numero_mayor(9,9,9))

