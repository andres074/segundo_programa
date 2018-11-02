'''Escribe una función que reciba una lista de números y devuelva otra pero conteniendo solo los números pares.'''

def lista_numeros_pares(numeros):
    numeros_pares= []
    for numero in numeros:
        if numero % 2 ==0:
            numeros_pares.append(numero)
    return numeros_pares

print(lista_numeros_pares([2,1,5,4,6,546,12,8,18,1,6,5,495,]))


