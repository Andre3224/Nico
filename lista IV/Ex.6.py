#Utilizando FOR faça um algoritmo que leia um conjunto x elementos, sendo x informado pelo usuário, e imprima sua soma e média.
lista=[]
x = int(input('Digite o tamanho do conjunto: '))
divd = x
while x != 0:
    y = int(input('Digite um número: '))
    x -= 1
    lista.append(y)
    
    
z = sum(lista)
méd = z/divd

print('A lista de elementos é, ', lista)
print('A soma dos elementos é: ', z)
print('A média é: ', méd) 