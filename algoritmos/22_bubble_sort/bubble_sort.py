'''
    Ordenar arreglos segun bubble_sort
    [2,7,1,5,0,4,3,8,-1,2,4]
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

