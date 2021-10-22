#7. Um determinado clube de futebol pretende classificar seus atletas em
#categorias e para isto ele contratou um programador para criar um programa que executasse esta tarefa.
#Para isso o clube criou uma tabela que continha a faixa etária do atleta e sua categoria.
#A tabela está demonstrada abaixo:

#IDADE CATEGORIA
#De 05 a 10 Infantil
#De 11 a 15 Juvenil
#De 16 a 20 Junior
#De 21 a 25 Profissional

#Construa um programa que solicite o nome e a idade de um atleta e imprima a sua categoria.

nome = str(input('Digite nome do atleta: '))

idd = int(input('Digite a idade do atleta: '))

if 5 <= idd <= 10:
    print('-'*60)
    print('O atleta ', nome, 'é: Infantil')
    print('-'*60)
    
elif 11 <= idd <= 15:
    print('-'*60)
    print('O atleta ', nome, 'é: juvenil')
    print('-'*60)

elif 16 <= idd <= 20:
    print('-'*60)
    print('O atleta ', nome, 'é: Junior')
    print('-'*60)
    
elif 21 <= idd <= 25:
    print('-'*60)
    print('O atleta ', nome, 'é: Profissional')
    print('-'*60)

else:
    print('-'*60)
    print('O atleta ', nome, 'não possui idade listada na tabela!')
    print('-'*60)