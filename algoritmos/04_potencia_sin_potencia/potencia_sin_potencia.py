'''
    Como se puede obtener la potencia dados la base y el exponente sin operador o funcion de potencia ?

    Limitaciones: numeros enteros positivos [0, 1, 10, 1000]
'''

escenarios = [
    [2, 0, 1],
    [5, 1, 5],
    [4, 2, 16],
    [2, 10, 1024],
]

def calcular_potencia(base, exponente, respuesta):
    potencia = 1

    def print_result():
        print("".join(['La potencia ',str(exponente), ' de ', str(base), ' es: ', str(potencia)]))

    def verificar():
        if potencia != respuesta:
            print("".join(['Error!, la potencia es: ', str(respuesta)]))

    if exponente == 0:
        print_result()
    elif exponente == 1:
        potencia = base
        print_result()
    else:
        # obtengo la potencia
        for i in range(exponente):
            potencia *= base
        print_result()
    verificar()

for prueba in escenarios:
    base, exponente, resp = prueba
    calcular_potencia(base, exponente, resp)