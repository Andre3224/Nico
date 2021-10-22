#Faça um algoritmo que leia a primeira letra do estado civil de uma pessoa e
#mostre uma mensagem com a sua descrição (Solteiro, Casado, Viúvo, Divorciado, Desquitado).
#Mostre uma mensagem de erro, se necessário.

estc = str(input('Digite o seu estado civil: '))

letra = estc[0]

if letra == 's' or letra == 'S':
    print('Você é: Solteiro(a)')
    
elif letra == 'c' or letra == 'C':
    print('Você é: Casado(a)')
    
elif letra == 'v' or letra == 'V':
    print('Você é: Viúvo(a)')
    
elif letra == 'd' or letra == 'D':
    
    letra2 = estc[1]
    
    if letra2 == 'i' or letra2 == 'I':
        print('Você é: Divorciado(a)')
    else:
        print('Você é: Desquitado(a)')
        
else:
    print('Erro! Confirme os dados!')