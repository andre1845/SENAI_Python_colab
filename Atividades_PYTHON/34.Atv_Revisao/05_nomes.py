# 5. Crie uma lista de 10 nomes (informados dentro do programa). Em seguida, o usuário informa um número inteiro equivalente a um índice, e o programa retorna o nome equivalente ao índice informado pelo usuário.
while True:
    
    nomes = ["Alice", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Henrique", "Isabela", "João"]
    
    indice = int(input('Qual indice deseja consultar? '))
    print(f'Nome {indice}: {nomes[indice]}')
    
    continuar = input('Deseja continuar? (s/n) ')
    if continuar.lower() == "n":
        print('FIM\n')
        break
    else:
        continue