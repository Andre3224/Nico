#Criar um programa que a partir dos vetores A, B e C. Calcule e exiba o vetor D.
#Perceba que o zero no vetor de respostas também indica possível erro.

A = [7,4,9,3,6]
B = ["+","-","/","*","/"]
C = [8,1,3,6,0]
D = [0,0,0,0,0]

D[0] = A[0] + C[0] 
D[1] = A[1] - C[1] 
D[2] = A[2] / C[2] 
D[3] = A[3] * C[3]

if 0 in C:
    D.append('Não pode dividir por 0')
else:
    D[4] = A[4] / C[4]

print(D)