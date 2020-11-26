'''
    Como se puede saber si un numero es primo ?

    Limitaciones: numeros enteros [-1, 1, 10, 1000]
'''

escenarios = [
    [1, 0],
    [2, 0],
    [6, 1],
    [8, 0],
    [28, 1],
    [496, 1],
    [8128, 1],
    [9000, 0],
]

def es_perfecto(numero, respuesta):
    es_perfecto = 0
    acumulador = 0

    def print_result():
        if es_perfecto:
            print("".join([str(numero), ' SI es perfecto']))
        else:
            print("".join([str(numero), ' NO es perfecto']))

    def verificar():
        if es_perfecto != respuesta:
            if respuesta:
                print('Error! SI es perfecto')
            else:
                print('Error! NO es perfecto')

    if numero < 6:
        print_result()
    else:
        # descarto divisores
        for i in range(1, int(numero/2) + 2 ):
            if numero % i == 0 and i != numero:
                acumulador += i
                if acumulador > numero:
                    break
        if acumulador == numero:
            es_perfecto = 1
        print_result()
    verificar()
print('Un numero perfecto es aquel cuyos divisores propios al sumarse obtienen el mismo numero como resultado.')
for prueba in escenarios:
    numero, resp = prueba
    es_perfecto(numero, resp)
