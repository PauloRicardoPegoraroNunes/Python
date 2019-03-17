import math
v = int(input('Valor : '))

v1 = 1
c = 0

while c < v:
    c = v1*(v1+1)*(v1+2)
    v1 += 1

if c == v:
    print('{} É Triangular'.format(v))
else:
    print('{} Não é Triangular'.format(v))
