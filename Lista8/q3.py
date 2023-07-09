#q3
'''Cria um programa que leia vários números
inteiros e positivos. A leitura se encerra quando encontrar um numero
negativo ou quando o vetor ficar completo. sabe-se que o vetor possui no
maximo 10 elementos. gerar e imprimir um vetor onde cada elemento é o
inverso do correspondente do vetor principal.'''

max = 5
list1 = []
list_inverted = []

print('Preencha a lista. Para encerrar, digite um número negativo.')

for i in range(max):
    elemento = int(input('Digite um número: '))
    if elemento < 0:
        break
    list1.append(elemento)

# print(len(list1))

for i in range(len(list1)):
    list_inverted.append(list1[i] * (-1))

print(list1)
print(list_inverted)

