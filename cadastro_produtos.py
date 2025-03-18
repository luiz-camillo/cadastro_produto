def desconto(x, percentual): #função para calcular desconto
  return x - (x * percentual / 100)

#validação da quantidade de produtos, try-except para tratar erros de inserção
while True:
    try:
        quantidade = int(input('Quantos produtos irá cadastrar? : '))
        break
    except ValueError:
        print('\nValor inválido, verifique e tente novamente')

#criação das listas
codigo = []
produto = []
preco = []

#loop para cadastro dos produtos com tratamento de codigo repetido e erros com o try-except
for i in range(quantidade):
    while True:
        try:
            novo_codigo = int(input(f'\nDigite o código do {i + 1}º produto: '))
            if novo_codigo in codigo:
                print('\nCódigo já cadastrado. Tente novamente')
                continue

            nome_produto = input(f'Qual o nome do produto {i + 1} ? : ').strip()

            while True:
                try:
                    valor_produto = float(input(f'Qual o valor do produto {nome_produto.upper()}: R$'))
                    break
                except ValueError:
                    print('\nValor inválido, verifique e tente novamente')

#adicionando os dados as listas após tratamento de erros e repetições
            codigo.append(novo_codigo)
            produto.append(nome_produto)
            preco.append(valor_produto)
            break

        except ValueError:
            print('\nValor inválido, verifique e tente novamente')

novo_preco = []

#adicionando desconto aos valores maiores que r$100
for product in preco:
    if product > 100:
        novo_preco.append(desconto(product,10))
    else:
        novo_preco.append(product)

print()
print(f'{"Código":<15}{"Produto":<30}{"Valor":<15}{"Desconto":<15}')  # Cabeçalho formatado

#iterando as listas e imprimindo os dados verificando se os produtos tiveram ou não desconto
for p in range(len(produto)):
    if preco[p] != novo_preco[p]:
        print(f'{codigo[p]:<15}{produto[p]:<30}R${novo_preco[p]:<14.2f}10%')  # Linha formatada com desconto
    else:
        print(f'{codigo[p]:<15}{produto[p]:<30}R${preco[p]:<14.2f}Não aplicado')  # Linha formatada sem descontado')
