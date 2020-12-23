'''
    Ordenar arreglos segun selection_sort
    [2,7,1,5,0,4,3,8,-1,2,4]
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
