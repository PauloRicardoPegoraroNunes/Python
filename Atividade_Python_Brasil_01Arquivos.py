lista = open('ips.txt', 'r')

for x in lista:
    print(x)

listainvalidos = []
listavalidos = []

numero_de_ips = int(input('Quantos IPS inválidos: '))

for i in range(0, numero_de_ips):
    ips = str(input('Digite o IP : '))
    listainvalidos.append('{} \n'.format(ips))

numero_de_ips_validos = int(input('Quantos IPS validos : '))

for i in range(0, numero_de_ips_validos):
    ips_validos = str(input('Digite o IP : '))
    listavalidos.append('{}\n'.format(ips_validos))

lista2 = open('ipslog.txt', 'w')

lista2.write('[Endereços inválidos]\n')
for i in listainvalidos:
    lista2.write(i)

lista2.write('[Endereços válidos]\n')
for x in listavalidos:
    lista2.writelines(x)


lista2.close()
