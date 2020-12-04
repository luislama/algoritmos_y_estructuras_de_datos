'''
    Un serie en donde el siguiente termino es calculado de la siguiente manera:
        n2 = n1/2       ; n1 es par
        n2 = n1*3 + 1   ; n1 es impar
    No se ha probado, pero sin importar cual numero sea el primero, la serie termina en 1
        13: 13 40 20 10 5 16 8 4 2 1
        12: 6 3 10 5 16 8 4 2 1

    Que numero menor a 1 millon, produce la secuencia mas larga ?
'''

MAX = 1000000

numero = 0
secuencia = 0
for i in range(1, MAX):
    n = i
    count = 1
    while(n != 1):
        count += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    if count > secuencia:
        secuencia =  count
        numero = i
        print(str(i).rjust(2) + ": " + str(count))

print("".join(["El numero menor a 1 millon que produce la secuencia mas larga es ", str(numero), " con ", str(secuencia), " numeros" ]))