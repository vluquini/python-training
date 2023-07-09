#q10
'''
Criar programa que leia e armazena os elementos de
uma matriz M inteira 10x10 e imprima todos os elementos que estão em
linhas pares e colunas impares.
'''

matriz = [[0 for j in range(10)] for i in range(10)]

for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input("Digite o elemento [%d][%d]: " % (i, j)))

print("Elementos das linhas pares e colunas ímpares:")

for i in range(0, 10, 2):
    for j in range(1, 10, 2):
        print(matriz[i][j], end=" ")

    print()
