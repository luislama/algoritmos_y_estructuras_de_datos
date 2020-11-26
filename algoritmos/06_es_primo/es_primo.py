'''
    Como se puede saber si un numero es primo ?

    Limitaciones: numeros enteros [-1, 1, 10, 1000]
'''

escenarios = [
    [-1, 0],
    [0, 0],
    [1, 0],
    [2, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [16, 0],
    [17, 1],
    [50, 0],
    [53, 1],
]

def es_primo(numero, respuesta):
    es_primo = 0

    def print_result():
        if es_primo:
            print("".join([str(numero), ' SI es primo']))
        else:
            print("".join([str(numero), ' NO es primo']))

    def verificar():
        if es_primo != respuesta:
            if respuesta:
                print('Error! SI es primo')
            else:
                print('Error! NO es primo')

    if numero < 2:
        print_result()
    else:
        # descarto divisores
        for i in range(2, int(numero/2) + 2 ):
            if numero % i == 0 and i != numero:
                break
            elif i == int(numero/2) + 1:
                es_primo = 1

        print_result()
    verificar()

for prueba in escenarios:
    numero, resp = prueba
    es_primo(numero, resp)
