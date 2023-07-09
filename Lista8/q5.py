#q5
'''
Criar programa que leia dados de 20 elementos inteiros. imprimir o
maior e o menor, sem ordenar, o percentual de números pares e a media
dos elementos do vetor.
'''

vetor = []
posicao = 0

while posicao < 20:
    numero = int(input("Digite o %dº número inteiro: " % (posicao + 1)))
    vetor.append(numero)
    posicao += 1

# encontra o maior e o menor elemento do vetor
maior = max(vetor)
menor = min(vetor)

# calcula o percentual de números pares
num_pares = len([x for x in vetor if x % 2 == 0])
percentual_pares = (num_pares / len(vetor)) * 100

# calcula a média dos elementos do vetor
media = sum(vetor) / len(vetor)

print("Maior elemento:", maior)
print("Menor elemento:", menor)
print("Percentual de números pares: %.2f%%" % percentual_pares)
print("Média dos elementos:", media)
