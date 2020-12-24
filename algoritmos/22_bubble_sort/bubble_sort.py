'''
    Se recorre el arreglo elemento por elemento comparandolo con el siguiente
    Si el elemento es mayor al siguiete, estos se intercambian y se continua con el siguiente elemento
    De esta manera se hacen varios recorridos al arreglo
    Luego de terminar cada recorrido, de haber realizado al menos 1 intercambio durante este, entonces se debe hacer otro mas

    El arreglo asegura tomar el elemento mayor y colocarlo al final de manera ordenada en el arreglo en cada iteracion

    [2,7,1,5,0,4,3,8,-1,2,4]
    r1: [2,1,5,0,4,3,7,-1,2,4,8]
    r2: [1,2,0,4,3,5,-1,2,4,7,8]
    r3: [1,0,2,3,4,-1,2,4,5,7,8]
    r4: [0,1,2,3,-1,2,4,4,5,7,8]
    r5: [0,1,2,-1,2,3,4,4,5,7,8]
    r6: [0,1,-1,2,2,3,4,4,5,7,8]
    r7: [0,-1,1,2,2,3,4,4,5,7,8]
    r8: [-1,0,1,2,2,3,4,4,5,7,8]
'''

elements = [2,7,1,5,0,4,3,8,-1,2,4]
num_elements = len(elements)


def bubble_sort(arreglo):
    ordered = False
    result =  arreglo
    ronda = 1
    while not ordered:
        ordered = True
        for i in range(0, num_elements - ronda):
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
                ordered = False
        print("".join(["ronda ", str(ronda), ":"]))
        print(result)
        ronda += 1
    return result


print("arreglo: ")
print(elements)
print("\n")
ordered_elements = bubble_sort(elements)

