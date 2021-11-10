#Faça um programa que leia dois vetores A e B contendo, cada um, 10 elementos inteiros.
#Intercale estes dois conjuntos (A[1] - B[1] - A[2] - B[2]) formando um novo vetor de 20 elementos.
#Imprima o novo vetor.

A = []
B = []

vetorAB = []

tam = 10

while tam != 0:
    print('-'*40)
    x = int(input('Digite um número para o vetor A: '))
    A.append(x)
    print('-'*40)
    y = int(input('Digite um número para o vetor B: '))
    B.append(y)
    vetorAB.append(x)
    vetorAB.append(y)
    tam -= 1
    
print('='*80)
print('O vetor A é: ', A)
print('-'*80)
print('O vetor B é: ', B)
print('-'*80)
print('O vetor AB é: ', vetorAB)
print('='*80)