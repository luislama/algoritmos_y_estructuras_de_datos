'''
    Los numeros primos son 2, 3, 5, 7, 11, 13, ...
    3 es el 2do, 13 el 6to. Cual es el 10001ro numero primo ?
'''

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

primo = 2

for i in range(1, 10001):
    if(i%100==0):
        print("".join([str(i).rjust(6),": ", str(primo)]))
    primo = siguiente_primo(primo)

print("".join(["El 10001ro numero primo es : ", str(primo)]))