#q3
'''Criar programa que leia dois conjuntos de números inteiros, tendo cada
um 10 e 20 elementos e apresente os elementos comuns aos conjuntos.
lembre-se de que os elementos podem se repetir mas não podem aparecer
repetidos na saída.'''

# set() é uma função imbutida para auxiliar na criação de conjuntos.
conjunto1 = set()
conjunto2 = set()

for i in range(4):
    elemento = int(input(f'Digite o {i+1} elemento do primeiro conjunto: '))
    conjunto1.add(elemento)

for i in range(5):
    elemento = int(input(f'Digite o {i + 1} elemento do segundo conjunto: '))
    conjunto2.add(elemento)

# intersection() seleciona apenas os elementos comuns aos 2 conjuntos
elementos_comuns = conjunto1.intersection(conjunto2)

print(elementos_comuns)
