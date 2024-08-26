

def fibonacci(valor):
    numero = []
    i = 0
    for i in range(valor):
        if i == 0:
            numero.append(0)
        elif i == 1:
            numero.append(1)
        else:
            proximo_valor = numero[i-1] + numero[i-2]
            numero.append(proximo_valor)
            i += 1 
    return numero

while True:
    num = int(input('Digite um número: '))
    sequencia = fibonacci(num)
    for x in sequencia:
        print(x)
    opcao = input('Continuar? s/n ')
    if opcao.lower() != 'n':
        continue
    else:
        break
