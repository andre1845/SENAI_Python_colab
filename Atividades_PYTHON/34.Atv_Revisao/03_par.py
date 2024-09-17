# 3. Crie um programa onde o usuário informa um número inteiro, e o programa informa se o número e par ou ímpar.
import os
while True:
    os.system('cls')
    numero = input('Digite um numero inteiro: ')
    try:
        numero = int(numero)
        result = numero % 2
        if result == 0:
            tipo = "PAR"
        else:
            tipo = "IMPAR"
        print(f'O numero {numero} é {tipo}')
    except:
        print('Entrada inválida!')
    
    continuar = input('Deseja continuar? (s/n) ')
    if continuar.lower() == "n":
        print('FIM\n')
        break
    else:
        continue
