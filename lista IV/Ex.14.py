#Faça um programa que solicita que o usuário entre com um número.
#Calcule a tabuada (de 1 a 10) para esse valor. Utilize WHILE.

num = int(input('Digite um número: '))
x=1
vez = 0

while vez<10:
   tab = num*x
   x+=1 # x = x+1
   vez +=1
   
   print(tab)
    
    
    
