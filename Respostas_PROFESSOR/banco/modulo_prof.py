
from datetime import date

def exibir_menu():
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f'\n{'='*20} BANCO MADALORIANO | {dia}/{mes}/{ano} {'='*20}\n')
    print('1 - Criar conta')
    print('2 - Entrar na conta')
    print('3 - Exibir correntistas')
    print('4 - Excluir conta')
    print('5 - Encerrar conta')

def exibir_operacoes():
    print('\nOPERAÇÕES')
    print('1 - Consultar saldo')
    print('2 - Depositar valor')
    print('3 - Sacar valor')
    print('4 - Voltar')

def exibir_dados(nome, i, saldo):
    print(f'ID: {i}')
    print(f'ID: {nome}')
    print(f'Agência: 1001')
    print(f'Conta: 1001{i}')
    print(f'Saldo: R$ {saldo}')

def depositar_valor(saldo, valor):
    saldo += valor
    return saldo

def sacar_valor(saldo, valor):
    saldo -= valor
    return saldo

