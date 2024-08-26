def calcular_fibonacci(n):
    if n <=1 :
        return n
    else:
        return calcular_fibonacci(n-1)+calcular_fibonacci(n-2)
    
n = int(input('Digite um numero: '))
    
for x in range(n):
    print(calcular_fibonacci(x))