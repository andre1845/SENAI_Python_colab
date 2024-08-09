import os

lista = []
lista_ordenada = []
retirados = []

os.system('cls')

while True:
    print('>'*20 + " MENU " + '<'*20)
    print("1 - Incluir na lista.")
    print("2 - Excluir da lista.")
    print("3 - Alterar nome da lista.")
    print("4 - Separar da lista.")
    print("5 - Localizar na lista.")
    print("6 - Imprimir lista principal ordenada.")
    print("7 - Imprimir itens retirados da lista.")
    print("8 - Imprimir a lista original.")
    print("9 - Pesquisar pela letra inicial do nome.")
    print("10 - Sair.")
    print('-' * 60)
    print(f'\n')
    
    opcao = input("Digite sua opção ")
    
    match opcao :
        case '1':
            nome = input('Nome a incluir na lista: ')
            if nome != "":
                nome = nome.title()
                lista.append(nome)
                print(f'{nome} incluído!')
                print(f'\n')
            else:
                print('Você não digitou nada...')
            continue
        case '2':
            nome = input('Nome a ser excluído da lista: ')
            try:
                lista.remove(nome)
                print(f'{nome} excluído!')
                print(f'\n')
            except:
                print(f'{nome} não encontrado')
            finally:
                continue
        case '3':
            nome = input('Nome a ser alterado : ')
            novo_nome = input('Novo nome : ')
            try:
                lista[lista.index(nome)]= novo_nome
                print(f'{nome} substituído por {novo_nome}')
            except:
                print(f'{nome} não encontrado. Tente novamente.')
            finally:
                continue
        case '4':
            nome_separado = input('Qual nome deseja separar da lista? ')
            try:
                indice = lista.index(nome_separado)
                separado = lista.pop(indice)
                retirados.append(separado)
                print(f'{separado} foi retirado da lista original.')
            except:
                print(f'{nome_separado} não foi encontrado.')
            finally:
                continue
        case '5':
            nome = input('Nome a ser localizado : ')
            try:
                indice = lista.index(nome)
                print(f'{nome} tem o índice {indice}')
            except:
                print(f'{nome} não encontrado. Tente novamente.')
            finally:
                continue
        case '6':
            lista_ordenada = lista.copy()
            lista_ordenada.sort()
            i = 1
            print('.' * 20 + 'LISTA ORDENADA' + '.'*20)
            for nome in lista_ordenada:
                print(f'{i}. {nome}')
                i = i+1
            print('-' * 50)        
            continue
        case '7':
            j = 1
            if(len(retirados) > 0):
                print('Nomes retirados da lista original1')
                for nome in retirados:
                    print(f'{j}. {nome}')
                    i = 1+1
            else:
                print('A lista de nomes retirados está vazia.')
            continue
        case'8':
            i = 1
            print('.' * 20 + 'LISTA ORIGINAL' + '.'*20)
            for nome in lista:
                print(f'{i}. {nome}')
                i = i+1
            print('-' * 50)        
            continue
        case '9':
            letra_inicial = input('Digite a letra inicial para buscar: ').capitalize()
            nomes_encontrados = [nome for nome in lista if nome.startswith(letra_inicial)]
    
            if nomes_encontrados:
                print(f'Nomes encontrados começando com "{letra_inicial}":')
                for nome in nomes_encontrados:
                    print(nome)
            else:
                print(f'Nenhum nome encontrado começando com "{letra_inicial}".')
            continue
        case '10':
            print('Programa encerrado !')
            break
        case _:
            print('Opção inválida')
            continue
    