# 10.  Crie um programa em que o usuário cadastre quantos cursos ele quiser (nome do curso, duração do curso em horas, Período do dia, quantidade de vagas) e exiba na tela.
import os

cursos = []

dados = ('Nome', 'Duracao', 'Periodo', 'Vagas',)
os.system('cls')
while True:
    print('>'*20 + "  CADASTRO DE CURSOS  " + '<'*20)
    print('1 - Incluir curso')
    print('2 - Listar cursos')
    print('3 - Alterar dados de curso')
    print('4 - Excluir curso')
    print('5 - Pesquisar curso')
    print('X - Para SAIR')

    opcao = input('Digite sua opção ')
    print('.'*60)

    match opcao:
        case '1':  # INCLUIR
            novo_curso = {}
            for chave in dados:
                novo_curso[chave] = input(f'Digite o(a) {chave} do curso: ')
            cursos.append(novo_curso)
            continue
        case '2':  # LISTAR
            for i, curso in enumerate(cursos, start=1):
                print(f'Curso {i}  ' + '+'*20)
                for chave in dados:
                    print(f'{chave} : {curso[chave]}')
                print('-'*30)
            continue
        case '3':  # ALTERAR
            pesquisar = input('Qual o nome do curso a ser alterado? ')
            for curso in cursos:
                if curso['Nome'] == pesquisar:
                    for chave in dados:
                        novo_valor = input(f'Digite o novo(a) {chave} (ou pressione Enter para manter o atual): ')
                        if novo_valor:
                            curso[chave] = novo_valor
                    break
            else:
                print('curso não encontrado.')
            continue
        case '4':  # EXCLUIR
            pesquisar = input('Qual o nome do curso a ser excluído? ')
            encontrados = [curso for curso in cursos if curso.get('Nome') == pesquisar]
            if len(encontrados) != 0:
                cursos = [curso for curso in cursos if curso['Nome'] != pesquisar]
                print(f'curso {pesquisar} excluído.')
            else:
                print('Nenhum curso encontrado.')
                    
            continue
       
        case '5':  # PESQUISAR indice
            pesquisar = input('Qual o nome do curso a ser pesquisado? ')
            encontrados = [(i, curso) for i, curso in enumerate(cursos) if curso.get('Nome') == pesquisar]
            
            if encontrados:
                for i, (indice, curso) in enumerate(encontrados, start=1):
                    print(f'curso {i} (Índice Original: {indice})  ' + '+'*20)
                    for chave in dados:
                        print(f'{chave} : {curso.get(chave, "Não informado")}')
                    print('-'*30)
            else:
                print('Nenhum curso encontrado.')
            continue

        case _:
            break
