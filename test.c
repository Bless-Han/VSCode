#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

typedef int integer;

int main()
{
    int *x;
    int *y;
    x = malloc(sizeof(int));
    

    *x = 42;
    printf("%i x\n", *x);

    y = x;
    *y = 13;
    printf("%i x\n", *x);
    free(x);
}