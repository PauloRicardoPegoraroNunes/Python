"""
Created on Sat May 19 18:39:05 2018

@author: paulo
"""

print('###########################################')
print('Bem Vindo ao Calculo de Trapésio'.upper())
print('###########################################')
      
      
      
l1menor = float(input('Digite o Lado Menor : '))
l2maior = float(input('Digite o Lado Maior : '))
l3altura = float(input('Digite  a Altura   : '))


calculo = ((l2maior+l1menor)*l3altura)/2


print('Seu trapésio possui  : ',calculo,' CM')
