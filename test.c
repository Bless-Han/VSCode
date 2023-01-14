#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

typedef int integer;

int main()
{
    int *m = malloc(3 * sizeof(int));
    m[0] = 9;
    m[1] = 20;
    m[4] = 22;
    printf("%i\n", m[4]);
    free(m);
    return 0;
}