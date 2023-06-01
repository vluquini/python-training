frutas = ['maçã', 'banana', 'abacaxi']
docesFesta = ['balaDeCoco', 'brigadeiro', 'cajuzinho']
feijoada = ['feijão preto', 'linguiça', 'bacon']

listona = [frutas, docesFesta, feijoada]
listona[1].append('brigadeiro de limão')
listona.extend(['suco de goiaba', 'refrigerante', 'cerveja'])

del listona[:]
print(listona)