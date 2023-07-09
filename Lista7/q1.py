#q1
def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} é um número par")
    else:
        print(f"{numero} é um número ímpar")

numero = int(input("Digite um numero: "))

par_ou_impar(numero)
