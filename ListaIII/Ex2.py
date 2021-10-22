#Escreva um programa que solicita que o usuário digite um operador matemático,
#sendo +, -,* e / as opções, e dois números inteiros.
#A partir do comando CASE realizar a operação escolhida e informar ao usuário.

x = int(input('Digite um numero: '))
y = int(input('Digite um numero: '))

opção = 0
while opção != 5:
    print('''    [1] +
    [2] -
    [3] *
    [4] /
    ''')
    opção = int(input('Selecione uma opção: '))
    if opção == 1:
       soma = x + y
       print(soma)
        
    elif opção == 2:
        sub = x - y
        print(sub)
        
    elif opção == 3:
        mult = x * y
        print(mult)
        
    elif opção == 4:
        div = x/y
        print(div)
        
    else:
        print('Saindo...')
        exit()