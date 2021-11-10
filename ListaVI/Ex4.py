#Escreva a função que recebe 3 argumentos: o primeiro argumento é um vetor de inteiros e o segundo argumento é um número.
#A função deve retornar quantas vezes o número ocorre dentro do vetor.
#O tamanho máximo da matriz deve ser definido por meio de constantes.

def funcao():
    vetor = []
    x = 0
    y = int(input('Digite o número que gosta, para saber se está ou não no vetor: '))
    somatorio = 0
    while x < 8:
        z = int(input('Digite um número: '))
        vetor.append(z)
        x += 1
        
        if z == y:
            somatorio += 1
    
    if y in vetor:
       print('=' * 40)
       print('O número escolhido está no vetor!')
       print('O número', y, 'ocorre dentro do vetor', somatorio, 'vezes')
       print('=' * 40)
    
    
    else:
        print('=' * 42)
        print('O número digitado (', y,') não está no vetor!')
        print('=' * 42)

funcao()