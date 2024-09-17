calcular_pg = lambda x: x*2
num = [1,2,3,4,5,6,7,8,9]

pg = list(map(calcular_pg, num))

for i in pg:
    print(i)