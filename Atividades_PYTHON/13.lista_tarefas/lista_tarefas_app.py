
tarefas = []

while True:

    print('1. Inserir tarefa')
    print('2. Listar tarefas')
    print('3. Ordenar tarefas por prioridade')
    print('4. Sair')
    

    opcao = input('Digite a opção: ')

    match opcao:
        
        case '1':
            tarefa = input('Digite a tarefa : ')
            prioridade = input('Qual a prioridade? (de 1 a 9)')
            tarefa = prioridade + " " + tarefa
            tarefas.append(tarefa)
            print(f'Tarefa incluída\n')
            continue
        
        case '2':
            print(f'\n LISTA DE TAREFAS')
            i = 0
            for tarefa in tarefas:
                i += 1
                print(f'{i}) {tarefa}')
            print('-'*50)
            continue
        
        case '3':
            tarefas.sort()
            print(f'\n LISTA DE TAREFAS\n')
            i = 0
            for tarefa in tarefas:
                i += 1
                print(f'{i}) {tarefa}')
            print('-'*50)
            continue
        
        case '4':
            break
        
        case _:
            print('Opção inválida')
        
    