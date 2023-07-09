#q4
'''Escreva um programa para armazenar uma agenda de 10 telefones em um dicionário. Cada pessoa
pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve
ter as seguintes funções:
-incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou
mais telefones. Ela deve receber como argumentos o nome e os telefones.
-incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda.
Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja
incluí-lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo
nome.
-excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. Se a
pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
-excluirNome – essa função exclui uma pessoa da agenda.
-consultarTelefone – essa função retorna os telefones de uma pessoa na agenda'''

agenda = {}

def incluirNovoNome(nome, telefones):
    agenda[nome] = telefones
    print(f"O nome {nome} foi adicionado à agenda com os telefones: {telefones}")

def incluirTelefone(nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
        print(f"Telefone {telefone} adicionado para o contato {nome}")
    else:
        resposta = input(f"O nome {nome} não existe na agenda. Deseja adicioná-lo? (s/n) ").lower()
        if resposta == "s":
            telefones = [telefone]
            incluirNovoNome(nome, telefones)

def excluirTelefone(nome, telefone):
    if nome in agenda:
        if len(agenda[nome]) > 1:
            agenda[nome].remove(telefone)
            print(f"Telefone {telefone} removido do contato {nome}")
        else:
            del agenda[nome]
            print(f"Contato {nome} removido da agenda")
    else:
        print(f"O nome {nome} não existe na agenda")

def excluirNome(nome):
    if nome in agenda:
        del agenda[nome]
        print(f"Contato {nome} removido da agenda")
    else:
        print(f"O nome {nome} não existe na agenda")

def consultarTelefone(nome):
    if nome in agenda:
        telefones = agenda[nome]
        print(f"O nome {nome} não existe na agenda")

#Exemplo de uso das funções
incluirNovoNome("João", ["1234-5678", "9876-5432"])
incluirTelefone("Maria", "1111-2222")
excluirTelefone("João", "1234-5678")
excluirNome("Maria")
consultarTelefone("João")
consultarTelefone("Maria")