import os
from modulo_prof import *


if __name__ == '__main__':

    correntistas = [
            {
                'Nome': 'Admin',
                'Saldo': 0
            }
        ]
    
    while True:
        
        exibir_menu()
        op = input('Informe o índice da ação que deseja realizar: ')
        os.system('cls')

        match op:
            case '1':
                conta = {
                    'Nome': '',
                    'Saldo': 0
                }
                conta['Nome'] = input('Informe o nome a ser cadastrado: ')
                correntistas.append(conta)
                print(f'{conta['Nome']} cadastrado com sucesso!')
                continue
            
            case '2':
                titular = input('Informe o nome do titular da conta: ')

                try:
                    for i in range(len(correntistas)):
                        if titular in correntistas[i]['Nome']:
                            nome = correntistas[i]['Nome']
                            saldo = correntistas[i]['Saldo']

                            while True:
                                exibir_dados(nome, i, saldo)
                                exibir_operacoes()

                                opera = input('Operação desejada: ')
                                os.system('cls')

                                match opera:
                                    case '1':
                                        print(f'Saldo: R$ {saldo:,.2f}')
                                        continue

                                    case '2':
                                        valor = float(input('Valor do depósito: R$ ').replace(',','.'))
                                        saldo = depositar_valor(saldo, valor)
                                        correntistas[i]['Saldo'] = saldo

                                        print('Depósito efetuado com sucesso.')
                                        print(f'Saldo atual: R$ {saldo:,.2f}')
                                        continue

                                    case '3':
                                        valor = float(input('Valor do saque: R$ '))

                                        if valor < saldo:
                                            saldo = sacar_valor(saldo, valor)
                                            correntistas[i]['Saldo'] = saldo #atualiza o saldo

                                            print('Saque efeturado com sucesso!')
                                            print(f'Saldo atual: R$ {saldo:,.2f}')
                                        else:
                                            print('Não foi possivel efetuar o saque.')
                                        
                                        continue

                                    case '4':
                                        break

                                    case _:
                                        print('Operação inválida!')
                                        continue
                        else:
                            continue #else do if que verifica o nome
                except:
                    print(f'{nome} não encontrado')

                continue #volta para o menu anterior
            
            case '3':
                for conta in correntistas:
                    print(conta)
                continue

            case '4':
                indice = int(input('Infor o ID da conta a ser excluída: '))

                try:
                    del[correntistas[indice]]
                    print(f'Conta {indice} deletada com sucesso!')
                except:
                    print('Não foi possível deletar conta!')
                continue

            case '5':
                break

            case _:
                print('Opção inválida!')

        