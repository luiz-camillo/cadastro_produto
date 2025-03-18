def desconto(x, percentual):
  return x - (x * percentual / 100)


while True:
    try:
        quantidade = int(input('Quantos produtos irá cadastrar? : '))
        break
    except ValueError:
        print('\nValor inválido, verifique e tente novamente')

codigo = []
produto = []
preco = []

for i in range(quantidade):
    while True:
        try:
            novo_codigo = int(input(f'\nDigite o código do {i + 1}º produto: '))
            if novo_codigo in codigo:
                print('\nCódigo já cadastrado. Tente novamente')
                continue

            nome_produto = input(f'Qual o nome do produto {i + 1}? : ')

            while True:
                try:
                    valor_produto = float(input(f'Qual o valor do produto {nome_produto.upper()}: R$'))
                    break
                except ValueError:
                    print('\nValor inválido, verifique e tente novamente')

            codigo.append(novo_codigo)
            produto.append(nome_produto)
            preco.append(valor_produto)
            break

        except ValueError:
            print('\nValor inválido, verifique e tente novamente')

novo_preco = []

for product in preco:
    if product > 100:
        novo_preco.append(desconto(product,10))
    else:
        novo_preco.append(product)

