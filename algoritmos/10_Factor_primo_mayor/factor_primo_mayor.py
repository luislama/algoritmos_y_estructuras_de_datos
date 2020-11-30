'''
    Cual es el factor primo mayor del numero 600851475143
'''
NUM = 600851475143

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

'''
todo numero puede ser descompuesto en un producto de numeros primos
'''
producto = 1
factor_primo = 2
temp = NUM

while(producto != NUM):
    while temp % factor_primo == 0:
        print(factor_primo)
        temp = NUM/factor_primo
        producto *= factor_primo
    if producto == NUM:
        break
    factor_primo = siguiente_primo(factor_primo)

print(''.join(['el factor primo mayor del numero ', str(NUM), ' es: ', str(factor_primo)]))
