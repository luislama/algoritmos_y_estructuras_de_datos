'''
    Encuentre el producto mayor entre 4 numeros adyacentes (arriba, abajo y en diagonal) en la matriz de 20x20
'''

matriz = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 ' + \
        '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 ' + \
        '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 ' + \
        '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 ' + \
        '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 ' + \
        '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 ' + \
        '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 ' + \
        '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 ' + \
        '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 ' + \
        '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 ' + \
        '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 ' + \
        '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 ' + \
        '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 ' + \
        '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 ' + \
        '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 ' + \
        '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 ' + \
        '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 ' + \
        '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 ' + \
        '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 ' + \
        '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

def producto_numeros(arreglo_numeros):
    if 0 in arreglo_numeros:
        return 0
    producto = 1
    for num in arreglo_numeros:
        producto *= num
    return producto

dimensiones = [20, 20]
numeros_adyacentes = 4
arr2x2 = []

fila = []
row = ""
for i, n in enumerate(matriz.split()):
    fila.append(int(n))
    row += n
    if (i + 1) % 20 == 0:
        arr2x2.append([el for el in fila])
        fila = []
        row += "\n"
        print(row)
        row = ""
    else:
        row += " "

numeros = []
producto = 1
tipo = ''
pos_en_matriz = []

def cambiar_respuesta(aux_numeros, aux_producto, aux_tipo, aux_pos_en_matriz):
    global numeros
    global producto
    global tipo
    global pos_en_matriz
    numeros = [num for num in aux_numeros]
    producto = aux_producto
    tipo = aux_tipo
    pos_en_matriz = aux_pos_en_matriz

def calcular_producto_respuesta(aux_numeros, aux_tipo, aux_pos_en_matriz):
    producto_aux_numeros = producto_numeros(aux_numeros)
    if producto_aux_numeros > producto:
        cambiar_respuesta(aux_numeros, producto_aux_numeros, aux_tipo, aux_pos_en_matriz)

if numeros_adyacentes < dimensiones[0] or numeros_adyacentes < dimensiones[1]:
    for num_fila, fila in enumerate(arr2x2):
        for pos_en_fila in range(1, len(fila) + 1):
            horizontal = pos_en_fila <= dimensiones[0] - numeros_adyacentes + 1
            vertical = num_fila <= dimensiones[1] - numeros_adyacentes
            aux_numeros = []
            if horizontal:
                aux_numeros = fila[(pos_en_fila - 1):(pos_en_fila + numeros_adyacentes -1)]
                calcular_producto_respuesta(aux_numeros, 'horizontal', [num_fila, pos_en_fila - 1])
            if vertical:
                aux_numeros = []
                for aux_num_fila in range(num_fila, num_fila + numeros_adyacentes):
                    aux_numeros.append(arr2x2[aux_num_fila][pos_en_fila - 1])
                calcular_producto_respuesta(aux_numeros, 'vertical', [num_fila, pos_en_fila - 1])
            if horizontal and vertical:
                aux_numeros = []
                count = 0
                for aux_num_fila in range(num_fila, num_fila + numeros_adyacentes):
                    aux_numeros.append(arr2x2[aux_num_fila][pos_en_fila + count - 1])
                    count += 1
                calcular_producto_respuesta(aux_numeros, 'diagonal abajo', [num_fila, pos_en_fila - 1])
            if (pos_en_fila <= dimensiones[0] - numeros_adyacentes + 1) and (num_fila >= numeros_adyacentes - 1):
                aux_numeros = []
                count = 0
                for aux_num_fila in range(num_fila, num_fila - numeros_adyacentes, -1):
                    aux_numeros.append(arr2x2[aux_num_fila][pos_en_fila + count - 1])
                    count += 1
                calcular_producto_respuesta(aux_numeros, 'diagonal arriba', [num_fila, pos_en_fila - 1])
else:
    print('las dimensiones del arreglo son menores a la cantidad de numeros adyacentes a buscar')


print("".join(["El producto mayor de ", str(numeros_adyacentes), " numeros adyacentes es : ", str(producto)]))
print("".join(["  posicion: ", str(pos_en_matriz)]))
print("".join(["  tipo:     ", tipo]))
print("".join(["  numeros : ", str(numeros)]))