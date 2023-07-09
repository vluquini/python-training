#q11
'''
Criar programa que leia e armazena os elementos de
uma matriz M inteira 10x10 e imprima todos os elementos que estão em
linhas pares e colunas impares.
'''

# cria uma matriz vazia com 10 linhas e 10 colunas
matriz = [[0 for j in range(10)] for i in range(10)]

# faz a leitura dos elementos da matriz
for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input("Digite o elemento [%d][%d]: " % (i, j)))

# cria uma nova matriz vazia com 10 linhas e 10 colunas
matriz_invertida = [[0 for j in range(10)] for i in range(10)]

# preenche a nova matriz com os elementos invertidos da matriz original
for i in range(10):
    for j in range(10):
        matriz_invertida[j][i] = matriz[i][j]

print("Matriz invertida:")

for i in range(10):
    for j in range(10):
        print(matriz_invertida[i][j], end=" ")

    print()
