import area
print('1 - Area do Circulo')
print('2 - Area do Triangulo')
print('3 - Area do Retangulo')
r = int(input('\nOque deseja calcular : '))

if r == 1:
    v1 = int(input('Raio = '))
    R = area.circulo(v1)
    print('Area Calculada : {}'.format(R))
if r == 2:
    lado = int(input('Lado : '))
    altura = int(input('Altura : '))
    R = area.triangulo(lado,altura)
    print('Area Calculada {}'.format(R))
if r == 3:
    lado1 = int(input('Lado A : '))
    lado2 = int(input('Lado B : '))
    R = area.retangulo(lado1,lado2)
    print('Area Calculada {}'.format(R))
