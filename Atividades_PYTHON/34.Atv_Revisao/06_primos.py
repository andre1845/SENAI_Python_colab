# 6. Crie um programa que possua uma lista com números de 1 a 20, e informe quais deles são primos.
import os
os.system('cls')
limite = int(input('Qual o limite para testar numeros primos? '))
for i in range (2, limite+1):
    #print(f'Numero {i} : ')
    cont = 0
    for j in range (2, i+1):
        teste = i % j
        if teste == 0 :
            cont = cont + 1
            if cont >= 2:
                j = i
    if cont <= 1:
        print(f'O numero {i} é primo.')
        print('-'*30)
print('Fim da lista.')        