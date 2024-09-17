#1. Crie um programa que peça para que o usuário digite um número, em seguida o converta para float, exibindo em tela tanto o número em si quanto seu tipo de dado.

num = input('Digite um número \n')
try:
    print(f'{num} -> {type(num)}\n')
    print('Agora convertendo: ')
    num_conv = float(num)
    print (f'{num_conv}  ->  {type(num_conv)}\n\n')
except:
    print('Entrada invalida!')