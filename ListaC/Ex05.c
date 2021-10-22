#include <stdio.h>

// 5.    Faça um programa que leia dois números reais e em seguida mostre: 
// a soma, o produto, a divisão e a subtração entre el

int main ()
{
    int x;
    int y;
    float soma;
    float sub;
    float mult;
    float divs;
    
    printf("Digite o valor de X: ");
    scanf("%i", &x);
    
    printf("Digite o valor de Y: ");
    scanf("%i", &y);
    
    mult = (x*y);
    divs = (x/y);
    sub = (x-y);
    soma = (x+y);
    
    printf("A soma entre X e Y é: %f\n", soma);
    printf("O produto de X e Y é: %f\n", mult);
    printf("A subtração entre X e Y é: %f\n", sub);
    printf("A divisão de X por Y é: %f\n", divs);
    
    return 0;
}