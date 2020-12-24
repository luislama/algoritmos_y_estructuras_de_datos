'''
    Se recorre el arrego elemento por elemento, buscando la posicion del menor elemento entre los siguientes que faltan por recorrer
    Luego de terminar de revisar los elementos siguientes, y obtener la posicion del menor de ellos, comparo el elemento en esa posicion con el de la posicion actual
    De ser mayor el elemento en la posicion actual, se intercambian estos elementos
    Al terminar el recorrido, elemento por elemento, termina el algoritmo

    El arreglo asegura tomar el elemento menor y colocarlo al principio de manera ordenada en el arreglo en cada iteracion

    [2,7,1,5,0,4,3,8,-1,2,4]
    r1: [-1,7,1,5,0,4,3,8,2,2,4]
    r2: [-1,0,1,5,7,4,3,8,2,2,4]
    r3: [-1,0,1,5,7,4,3,8,2,2,4]
    r4: [-1,0,1,2,7,4,3,8,5,2,4]
    r5: [-1,0,1,2,2,4,3,8,5,7,4]
    r6: [-1,0,1,2,2,3,4,8,5,7,4]
    r7: [-1,0,1,2,2,3,4,8,5,7,4]
    r8: [-1,0,1,2,2,3,4,4,5,7,8]
    r9: [-1,0,1,2,2,3,4,4,5,7,8]
    r10: [-1,0,1,2,2,3,4,4,5,7,8]
'''

elements = [2,7,1,5,0,4,3,8,-1,2,4]
num_elements = len(elements)


def selection_sort(arreglo):
    ordered = False
    result =  arreglo
    ronda = 1
    for i in range(0, num_elements - 1):
        min = i
        for j in range(i+1, num_elements):
            if result[j] < result[min]:
                min = j
        if min != i:
            result[i], result[min] = result[min], result[i]
        print("".join(["ronda ", str(ronda), ":"]))
        print(result)
        ronda += 1

print("arreglo: ")
print(elements)
print("\n")
ordered_elements = selection_sort(elements)
