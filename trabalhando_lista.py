print('Bem vindo ao Login')

lista_nomes = open('nomes.txt','w')

print('Para se cadastrar é necessário nome e senha')
nome = str(input('Nome : '))

senha = str(input('Senha : '))

lista_nomes.writelines('\n{}'.format(nome))
lista_nomes.writelines('\n{}'.format(senha))
lista_nomes.close()

print('Pronto agora basta logar')
user = str(input('Nome : '))
password = str(input('Senha : '))


leitura = open('nomes.txt','r')


if user == nome and password == senha:
    print('Logado')
else:
    print('Erro')
