#Crie um programa para ler uma letra e mostrar uma mensagem: se é vogal maiúscula, vogal minúscula ou consoante.
#Considere somente as letras do alfabeto.

letra = str(input('Digite uma letra: '))

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Vogal minúscula')
    
elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('Vogal maiúscula')

else:
    print('Consoante')