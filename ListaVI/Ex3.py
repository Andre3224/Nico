#Dado um vetor com 10 elementos inteiros,
#substituir cada elemento por ele mesmo multiplicado pela posição do elemento no conjunto,
#para i = 0,1,2...10. Utilize procedimento.

vetor = [2,4,6,8,10,12,14,16,18,20]

def troca():
    x = 0
    while x < 10:
        vetor[0+x] *= (0+x)
        x += 1
    print(vetor)

troca()