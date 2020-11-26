'''
    Como se puede obtener el cociente de 2 numeros sin dividir ?

    Limitaciones: numeros enteros positivos [0, 1, 10, 1000]
'''

escenarios = [
    [6, 3, 2],
    [50, 10, 5],
    [0, 6, 0],
    [7, 7, 1],
]

def calcular_cociente(dividendo, divisor, respuesta):
    cociente = 0

    def print_result():
        print("".join(['El cociente entre ',str(dividendo), ' y ', str(divisor), ' es: ', str(cociente)]))

    def verificar():
        if cociente != respuesta:
            print("".join(['Error!, el producto es: ', respuesta]))

    if dividendo == 0  and divisor == 0:
        print("No se considera este escenario. 0 dividido para 0 es indeterminado")
    elif divisor == 0:
        print("No se considera este escenario. La division para 0 es indeterminada")
    elif dividendo == 0:
        print_result()
    elif dividendo == divisor:
        cociente = 1
        print_result()
    else:
        # obtengo cociente
        cociente = 1
        while(cociente * divisor < dividendo):
            cociente += 1
        print_result()
    verificar()

for prueba in escenarios:
    num1, num2, resp = prueba
    calcular_cociente(num1, num2, resp)
