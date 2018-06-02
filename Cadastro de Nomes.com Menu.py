"""
Created on Sat Jun  2 02:43:19 2018

@author: programer
"""

nomes = []


def menu():
    print('Cadastrar[1]')
    print('Consultar[2]')
    print('sair[3]')
    
    y = int(input('Digite um Opção : '))
    
    if y == 1:
        cadastro()
        print('###############################')
        menu()
        
    if y == 2:
        print('#################################')
        for v in nomes:
            print('Cadastrados: '.upper(),v)
        print('###############################')
        menu()
            
    
    if y == 3:
        print('saindo')
    

def cadastro():
    
    x = int(input('Quantos nomes : '))
    
    for x in range(0,x):
        nome = str(input('Nomes :'))
        nomes.append(nome)
        
    return cadastro


menu()
