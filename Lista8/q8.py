#q8
'''
Criar programa que leia elementos de uma matriz inteira de 10x10 e
escreva todos os elementos, exceto os elementos da diagonal principal.
'''

# cria uma matriz vazia com 10 linhas e 10 colunas
matriz = [[0 for j in range(10)] for i in range(10)]

# faz a leitura dos elementos da matriz
for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input("Digite o elemento [%d][%d]: " % (i, j)))

print("Elementos da matriz (exceto a diagonal principal):")

for i in range(10):
    for j in range(10):
        if i != j:
            print(matriz[i][j], end=" ")

    print()

