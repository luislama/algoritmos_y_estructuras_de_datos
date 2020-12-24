'''
    24_jose_javier_villena_sort
    Recorrer el arreglo buscando las posiciones de los numeros mayor y menor
    Al finalizar cada iteracion colocar los numeros al principio y al final, intercambiando los numeros
    Luego de cada vuelta, las posiciones a recorrer disminuyen en 2, puesto que los extremos ya han sido examinados

    [2,7,1,5,0,4,3,8,-1,2,4]
    r1: [-1,7,1,5,0,4,3,4,2,2,8]
    r2: [-1,0,1,5,2,4,3,4,2,7,8]
    r3: [-1,0,1,2,2,4,3,4,5,7,8]
    r4: [-1,0,1,2,2,4,3,4,5,7,8]
    r5: [-1,0,1,2,2,3,4,4,5,7,8]
'''

elements = [2,7,1,5,0,4,3,8,-1,2,4]
num_elements = len(elements)

def jose_javier_villena_sort(arreglo):
    ordered = False
    result =  arreglo
    ronda = 1
    i = 0
    j = len(result) - 1
    while i < j - 1:
        min = i
        max = j
        for k in range(i, j):
            if result[k] < result[min]:
                min = k
            if result[k] > result[max]:
                max = k
        if min != i or max != j:
            if min == j and max == i:
                result[i], result[j] = result[j], result[i]
            elif max == i and min != j:
                result[i], result[min], result[j] = result[min], result[j], result[i]
            elif max != i and min == j:
                result[i], result[max], result[j] = result[j], result[i], result[max]
            elif max != i and min != j:
                result[i], result[min], result[j], result[max] = result[min], result[i], result[max], result[j]
            else:
                pass

        print("".join(["ronda ", str(ronda), ":"]))
        print(result)
        print('\n')

        i += 1
        j -= 1
        ronda += 1

print("arreglo: ")
print(elements)
print("\n")
ordered_elements = jose_javier_villena_sort(elements)