#Faça um programa que receba 10 valores inteiros digitados pelo usuário e os armazene em um vetor.
#Sequencialmente faça a impressão desses valores.

vetor = []

num = 10

while num !=0:
    x = int(input('Digite um número: '))
    vetor.append(x)
    num -= 1

vetor.sort(reverse=False)
print('O vetor é: ', vetor)