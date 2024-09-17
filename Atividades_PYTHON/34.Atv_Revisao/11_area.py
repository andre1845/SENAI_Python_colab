# 11. Crie um programa com funções para calcular a área de 4 figuras geométricas (quadrado, círculo, triângulo e trapézio).

def mostra_menu():
    print('1 - Calcular quadrilatero')
    print('2 - Calcular triangulo')
    print('3 - Calcular circulo')
    print('4 - Calcular trapezio')
    print('5 - Sair')

def quadrilatero(base, altura):
    result = base * altura
    return result

def trapezio(base_maior, base_menor, altura):
    result = ((base_maior + base_menor)/2) * altura
    return result

def triangulo(base, altura):
    result = base * (altura / 2)
    return result

def circulo(raio):
    result = 3.14 * (raio**2)
    return result

# programa principal (MAIN)
while True:
    mostra_menu()
    opcao = input('opcao? ')

    match opcao:
        
        case '1':
            b = float(input("Digite a base: "))
            a = float(input("Digite a altura: "))
            print(f'Area do quadrilatero = {quadrilatero(b,a)}')
            print('-'*40)
            continue
        case '2':
            b = float(input("Digite a base: "))
            a = float(input("Digite a altura: "))
            print(f'Area do triangulo = {triangulo(b,a)}')
            print('-'*40)
            continue
        case '3':
            r = float(input("Digite o raio: "))
            print(f'Area do circulo = {circulo(r)}')
            print('-'*40)
            continue
        case '4':
            c = float(input("Digite a base maior: "))
            b = float(input("Digite a base menor: "))
            a = float(input("Digite a altura: "))
            print(f'Area do quadrilatero = {trapezio(c,b,a)}')
            print('-'*40)
            continue
        case _:
            print('FINAL')
            break
        