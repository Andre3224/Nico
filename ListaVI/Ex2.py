#Armazenar 10 valores inteiros num vetor de 10 posições.
#Após, leia o vetor e mostre os valores armazenados, adicionando em 10 unidades quando forem números pares

vetor10 = []

num = 10

while num != 0:
    
    x = int(input('Digite um número: '))
    
    if x%2 == 0:
        x += 10
        vetor10.append(x)
        num -= 1
        
    else:
        vetor10.append(x)
        num -= 1
        
print('O vetor é: ', vetor10)