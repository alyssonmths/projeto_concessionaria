# SISTEMA CONCESSIONÁRIA

def procurar_carro():
    print('\033[36mPESQUISA: \033[0m')
    print('\033[1mPreço máximo: digite o valor\nEstado de conservação: escolha uma das opções: \033[33mnovo - seminovo - conservado - mal estado')
    pesquisa = input('Sua escolha: \033[0m')
    
    carros = [] # inicializa o array contendo os resultados da pesquisa

    with open('estoque_carros.txt', 'r') as estoque_carros: # abre o arquivo e percorre as linhas
        for linha in estoque_carros:
            carro = linha.strip().split(',')
            carro[1] = float(carro[1])
            carro[2] = int(carro[2])
            try:
                if carro[1] <= float(pesquisa):
                    carros.append({
                        'nome_carro': carro[0],
                        'preco': carro[1],
                        'ano': carro[2],
                        'estado': carro[3]
                    })
            except:
                if carro[3] == pesquisa:
                    carros.append({
                        'nome_carro': carro[0],
                        'preco': carro[1],
                        'ano': carro[2],
                        'estado': carro[3]
                    })
    if len(carros) != 0:
        return carros
    else:
        return '\033[31mCarro não encontrado!\033[0m'
def cadastrar_carro():
    print('\033[36mCADASTRO DE NOVO CARRO: \033[0m')
    nome = input('\033[1mNome: ')
    while True:
        try:
            preco = float(input('\033[1mPreço: '))
            break
        except ValueError:
            print('\033[31mErro: Digite um valor numérico para o preço.\033[0m')
    while True:
        try:
            ano_fabricacao = int(input('\033[1mAno de fabricação: '))
            break
        except ValueError:
            print('\033[31mErro: Digite um número inteiro válido para o ano de fabricação.\033[0m')

    estado = input('Estado de conservação: ')

    with open('estoque_carros.txt', 'a') as estoque_carros:
        estoque_carros.write(f'{nome},{preco},{ano_fabricacao},{estado}\n')
    
    return '\033[32mCarro cadastrado!\033[0m'
def gerar_tabela(lista):
    tamanho_nome_maximo = 0
    tamanho_preco_maximo = 0

    for carro in lista:
        if len(carro['nome_carro']) > tamanho_nome_maximo:
            tamanho_nome_maximo = len(carro['nome_carro'])
        if len(str(carro['preco'])) > tamanho_preco_maximo:
            tamanho_preco_maximo = len(str(carro['preco']))

    for carro in lista:
        tamanho_nome_atual = len(carro['nome_carro'])
        tamanho_preco_atual = len(str(carro['preco']))

        print(f'{carro['nome_carro'] + ' ' * (tamanho_nome_maximo-tamanho_nome_atual)} | R$ {str(carro['preco']) + ' ' * (tamanho_preco_maximo-tamanho_preco_atual)} | {carro['ano']} | {carro['estado']}')

print('\033[36m-=- Simulador concessionária -=-\033[0m')

while True:
    print('\033[1m0 - Sair do sistema\n1 - Cadastrar um novo carro\n2 - Pesquisar carros')
    escolha = input('\033[33mSua escolha: \033[0m')
    if escolha == '1':
        print(cadastrar_carro())
    elif escolha == '2':
        carros = procurar_carro()
        if type(carros) == list:
            gerar_tabela(carros)
        else:
            print(carros)
    elif escolha == '0':
        break
    else:
        print('\033[31mEscolha uma opção válida!\033[0m')
        continue

print('\033[32mObrigado por utilizar o sistema\033[0m')
