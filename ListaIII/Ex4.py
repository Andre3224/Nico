# Faça um programa que receba o valor da venda, escolha a condição de pagamento no menu e mostre o total da venda final
# conforme condições a seguir:
#1 - Venda a Vista - desconto de 10%
#2 - Venda a Prazo 30 dias - desconto de 5%
#3 - Venda a Prazo 60 dias - mesmo preço
#4 - Venda a Prazo 90 dias - acréscimo de 5%
#5 - Venda com cartão de débito - desconto de 8%
#6 - Venda com cartão de crédito - desconto de 7%.

num = float(input('Digite o valor da compra: '))

opção = 0
while opção != 7:
    print('''    [1] Venda a vista
    [2] Venda a prazo (30 dias)
    [3] Venda a prazo (60 dias)
    [4] Venda a prazo (90 dias)
    [5] Venda com cartão de débito
    [6] venda Cartão de crédito
    ''')
    opção = int(input('Selecione uma opção: '))
    if opção == 1:
       
        
    elif opção == 2:
       
        
    elif opção == 3:
       
        
    elif opção == 4:
        
        
    elif opção == 5:
       
    
    elif opção == 6:
       
    else:
        print('Saindo...')
        exit()