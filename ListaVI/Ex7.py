#Armazenar 10 valores inteiros num vetor de 10 posições.
#Sequencialmente, imprima-os em ordem inversa multiplicados por 2.

vetor = []
vetor2= []
num = 5

while num !=0:
    x = int(input('Digite um número: '))   
    vetor.append(x)
    num -= 1

vetor.sort(reverse=True)
vetor2 = vetor

quant = 5
z = 0
while quant !=0:
    vetor2[0+z] = vetor[0+z] * 2
    quant -= 1
    z += 1
    
print('O vetor é: ', vetor2)