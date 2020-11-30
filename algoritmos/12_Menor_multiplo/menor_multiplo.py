'''
    Cual es el minimo comun multiplo de los numeros 1, 2, 3, ... 20
'''
multiplo = 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
factores = []


def es_primo(numero):
    #if numero < 2 :
    if numero < 2:
        return False
    elif numero in [2,3]:
        return True
    else:
        aux = 2
        mitad = numero/2
        while(aux <= mitad):
            if numero % aux == 0:
                return False
            aux += 1
    return True

def siguiente_primo(numero):
    aux = numero + 1
    while not es_primo(aux):
        aux += 1
    return aux

def verificar(numeros):
    for i in numeros:
        if i != 1:
            return False
    return True

factor_primo = 2

while not verificar(numeros):
    add = False
    for i in range(0, len(numeros)):
        if numeros[i] == 1:
            continue
        if numeros[i] % factor_primo == 0:
            numeros[i] /= factor_primo
            if not add:
                add = True
    if add:
        print(numeros)
        multiplo *= factor_primo
    else:
        factor_primo = siguiente_primo(factor_primo)

print(''.join(['El multiplo menor de los numeros del 1 al 20 es: ', str(multiplo)]))