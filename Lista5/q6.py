#q6
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

lista_numeros = [num1, num2, num3]
lista_ordenada = sorted(lista_numeros)
print("Os números em ordem crescente são: ", lista_ordenada[0], lista_ordenada[1], lista_ordenada[2])
