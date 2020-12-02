'''
    Encuentra la diferencia entre la suma de los cuadrados de los primeros cien numeros naturales y el cuadrado de la suma
'''

MAX = 100

suma_cuadrados = 0
suma = 0

for numero in range(1, MAX + 1):
    suma_cuadrados += numero*numero
    suma += numero

diferencia = (suma*suma) - suma_cuadrados
print("".join(["La diferencia entre la suma de los cuadrados de los primeros cien numeros naturales y el cuadrado de la suma es: ", str(diferencia)]))