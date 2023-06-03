#q5
agenda = {}
for i in range(2):
    cpf = input("Digite o CPF: ")
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    telefone = input("Digite o telefone: ")
    agenda[cpf] = {"nome": nome, "idade": idade, "telefone": telefone}

for cpf, dados in agenda.items():
    print(f"{cpf}: {dados['nome']}-{dados['idade']}-{dados['telefone']}")

