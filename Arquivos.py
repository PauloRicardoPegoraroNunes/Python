import sys
import os
nomelist = []
def menu():
    x = True
    while x == True:
        print(25*'-'+'MENU'+25*'-')
        print('1 - Nova Lista')
        print('2 - Consultar Lista')
        print('3 - Editar Lista')
        print('4 - Deletar Lista')
        print('5 - Sair')
        res = int(input('Escolha uma opção : '))
        if res == 1:
            nova_lista()
        if res == 2:
            consultar()
        elif res == 3:
            cadastrar()
        elif res == 4:
            deletar()
        elif res == 5:
            x = False
            print('Encerrando........')


def nova_lista():
    print(25*'-'+'NOVA LISTA'+25*'-')
    nome_lista = str(input('Nome da lista : '))
    nomelist.append(nome_lista)
    temp = open(nome_lista+'.txt','w')
    q = int(input('Quantas palavras são ? '))
    print(25*'-'+'PALAVRAS'+25*'-')

    lista = []

    for c in range(0,q):
        n = str(input('Digite : '))
        lista.append('{}\n'.format(n))

    temp.writelines(lista)
    temp.close()

def cadastrar():
    print(25*'-'+'Criar Lista'+25*'-')

    nom = str(input('Digite o nome da lista que queira modificas [.txt] : '))
    temp = open(nom,'r')
    lista = temp.readlines()


    q = int(input('Quantas palavras são ? '))
    print(25*'-'+'PALAVRAS'+25*'-')

    for c in range(0,q):
        m = str(input('Digite : '))
        lista.append('{}\n'.format(m))

    temp = open(nom,'w')
    temp.writelines(lista)
    temp.close()

def consultar():
    print(25*'-'+'PALAVRAS'+25*'-')
    t = str(input('Digite a Lista que deseja consultar [.txt] : '))
    temp = open(t,'r')
    for x in temp:
        sys.stdout.write(x)
    print(25*'-'+'FIM'+25*'-')
    temp.close()

def deletar():
    arquivo = str(input('Nome do Arquivo [.txt]: '))
    os.remove(arquivo)


menu()
