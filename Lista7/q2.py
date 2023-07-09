#q2
import math

def area_do_circulo(raio):
    area = math.pi * (raio ** 2)
    return area

numero = int(input("Digite um numero: "))

area = area_do_circulo(numero)

print(f"A área do círculo é {area}")
