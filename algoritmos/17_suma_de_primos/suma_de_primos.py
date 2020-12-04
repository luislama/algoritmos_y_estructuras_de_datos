'''
    Encuentre la suma de los numeros primos menores a 2 millones
'''

'''
Analisis

    Anteriormente, el numero primo mayor a calcular fue el 10001, el algoritmo de buscar los numeros primos no era eficiente,
    pero no representaba un problema

    En este caso, el tope es de 2000000 y necesita otro enfoque
    Se utiliza un arreglo para ir almacenando los numeros primos, sin embargo no es suficiente

    Investigando, se encuentra un metodo que evita el tener que verificar si cada numero es primo dentro de la serie
    Se utiliza un arreglo para marcar los numeros no primos dentro de la serie, y al avanzar por el arreglo, aquellos que
    no estan marcados, son primos
    0 1 2 3 4 5 6 7 8 9 10
    1 1 0 0 1 0 1 0 1 1  1

    0 no es primo

    1 no es primo

    2 si es primo, encuentro sus multiplos dentro de la serie
    2 4 6 8 10
    0 1 2 3 4 5 6 7 8 9 10
    1 1 0 0 1 0 1 0 1 0  1

    3 no esta marcado, es primo, encuentro sus multiplos
    3 9
    0 1 2 3 4 5 6 7 8 9 10
    1 1 0 0 1 0 1 0 1 1  1

    de esta manera, tachando los multiplos que son faciles de calcular, se pueden sumar los primos sin necesidad de hacer la verificacion
    se necesita el arreglo de 2000001 elementos
'''

MAX = 2000000

numeros = [0]*(MAX + 1)
numeros[0] = 1
numeros[1] = 1

suma_de_primos = 0

for i in range(MAX + 1):
    if numeros[i] == 0:
        suma_de_primos += i
        for mult in range(i, int(MAX/i) + 1):
            numeros[i * mult] = 1

print("".join(["La suma de los numeros primos menores a ", str(MAX), " es: ", str(suma_de_primos)]))
