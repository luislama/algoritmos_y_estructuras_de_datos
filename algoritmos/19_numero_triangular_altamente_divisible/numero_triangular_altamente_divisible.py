'''
    Los numeros triangulares se obtienen de sumar los numeros naturales
    el 7mo numero triangular es 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28

    La lista de los factores de los numeros triangulares es:
         1: 1
         3: 1, 3
         6: 1, 2, 3, 6
        10: 1, 2, 5, 10
        15: 1, 3, 5, 15
        21: 1, 3, 7, 21
        28: 1, 2, 4, 7, 14, 28
        ...
    El 28 tiene mas de 5 divisores
    Cual es el menor numero triangular con mas de 500 divisores ?
'''

'''
    Analisis
    Como ejemplo tenemos el 12
    1 2 3 4 5 6 7 8 9 10 11 12
    - 1 y 12 son divisores naturales -> debemos revisar 2 3 4 5 6 7 8 9 10 11
    - el mayor divisor de 12 sera la mitad, en caso de tener mitad -> debemos revisar del 2 3 4 5 6

    Aun con este acercamiento, intentar revisar numeros grandes, representa un problema por la cantidad de numeros
    se puede usar una estructura para ir almacenando los divisores encontrados

    Se debe encontrar la manera de ir reduciendo la lista de numeros a revisar
    Al encontrar un numero que es divisor, buscamos inmediatamente el otro divisor, cuyo producto es el numero:
        12 es divisible para 2, 12/2 = 6 -> esto nos da 2 numeros que son divisores

    Encontre una ultima optimizacion que es disminuir el tope
    numero 24
        numeros a revisar 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
    quitando 1 y 24
        numeros a revisar 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
    pensando en que el maximo divisor posible es la mitad
        numeros a revisar 2 3 4 5 6 7 8 9 10 11 12
    Iteramos y empezamos a revisar
        i: 2
            numeros por revisar 3 4 5 6 7 8 9 10 11 12
            24 % 2 = 0 -> agregamos 2 y 12
            max: 12 - 1
            i: i + 1
        i: 3
            numeros por revisar 4 5 6 7 8 9 10 11
            24 % 3 = 0 -> agregamos 3 y 8
            max: 8 - 1
            i: i + 1
        i: 4
            numeros por revisar 5 6 7
            24 % 4 = 0 -> agregamos 4 y 6
            max: 6 - 1
            i: i + 1
        itr: 5
            numeros por revisar: NINGUNO
            24 no es divisible para 5
        ya no quedan numeros que revisar

    El algoritmo reduce la cantidad de numeros a revisar de 24 a 4, teniendo un gran impacto en el rendimiento

    **Al final agregue un filtro de numeros pares, por alguna razon, me es dificil creer que un numero impar tenga mas divisores que uno par, siendo estos numeros "cercanos"
'''

num_factores = 0
MAX = 500

natural = 1
triangular = 0

cociente = 144

def calcular_numero_factores(numero):
    divisores = [1, numero]
    if numero == 1:
        return 1
    max = int(numero/2) + 1
    i = 2
    while i < max:
        if i not in divisores and numero % i == 0:
            divisores.append(i)
            divisores.append(numero/i)
            max = numero/i
        i += 1
    return len(divisores)

while num_factores <= MAX:
    triangular += natural
    aux_num_factores = calcular_numero_factores(triangular)
    natural += 1
    if triangular % 2 != 0:
        continue
    if aux_num_factores > num_factores:
        num_factores =  aux_num_factores
        print("".join([str(triangular), ': ', str(aux_num_factores), ' divisores']))
print("".join(['El menor numero triangular con mas de 500 divisores es ', str(triangular), ' y tiene ', str(aux_num_factores), ' divisores']))