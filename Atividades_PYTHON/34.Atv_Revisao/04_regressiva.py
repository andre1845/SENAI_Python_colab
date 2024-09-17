# 4. Crie um programa que o usuário informa um número inteiro positivo, e o programa exibe na tela uma contagem regressiva.
import os
import time
import math

cont = int(input('Digite o tempo em segundos: '))
try:
    cont = (math.fabs(cont))
    while cont > 0:
        os.system('cls')
        print(f'{cont} .', end="")
        for i in range (10):
            time.sleep(0.1)
            print('.', end="")
        cont -= 1
    print('\n\nFIM da contagem.\n')
    
except:
    print('Entrada Inválida!')

