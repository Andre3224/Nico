#Escreva um algoritmo que leia o número de elementos de uma progressão aritmética (PA),
#o primeiro termo dessa progressão e a razão da progressão.
#Utilizando WHILE e escreva os n termos desta progressão, bem como a soma dos elementos.

PA =[]

tam = int(input('Digite o tamanho da PA: '))
raz = int(input('Digite a razão da PA: '))
a1 = int(input('Digite o primeiro termo da PA: '))

PA.append(a1)
an = a1
tam -= 1  

while tam != 0:
    an = an + raz
    PA.append(an)
    tam -= 1

z = sum(PA)

print(PA)
print('A soma dos termos é: ',z)