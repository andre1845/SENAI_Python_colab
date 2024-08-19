import os

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * len(cpf):
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    if digito1 >= 10:
        digito1 = 0

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    if digito2 >= 10:
        digito2 = 0

    # Verifica se os dígitos calculados são iguais aos dígitos fornecidos
    return cpf[-2:] == f"{digito1}{digito2}"

clientes = []

dados = ('Nome', 'Data de Nascimento', 'CPF', 'Profissão', 'Email', 'Endereço', 'Telefone',)
os.system('cls')
while True:
    print('>'*20 + "  CADASTRO DE CLIENTES  " + '<'*20)
    print('1 - Incluir cliente')
    print('2 - Listar clientes')
    print('3 - Alterar dados de cliente')
    print('4 - Excluir cliente')
    print('5 - Pesquisar cliente')
    print('X - Para SAIR')

    opcao = input('Digite sua opção ')
    print('.'*60)

    match opcao:
        case '1':  # INCLUIR
            novo_cliente = {}
            for chave in dados:
                novo_cliente[chave] = input(f'Digite o(a) {chave} do cliente: ')
                if chave == 'CPF':
                    if validar_cpf(novo_cliente['CPF']):
                        novo_cliente['CPF'] = novo_cliente['CPF']
                    else:
                        novo_cliente['CPF'] = 'CPF inválido'                
            clientes.append(novo_cliente)
            continue
        case '2':  # LISTAR
            for i, cliente in enumerate(clientes, start=1):
                print(f'Cliente {i}  ' + '+'*20)
                for chave in dados:
                    print(f'{chave} : {cliente[chave]}')
                print('-'*30)
            continue
        case '3':  # ALTERAR
            pesquisar = input('Qual o nome do cliente a ser alterado? ')
            for cliente in clientes:
                if cliente['Nome'] == pesquisar:
                    for chave in dados:
                        novo_valor = input(f'Digite o novo(a) {chave} (ou pressione Enter para manter o atual): ')
                        if novo_valor:
                            cliente[chave] = novo_valor
                    break
            else:
                print('Cliente não encontrado.')
            continue
        case '4':  # EXCLUIR
            pesquisar = input('Qual o nome do cliente a ser excluído? ')
            encontrados = [cliente for cliente in clientes if cliente.get('Nome') == pesquisar]
            if len(encontrados) != 0:
                clientes = [cliente for cliente in clientes if cliente['Nome'] != pesquisar]
                print(f'Cliente {pesquisar} excluído.')
            else:
                print('Nenhum cliente encontrado.')
                    
            continue
       
        case '5':  # PESQUISAR indice
            pesquisar = input('Qual o nome do cliente a ser pesquisado? ')
            encontrados = [(i, cliente) for i, cliente in enumerate(clientes) if cliente.get('Nome') == pesquisar]
            
            if encontrados:
                for i, (indice, cliente) in enumerate(encontrados, start=1):
                    print(f'Cliente {i} (Índice Original: {indice})  ' + '+'*20)
                    for chave in dados:
                        print(f'{chave} : {cliente.get(chave, "Não informado")}')
                    print('-'*30)
            else:
                print('Nenhum cliente encontrado.')
            continue

        case _:
            break


'''
def main():
    cpf = input("Digite o CPF (apenas números): ")
    if validar_cpf(cpf):
        print("CPF válido!")
    else:
        print("CPF inválido!")

if __name__ == "__main__":
    main()
'''

