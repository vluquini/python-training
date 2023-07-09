#q9
'''
ler uma matriz 4x5 de inteiros calcular e imprimir a soma de todos os seus elementos
'''

matriz = [[0 for j in range(5)] for i in range(4)]

for i in range(4):
    for j in range(5):
        matriz[i][j] = int(input("Digite o elemento [%d][%d]: " % (i, j)))

# calcula a soma de todos os elementos da matriz
soma = 0

for i in range(4):
    for j in range(5):
        soma += matriz[i][j]

print("A soma de todos os elementos da matriz é:", soma)
