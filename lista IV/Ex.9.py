#Faça um algoritmo que leia um conjunto de n inteiros, sendo n informado pelo usuário.
#Utilizando WHILE imprima o maior e menor dado informado.

conj = []

tam = int(input('Digite o tamanho do conjunto: '))

while tam !=0:
    x = int(input('Digite um número: '))
    conj.append(x)
    tam -=1
    
print(conj)

men = min(conj)
mai = max(conj)

print('O menor número é: ', men)
print('O maior número é: ', mai)