# 7. Crie um programa onde o usuário possa digitar uma lista de nomes (quantos ele quiser) e no final exiba a lista de nomes em ordem alfabética na tela, mostrando também o número de nomes digitado pelo usuário.

nomes = []

while True:
    print(f'\n OPCOES')
    print('1 - Inserir')
    print('2 - Exibir lista')
    print('3 - Ordenar')
    print('4 - Ordenar inversamente')
    print('5 - Sair')
    print('-'*50)

    opcao = input('Escolha uma opcao ')

    match opcao:
        case '1':
            print('Digite os nomes e pressione ENTER. Deixe vazio para encerrar a entrada de nomes')
            while True:
                novo_nome = input('Novo Nome: ')
                if novo_nome == "":
                    break
                nomes.append(novo_nome.upper())
                print('Nome inserido\n')
                continue
        
        case '2':
            i=0
            print('\nLista\n')
            for nome in nomes:
                i+=1
                print(f'{i}. {nome}')
            print('.'*60)
            print(f'A lista contém {len(nomes)} nomes.')
            continue
                
        case '3':
            i=0
            print('\nLista Ordenada\n')
            nomes.sort()
            for nome in nomes:
                i+=1
                print(f'{i}. {nome}')
            print('.'*60)
            print(f'A lista contém {len(nomes)} nomes.')
            continue
            
        case '4':
            i=0
            print('\nLista Inversa\n')
            nomes.sort(reverse=True)
            for nome in nomes:
                i+=1
                print(f'{i}. {nome}')
            print('.'*60)
            print(f'A lista contém {len(nomes)} nomes.')
            continue
        
        case '5':
            break
        
        case _:
            print('Opcao invalida')
            continue