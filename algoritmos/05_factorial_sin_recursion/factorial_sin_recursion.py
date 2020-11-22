'''
    Como se puede obtener el factorial de un numero ?

    Limitaciones: numeros enteros positivos [0, 1, 10, 1000]
'''

escenarios = [
    [0, 1],
    [1, 1],
    [3, 6],
    [5, 120],
]

def calcular_factorial(numero, respuesta):
    factorial = 1

    def print_result():
        print("".join(['El factorial de ',str(numero), ' es: ', str(factorial)]))

    def verificar():
        if factorial != respuesta:
            print("".join(['Error!, la potencia es: ', str(respuesta)]))

    if numero in [0, 1]:
        print_result()
    else:
        # obtengo la potencia
        for i in range(numero):
            factorial *= i + 1
        print_result()
    verificar()

for prueba in escenarios:
    numero, resp = prueba
    calcular_factorial(numero, resp)