#q4
'''Ler um vetor vet de 10 elementos e obter um vetor w cujos
componentes são os fatoriais dos respectivos componentes de v.'''

# função para calcular fatorial
def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat

# vetor com 10 elementos
vet = [0] * 10

# leitura dos valores do vetor
for i in range(10):
    vet[i] = int(input("Digite um número: "))

# vetor w com os fatoriais dos elementos de vet
w = [fatorial(v) for v in vet]

# exibição dos vetores vet e w
print("Vetor vet:", vet)
print("Vetor w:", w)

