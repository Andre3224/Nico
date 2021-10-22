#Utilizando WHILE faça um algoritmo que leia um conjunto x elementos,
#sendo x informado pelo usuário, e imprima sua soma e média.

print('Bem vindo ao programa :)')

x = int(input('Digite o tamanho do conjunto que quer calcular: '))
a = x
soma = 0

while x != 0:
    y = int(input('Digite um número: '))
    x -= 1
    soma = soma + y
    méd = soma/a
    
print(soma)
print(méd)