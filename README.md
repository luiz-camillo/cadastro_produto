O código começa pedindo para o usuário informar quantos produtos ele deseja cadastrar.
Se o usuário inserir algo errado, como texto no lugar de número, o bloco try-except captura o erro e trata a exceção, mostrando uma mensagem de aviso e pedindo para tentar novamente.
Após isso, o programa cria três listas vazias para armazenar as informações dos produtos: o código, o nome e o preço.

Em seguida, o código começa a cadastrar os produtos.
O usuário precisa informar o código, o nome e o preço de cada produto.
Se o código inserido já foi utilizado, o programa avisa e solicita um novo código.
O nome do produto é tratado para remover espaços extras no início ou no final, e o preço é validado para garantir que seja um número válido.
Se o usuário inserir algo errado ao digitar o preço, o try-except captura e trata o erro, pedindo para tentar novamente.

Depois de cadastrar todos os produtos, o código cria uma nova lista com os preços atualizados, considerando os descontos.
Se o preço for superior a 100 reais, aplica-se um desconto de 10%.
Caso contrário, o preço permanece o mesmo.

Por fim, o programa exibe uma tabela com os dados dos produtos cadastrados, mostrando o código, o nome, o preço e se o desconto foi aplicado ou não.
Se o desconto for aplicado, o valor "10%" é exibido, caso contrário, é mostrado "Não aplicado".
O código foi estruturado de forma a garantir que qualquer erro de entrada seja tratado adequadamente, oferecendo uma experiência mais robusta ao usuário.
