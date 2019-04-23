import math

def infos():
    print('Seja bem vindo à calculadora X9!\n')
    print('Como eu uso?:\n')
    print('Escolha 5 números, e digite-os, e a calculadora dará o resultado.\n')
    print('Mas, se eu quiser digitar menos de 5 números?:\n')
    print('Se quiser usar menos de 5 números é fácil, deixe 0 no lugar de algum número.\n')
    print('Para conseguir utilizar a calculadora X9, faça um registro que está logo abaixo.\n')
    print('REGISTRO:\n')

def pessoa():
    nome = input('Qual o seu nome? ')
    idade = input('Qual a sua idade? ')
    signo = input('Qual o seu signo? ')
    print('Agora você pode utilizar a calculadora X9!\n')

def menu():
    while True:
        
        print('1 - Soma')
        print('2 - Subtração')
        print('3 - Divisão')
        print('4 - Multiplicação')
        print('5 - Sair\n')
        r = int(input('Escolha : '))

        if r == 1:
            soma()
        elif r == 2:
            sub()
        elif r == 3:
            div()
        elif r == 4:
            mult()
        elif r == 5:
            print('Obrigado por utilizar a calculadora X9\n')
            print('Criador: Paulo Ricardo\n')
            print('Linguagem utilizada: Python\n')
            break
        else:
            print('Valor inválido')



def soma():
    n = float(input('Valor : '))
    n2 = float(input('Valor : '))
    somas = n + n2
    print('O Resultado Da Soma: {}\n'.format(somas))
 
def div():
    n = float(input('Valor : '))
    n2 = float(input('Valor : '))
    div = n/n2
    print('O Resultado Da Divisão: {}\n'.format(div))
  
def sub():
    n = float(input('Valor : '))
    n2 = float(input('Valor : '))
    sub = n - n2
    print('O Resultado Da Soma: {}\n'.format(sub))
  
def mult():
    n = float(input('Valor : '))
    n2 = float(input('Valor : '))
    mult = n * n2
    print('O Resultado Da Soma: {}\n'.format(mult))
  
