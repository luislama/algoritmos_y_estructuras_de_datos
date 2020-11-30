'''
    Encontrar la suma de todos los multiplos de 3 y 5 menores a 1000
'''
suma = 0
MAX = 1000
for n in range(1, MAX):
    print(n)
    if (n % 3 == 0) or (n % 5 == 0):
        print('m')
        suma += n
print(''.join(['La suma de todos los multiplos de 3 y 5 menores a 1000 es: ', str(suma)]))
