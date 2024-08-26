import os

# função de leitura de arquivo
def ler_arquivo():
    with open('manipular_arq/arquivo.txt', 'r', encoding='utf-8') as arquivo:
        dados = arquivo.read()
    return dados

def exibir_menu():
    print('1 - Ler arquivo')
    print('2 - Gravar novos dados no arquivo')
    print('3 - Sair do programa')

# função para gravar novos dados
def gravar_arquivo(dados, nome, email, profissao):
    dados += f'\n\n{'-'*30}\n\nNome: {nome}\nEmail: {email}\nProfissão: {profissao}'
    with open('manipular_arq/arquivo.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(dados)

    
if __name__ == '__main__':
    while True:
        dados = ler_arquivo()
        exibir_menu()
        opcao = input('Opcao desejada: ')
        os.system('cls')
        match opcao:
            case '1':
                print(f'\n{dados}\n')
                continue
            
            case '2':
                print('NOVO CADASTRO:\n')
                novo_nome = input('Informe o novo nome: ')
                novo_email = input('Informe o novo email: ')
                nova_profissao = input('Informe a nova profissao: ')
                gravar_arquivo(dados, novo_nome, novo_email, nova_profissao)
                continue
            case '3':
                print('FIM')
                break
            case _:
                print('Opção Inválida')
                continue
    
    
    print(ler_arquivo())