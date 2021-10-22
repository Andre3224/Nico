#Faça um programa que mostre o menu abaixo para que o usuário selecione o tipo de cálculo que deve ser realizado:
#1-Raiz quadrada
#2-A metade
#3-10% do número
#4-O dobro
#Através do uso do CASE receba um número digitado pelo usuário e informe sobre sua escolha.
import math

num = int(input('Digite um número: '))

opção = 0
while opção != 5:
    print('''    [1] Raiz quadrada
    [2] A metade
    [3] 10% do número
    [4] O dobro
    ''')
    opção = int(input('Selecione uma opção: '))
    if opção == 1:
       raiz = math.sqrt(num)
       print(raiz)
        
    elif opção == 2:
        met = num/2
        print(met)
        
    elif opção == 3:
        dez = 0,10 * num
        print(dez)
        
    elif opção == 4:
        dobro = 2*(num)
        print(dobro)
        
    else:
        print('Saindo...')
        exit()