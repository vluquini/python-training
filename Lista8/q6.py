#q6
'''
Criar programa que leia elementos de uma matriz inteira de 10x10 e escreva os elementos
da diagonal principal.
'''

# cria uma matriz vazia com 10 linhas e 10 colunas
matriz = [[0 for j in range(10)] for i in range(10)]

# faz a leitura dos elementos da matriz
for i in range(10):
    for j in range(10):
        matriz[i][j] = int(input("Digite o elemento [%d][%d]: " % (i, j)))

# imprime os elementos da diagonal principal
print("Elementos da diagonal principal: ")

for i in range(10):
    print(matriz[i][i], end=" ")

print()
