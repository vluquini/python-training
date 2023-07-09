#q5
def ip_valido(endereco_ip):
    partes = endereco_ip.split('.')
    if len(partes) != 4:
        return False

    for parte in partes:
        if not parte.isdigit() or int(parte) < 0 or int(parte) > 255:
            return False

    return True

endereco_ip = input("Digite um endereço IP: ")

if ip_valido(endereco_ip):
    print(f"O endereço {endereco_ip} é válido.")
else:
    print(f"O endereço {endereco_ip} não é válido.")
