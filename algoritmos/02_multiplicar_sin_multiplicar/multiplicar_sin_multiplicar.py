'''
    Como se puede obtener el producto de 2 numeros sin multiplicar ?

    Limitaciones: numeros enteros positivos [0, 1, 10, 1000]
'''

escenarios = [
    [2, 3, 6],
    [5, 10, 50],
    [0, 6, 0],
]

def calcular_producto(num1, num2, respuesta):
    producto = 0

    def print_result():
        print("".join(['El producto entre ',str(num1), ' y ', str(num2), ' es: ', str(producto)]))

    def verificar():
        if producto != respuesta:
            print("".join(['Error!, el producto es: ', respuesta]))

    # uno de los 2 es cero ?
    if 0 in [num1, num2]:
        print_result()
    else:
        # obtengo el producto
        for i in range(num2):
            producto += num1
        print_result()
    verificar()

for prueba in escenarios:
    num1, num2, resp = prueba
    calcular_producto(num1, num2, resp)
