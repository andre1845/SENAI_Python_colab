# 9. Crie um programa onde o usuário cadastre uma quantidade desejada de eventos (nome do evento e classificação indicativa) e após o cadastro dos eventos, o usuário possa informar o nome e a idade, e se inscrever em um dos eventos. Caso o usuário não tenha idade mínima, o programa proíbe a inscrição e pede para o mesmo se inscrever em outro evento. Caso o usuário tenha a idade mínima, o programa inscreve o usuário exibindo a data da inscrição e encerra.
import os
import datetime

def verifica_idade(idade, classificacao):
    if idade >= classificacao:
        result = "Participação autorizada"
    else:
        result = "Participação NEGADA. Voce nao tem idade suficiente."
    return result

def menu():    
    print('>'*20 + "  CADASTRO DE ATIVIDADES  " + '<'*20)
    print('1 - Incluir atividade')
    print('2 - Listar atividades')
    print('3 - Alterar dados de atividade')
    print('4 - Excluir atividade')
    print('5 - ESCOLHER ATIVIDADE')
    print('6 - Encerrar')

# -------------------------------------------------------------------- #

atividades = []
dados = ("Nome", "Classificacao")

while True:
    menu()
    opcao = input('Escolha uma opção: ')
    match opcao:
            case '1':  # INCLUIR
                    nova_atividade = {}
                    for chave in dados:
                        nova_atividade[chave] = input(f'Digite o(a) {chave}: ')
                    atividades.append(nova_atividade)
                    continue
            case '2':  # LISTAR
                for i, atividade in enumerate(atividades, start=1):
                    print(f'Atividade {i}  ' + '+'*20)
                    for chave in dados:
                        print(f'{chave} : {atividade[chave]}')
                    print('-'*30)
                continue
            case '3':  # ALTERAR
                pesquisar = input('Qual a atividade deseja alterar? ')
                for atividade in atividades:
                    if atividade['Nome'] == pesquisar:
                        for chave in dados:
                            novo_valor = input(f'Digite o(a) novo(a) {chave} (ou pressione Enter para manter o atual): ')
                            if novo_valor:
                                atividade[chave] = novo_valor
                        break
                else:
                    print('Atividade não encontrada.')
                continue
            case '4':  # EXCLUIR
                pesquisar = input('Qual o nome da atividade a ser excluída? ')
                encontrados = [atividade for atividade in atividades if atividade.get('Nome') == pesquisar]
                if len(encontrados) != 0:
                    atividades = [atividade for atividade in atividades if atividade['Nome'] != pesquisar]
                    print(f'Atividade {pesquisar} excluída.')
                else:
                    print('Nenhuma atividade encontrada.')
                        
                continue
        
            case '5':  # ESCOLHER indice
                nome = input ('Digite seu nome: ')
                data_atual = datetime.datetime.now()
                pesquisar = input('Qual o nome da atividade escolhida? ')
                encontrada = [ atividade for atividade in atividades if atividade.get('Nome') == pesquisar]
                if encontrada:
                    classif = int(encontrada[0]['Classificacao'])
                    while True:
                        try:
                            idade = input('Qual a sua idade? ')
                            idade = int(idade)
                            verif = verifica_idade(idade, classif)
                            print(verif)
                            print(f'{nome} inscrito em {encontrada[0]['Nome']} em {data_atual}')
                            
                            break
                        except:
                            print('Idade inválida. Digite um número inteiro e positivo.')
                            continue
                else:
                    print('Nenhuma atividade encontrada.')
                continue

            case '6':
                print('FIM')
                print('x'*50)
                break
            case _:
                print('Opcao invalida.')
                continue

