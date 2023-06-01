frutas = ['maçã', 'banana', 'abacaxi']
docesFesta = ['balaDeCoco', 'brigadeiro', 'cajuzinho']
feijoada = ['feijão preto', 'linguiça', 'bacon']

listona = [frutas, docesFesta, feijoada]

# b = sim
print(listona[1][1])

# c
listona[1].append('brigadeiro de limão')

# d
listona.extend(['suco de goiaba', 'refrigerante', 'cerveja'])

print(listona)

