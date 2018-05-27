temp = int(input('Entre com uma temperatura : '))

if temp < 0 :
    print('Congelando')
    
elif 0 <= temp <= 20 :
    print('Está Frio')
elif 21 <= temp <= 25 :
    print('Temperatura Normal')
elif 26 <= temp <=36:
    print('Está quente')
else : 
    print('Está fervendo ')
