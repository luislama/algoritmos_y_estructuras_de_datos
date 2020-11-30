'''
    Encuentra el numero palindromo mayor formado por el producto de dos numeros de 3 digitos
'''

aux = 999
nums = []

def es_palindromo(numero):
    num_str = str(numero)
    return str(numero) == num_str[::-1]

palindromo = -1

producto = -1
buscando = True
while aux > 99:
    if palindromo != -1 and aux**2 < palindromo:
            break
    aux2 = aux
    while(aux2 > 99):
        producto = aux * aux2
        if palindromo != -1 and producto < palindromo:
            break
        if es_palindromo(producto):
            if producto > palindromo:
                print(''.join([str(aux), ' * ', str(aux2), ' = ', str(producto)]))
                nums = [aux, aux2]
                palindromo = producto
            break
        aux2 -= 1
    aux -= 1

print(''.join(['El numero palindromo mas grande formado del producto de dos numeros de 3 digitos es: ', str(palindromo)]))
print(''.join([str(nums[0]), ' * ', str(nums[1]), ' = ', str(palindromo)]))
