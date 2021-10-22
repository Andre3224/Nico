#Faça um algoritmo que leia n números inteiros informados pelo usuário, sendo n informado pelo usuário.
#Utilizando WHILE indique a quantidade de números pares e a quantidade de números impares.

par = []
impar = []

tam = int(input('Digite o tamanho do conjunto: '))

while tam !=0:
    x = int(input('Digite um número: '))
    
    rest = x%2
    
    if rest == 0:
        par.append(x)
    else:
        impar.append(x)
    
    tam -=1

print('-'*50)    
print('Os números pares são: ', par)
pl = len(par)
print('Existem na lista',pl, 'números pares')

print('-'*50)
print('Os números impares são: ', impar)
il = len(impar)
print('Existem na lista',il, 'números impares')
