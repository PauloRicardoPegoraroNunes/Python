"""
Created on Sun May 20 20:36:34 2018

@author: paulo
"""

ar = 20 #padrão

al = str(input('Alteração na Arrancada [S/N] ? ')).upper()


if al == 'S':
    q1 = int(input('Quanto R$: '))
    soma = ar-q1
    print('De Arrancada Ficou ',soma,' R$')
    

qt = int(input('Quantas corridas foram ? '))

s = 0
for  x in range ( 0,qt):
     y = float(input('Valor corrida : '))

     s  += y
    
if  al  == 'S':
          sm = (ar-q1)+s

else:

          sm = ar + s
print('Valor para Receber  =  ',sm,' R$')
    
    
    
  
    
    
    
     
