#include <stdio.h>

// 3.    Escreva um programa para ler, calcular e escrever a 
// média aritmética entre dois números.
int main ()
{
    int num1;
    int num2;
    float med;
    
    printf("Digite o primeiro número: ");
    scanf("%i", &num1);
    
    printf("Digite o segundo número: ");
    scanf("%i", &num2);
    
    med = (num1 + num2)/2;
    
    printf("A média é: %f\n", med);
    
    return 0;
}