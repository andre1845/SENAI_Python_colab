import os
lista_notas = []
i = 1
os.system('cls')
print ('Digite as notas abaixo. ')
while True:
    
    nota_input = input(f'Digite a {i}ª nota (Deixe em branco para encerrar)')
    nota_input = str(nota_input).replace(",", ".")
    try:
        nota_input = float(nota_input)
        if nota_input < 0 or nota_input >10:
            print('Nota invalida')
            continue
    except:
        if nota_input != "" :
            print('Nota invalida')
            continue
    
    i = i+1
    if nota_input != "":
        nota = nota_input
        lista_notas.append(nota)
        continue
    else:
        
        qtde = len(lista_notas)
        soma = sum(lista_notas)
        media = soma/qtde
        print(f'\nA média das {qtde} notas é {media:,.2f}')
        
    continuar = input('Deseja calcular outra média? (s/n) ')
    if continuar != "n":
        i=1
        lista_notas = []
        continue
    else:
        break
