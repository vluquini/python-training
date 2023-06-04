#q7
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

lista_numeros = [num1, num2, num3]
lista_ordenada = sorted(lista_numeros, reverse=True)
maior = lista_ordenada[0]
menor = lista_ordenada[2]
meio = lista_ordenada[1]

print("O maior numero: ", maior)
print("O numero do meio:", meio)
print("O menor numero: ", menor)
