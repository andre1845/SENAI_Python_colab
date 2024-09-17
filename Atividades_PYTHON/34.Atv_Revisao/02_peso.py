# 2. Crie um programa que receba o peso (em gramas) de um bebê recém-nascido, e indique se o bebê está normal ou se precisa ficar internado, caso o bebê tenha menos que 2500g.

try:
    peso = int(input('Digite o peso do bebê: '))
    if(peso <= 2500):
        print('Peso abaixo do mínimo. Necessita ser internado.\n\n')
    else:
        print('Peso normal.\n\n')
except:
    print('Entrada invalida!')