'''
    Como se puede obtener la diferencia de 2 numeros sin restar ?

    Limitaciones: numeros enteros [0, 1, -2, 1000]
'''

escenarios = [
    [1, 5, 4],
    [1, 1, 0],
    [-1, -10, 9],
    [10, -1, 11],
]

def calcular_differencia(num1, num2, respuesta):
    diferencia = 0

    def print_result():
        print("".join(['La diferencia entre ',str(num1), ' y ', str(num2), ' es: ', str(diferencia)]))

    def verificar():
        if diferencia != respuesta:
            print("".join(['Error!, la diferencia es: ', respuesta]))

    # hay diferencia ?
    if num1 == num2:
        print_result()
    else:
        # obtengo diferencia
        minimo = min([num1, num2])
        maximo = max([num1, num2])
        diferencia = 0
        while(minimo + diferencia != maximo):
            diferencia += 1
        print_result()
    verificar()

for prueba in escenarios:
    num1, num2, resp = prueba
    calcular_differencia(num1, num2, resp)