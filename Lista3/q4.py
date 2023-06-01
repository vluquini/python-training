compras = ['carne', 'feijão', 'macarrão', 'refrigerante', 'água sanitária', 'sorvete', 'sabonete', 'sabão em pó']

while 'detergente' in compras:
    compras.remove('sabão em pó')
while 'sabão em pó' in compras:
    compras.remove('água sanitária')

compras.remove('sorvete')


