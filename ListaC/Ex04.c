#include <stdio.h>

// 4.    Faça um programa para ler dois valores (x e y), 
// calcular x multiplicado por y e imprimir o resultado.

int main ()
{
    int x;
    int y;
    float mult;
    
    printf("Digite o valor de X: ");
    scanf("%i", &x);
    
    printf("Digite o valor de Y: ");
    scanf("%i", &y);
    
    mult = (x*y);
    
    printf("O produto de X e Y é: %f\n", mult);
    
    return 0;
}