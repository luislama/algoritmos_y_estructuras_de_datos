'''
    Encontrar la suma de todos los numeros pares en la serie de Fibonacci, menores a 4 millones
'''
suma = 0
MAX = 4000000
n1 = 1
n2 = 1
#print(n1)
while(n2 < MAX):
    #print(n2)
    if (n2 % 2 == 0):
        suma += n2
    n1, n2 = n2, n1 + n2


print(''.join(['La suma de todos los numeros pares en la serie de Fibonacci, menores a 4 millones es: ', str(suma)]))
