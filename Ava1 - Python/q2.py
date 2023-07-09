#q2
'''Dada a frase “Python é muito legal”, use fatiamento para dar nome às variáveis contendo
cada palavra. O programa deverá:
a. imprima a quantidade de elementos da frase, das variáveis com os respectivos conteúdos
e tamanho.
b. imprima a frase invertida;
'''

frase = "Python é muito legal"
fatiamento = frase.split()
palavra1 = fatiamento[0]
palavra2 = fatiamento[1]
palavra3 = fatiamento[2]
palavra4 = fatiamento[3]

print(len(fatiamento))
print("Palavra 1 : ", palavra1, " tamanho: ", (len(palavra1)))
print("Palavra 2 : ", palavra2, " tamanho: ", (len(palavra2)))
print("Palavra 3 : ", palavra3, " tamanho: ", (len(palavra3)))
print("Palavra 4 : ", palavra4, " tamanho: ", (len(palavra4)))

print(frase[::-1])

