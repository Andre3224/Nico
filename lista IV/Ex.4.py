#Utilizando WHILE escreva um programa que receba um inteiro e calcule seu fatorial.

x = int(input('Digite um número: '))
fat = 1
y = x
while (x > 0):
    fat *= x #(fat = fat * x)
    print(x)
    x -= 1 #(x = x - 1) 
    
print('O valor do fatorial de',y,'é: ', fat)