print('\nNúmeros amarelos são os divisiveis, os vermelhos são os que não pode ser divididos pelo valor x')
x=int(input("Digite um numero: "))
cont = 0
for c in range(1,x+1):
    if x % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')

    print('{} '.format(c), end='')
print('\n\033[m0 número {} foi divisel {} vezes'.format(x,cont))
if cont == 2:
    print('É Primo')
else:
    print('Não é Primo')
