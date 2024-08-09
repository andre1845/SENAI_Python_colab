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
            novo_nome = input('Novo Nome: ')
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
            continue
                
        case '3':
            i=0
            print('\nLista Ordenada\n')
            nomes.sort()
            for nome in nomes:
                i+=1
                print(f'{i}. {nome}')
            print('.'*60)
            continue
            
        case '4':
            i=0
            print('\nLista Inversa\n')
            nomes.sort(reverse=True)
            for nome in nomes:
                i+=1
                print(f'{i}. {nome}')
            print('.'*60)
            continue
        
        case '5':
            break
        
        case _:
            print('Opcao invalida')
            continue
        