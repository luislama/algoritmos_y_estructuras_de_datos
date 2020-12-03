'''
    Existe un triple pitagorico en donde a + b + c = 1000
    Triple Pitagorico:
        a < b < c
        a^2 + b^2 = c^2
    Encuentre el producto de los 3 numeros
'''

'''
    Analisis:

    trabajando las ecuaciones se puede llegar a la siguiente expresion:
    [1]: a^2 + b^2 = c^2
    [2]: a + b + c = 1000  ->  c^2 = (1000 - (a + b))^2
    reemplazamos c^2  de [2] en [1]:
        a^2 + b^2 = (1000 - (a + b))^2
        ...
        500000 - 1000*(a+b) + (a*b) = 0  ->  [COND]
    Se utilizara la condicion para encontrar el triple pitagorico
'''

MAX = 1000

numeros = [0]*3

def cumple_condiciones(numeros):
    if (len(numeros) != 3) or (0 in numeros):
        return False
    a, b, c = numeros
    if (500000 - 1000*(a+b) + (a*b)) == 0:
        return True

a = 1
while not cumple_condiciones(numeros):
    for b in range(a + 1, MAX):
        numeros = [a, b, 1]
        if cumple_condiciones(numeros):
            break
        b += 1
    a += 1

numeros[2] = 1000 - numeros[0] - numeros[1]
a, b, c = numeros
print("".join(["Triple pitagorico: ", str(a), ", ", str(b), ", ", str(c)]))
print("".join(["  ", str(a), " + ", str(b), " + ", str(c), " = 1000", "  ->  ", str(sum(numeros) == 1000)]))
print("".join(["  ", str(a), "^2 + ", str(b), "^2 = ", str(c), "^2\n", \
                "    ->  ", str(a**2), " + ", str(b**2), " = ", str(c**2), "\n", \
                "    ->  ", str(a**2 + b**2), " = ", str(c**2), "\n", \
                "    ->  ", str(a**2 + b**2 == c**2)]))
print("".join(["  ", str(a), " x ", str(b), " x ", str(c), " = ", str(a*b*c)]))
