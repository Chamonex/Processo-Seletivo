#include <stdio.h>

int fibonacci(int a, int b, int n) {
    // função recursiva de fibonacci;

    if (a+b == n)
        return 1;   // encontrou o número
    
    else if (a+b > n)
        return 0;   // passou do número

    else
        return fibonacci(b, (a+b), n);
}

void main() {

    int n;          
    scanf("%d", &n);

    if (fibonacci(0, 1, n))
        printf("o numero informado PERTENCE a sequencia de fibonacci\n");
    else
        printf("O numero informado NAO pertence a sequencia de fibonacci\n");
}