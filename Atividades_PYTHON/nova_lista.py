usuarios = [
    {'Nome':  'Fulano',
     'Idade': 20,
     'Profissão': 'Programador',
    },
    {'Nome':  'Alberto',
     'Idade': 32,
     'Profissão': 'Desenvolvedor',
    },
    {'Nome':  'Mario',
     'Idade': 20,
     'Profissão': 'Eletricista',
    },
    {'Nome':  'Roberta',
     'Idade': 41,
     'Profissão': 'Policial',
    }   
]

chaves = ["Nome", "Idade", "Profissão"]

# Criação de um novo usuário
while True:
    novo_usuario = {}
    for chave in chaves:
        novo_usuario[chave] = input(f'Digite o {chave} do novo usuário: ')

    usuarios.append(novo_usuario)
    continuar = input('Continuar? s/n')
    if continuar != 'n':
        continue
    else:
# Exibição dos usuários
        for usuario in usuarios:
            for chave in chaves:
                print(f'{chave}: {usuario[chave]}')
            print('-' * 30)
        break
